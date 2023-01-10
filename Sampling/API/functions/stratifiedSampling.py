'''
Population Units - Yi
Population Size - N
Sample Size - n
Number of Stratas - k
Population Strata Size - Ni
Stratum Sample Size - ni
Error - e
Allocation Type - allocationType
'''
from API.functions.testDatabase import databaseTwo, databaseOne
from API.functions.sampleSize import dowellSampleSize
from API.functions.allocation import dowellEqualAllocation, dowellProportionalAllocation
import requests
import json

def populationData(insertedId):
  url = "http://100061.pythonanywhere.com/api/"
  payload = json.dumps({
    "inserted_id": insertedId,
    })
  headers = {
    'Content-Type': 'application/json'
    }
  response = requests.request("POST", url, headers=headers, data=payload).json()
  Yi = response['classifiedData']
  return Yi

def dowellStratifiedSampling(stratifiedSamplingInput):
  e = stratifiedSamplingInput['e']
  allocationType = stratifiedSamplingInput['allocationType']
  samplingType = stratifiedSamplingInput['samplingType']
  insertedId = stratifiedSamplingInput['insertedId']
  # Yi = populationData(insertedId)  
  Yi = databaseTwo()
  N = len(Yi)
  allStratas = {}
  stratas = []
  for i in  Yi[0].keys():
    stratas.append(i)

  k = len(stratas)
  
  for i in stratas:
      tempSet = set()
      for j in Yi:
          tempSet.add(j[i])
      allStratas[i] = list(tempSet)
  stratifiedSamplingOutput = {}
  ni = {}
  n = dowellSampleSize(N, e)
  if(type(n)== int):
    for i in range(1, k+1):
      if(allocationType == 'equal'):
        ni[stratas[i-1]] = dowellEqualAllocation(n, k)
      elif(allocationType == 'proportional'):
        Ni = len(allStratas[stratas[i-1]])
        ni[stratas[i-1]] = dowellProportionalAllocation(N, n, Ni)
      else:
        stratifiedSamplingOutput['message'] = f'{allocationType} is not a valid allocation type, select a either equal or proportional allocation type'
  else:
     stratifiedSamplingOutput['message'] = n
  print("Yi is ", Yi)
  print("stratas is ", stratas)
  print("k is ", k)
  print("allStratas is ", allStratas)
  print("ni is ", ni)
  print("N is ", N)
  print("n is ", n)
  return stratifiedSamplingOutput


dowellStratifiedSampling({
  'e': 0.1,
  'insertedId': "dsfsdfsd",
  'samplingType':"",
  # 'allocationType': "equal",
  'allocationType': "proportional",
})