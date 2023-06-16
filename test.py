import time
from random import randrange, shuffle


from random import randint
from random import randrange
'''
Population Size - N
Stratum Number - K
Stratum Size - Ni
Sample Size - n
'''

def dowellProportionalAllocation(N, n, Ni): 
    ni = int((Ni * n) / N)
    return ni

def dowellEqualAllocation(n, k):
    ni = int(n / k)
    return ni
def dowellRandomGeneration(N, n, Yi):
    sampleUnits = []
    try:
        rand_nos = [randrange(0, N) for _ in range(n)]
        sampleUnits = [Yi[i] for i in rand_nos]
    except IndexError:
        return "Error: The specified index is out of range. Please try again increase or decrease the value."


    return sampleUnits

def dowellRandomTable(N, n, Yi):
    sampleUnits = []
    page_no = 10
    rows = 10
    columns = 10
    for _ in range(n):
        rand_page = randint(1, page_no)
        rand_row = randint(1, rows)
        rand_col = randint(1, columns)
        a = f"Enter the number in page: {rand_page} row: {rand_row} column: {rand_col}: "
        random_no = 6
        # check if random_no is greater than N eg if random_no = 0234 and
        # N is 100 pick the first 3 digits (023)
        if random_no > N:
            rand_len = len(str(N))
            # Pick the first N digits.
            rand_index = int(str(random_no)[:rand_len])
            # check if random_no is greater than N eg if random_no = 123456 and
            # N is 100 pick the first 3 digits (123)
            # eg 123 > 100
            if rand_index >= N:
                rand_index %= N
        else:
            rand_index = random_no

        try:
            sampleUnits.append(Yi[rand_index])
        except IndexError:
            return "Error: The specified index is out of range. Please try again with valid input or increase or decrease value."

    return sampleUnits


def dowellGeometricalFunction(N, n, Yi):
    # inscribe the circle randomly by starting from a random index
    start = randrange(0, N)
    Yi = Yi[start:] + Yi[:start]
    # partition the population list into 3 parts corresponding to the areas
    # where the triangle touches the circle x, y and z are the three regions
    # in which the triangle will rotate
    partition = N // 3
    x, y, z = (
        Yi[:partition],
        Yi[partition : (2 * partition)],
        Yi[(2 * partition) :],
    )
    # check if lists x, y, and z have at least one element
    if len(x) > 0 and len(y) > 0 and len(z) > 0:
        sampleUnits = []
        for _ in range(n // 3):
            # check if indices are within the bounds of the lists
            if len(x) > 0 and len(y) > 0 and len(z) > 0:
                sampleUnits.append([x[0], y[0], z[0]])
                # rotate by 1 value
                x = x[1:] + x[:1]
                y = y[1:] + y[:1]
                z = x[1:] + z[:1]
            else:
                return []  # or handle the error condition as per your requirements
        return sampleUnits
    else:
        return "Please decrease or increase the value of 'N' to ensure at least 3 units in each partition."

def dowellSampleSize(N, e):
    n = int(N / (1 + N * e * e))
    print(n)
    if n > 1 and n < 500:
        return n
    else:
        return "Sample size is not adequate"

def dowellSimpleRandomSampling(simpleRandomSamplingInput):
    Yi = simpleRandomSamplingInput['Yi']
    N = simpleRandomSamplingInput['N']
    n = simpleRandomSamplingInput['n']
    method = simpleRandomSamplingInput['method']
    # print(Yi)
    # lengths = [len(item) for sublist in Yi for item in sublist]
    # variance = pvariance(lengths)
    variance = 0.23
    simpleRandomSamplingOutput = {
        'status': True
    }
    if variance > 1:
        simpleRandomSamplingOutput['message'] = "Simple random sampling cannot be used"
        simpleRandomSamplingOutput['status'] = False
    else:
        if method == 'geometricalApproach':
            simpleRandomSamplingOutput['sampleUnits'] = dowellGeometricalFunction(N, n, Yi)
        elif method == 'mechanicalRandomisation':
            simpleRandomSamplingOutput['sampleUnits'] = dowellRandomTable(N, n, Yi)
        elif method == 'randomNumberGeneration':
            simpleRandomSamplingOutput['sampleUnits'] = dowellRandomGeneration(N, n, Yi)
        else:
            simpleRandomSamplingOutput['message'] = f'{method} is not a valid method. Select a valid method from geometricalApproach, mechanicalRandomisation, or randomNumberGeneration'
            simpleRandomSamplingOutput['status'] = False
        shuffle(Yi)
    return simpleRandomSamplingOutput

def dowellStratifiedSampling(stratifiedSamplingInput):

  stratifiedSamplingOutput = {}
  allStratas = {}
  ni = {}
  stratas = []

  e = stratifiedSamplingInput['e']
  allocationType = stratifiedSamplingInput['allocationType']
  samplingType = stratifiedSamplingInput['samplingType']
  insertedId = stratifiedSamplingInput['insertedId']
  replacement = stratifiedSamplingInput['replacement']

  Yi = stratifiedSamplingInput['Yi']
  N = int(stratifiedSamplingInput['populationSize'])
  for i in range(len(Yi[0])):
    stratas.append(i)
  k = len(stratas)
  if replacement == True:
    for i in stratas:
        tempList = []
        for j in range(len(Yi)):
            tempList.append(Yi[j][i])
        allStratas[i] = tempList
  elif replacement == False:
    for i in stratas:
        tempSet = set()
        for j in range(len(Yi)):
            tempSet.add(Yi[j][i])
        allStratas[i] = list(tempSet)
  else:
    stratifiedSamplingOutput['message'] = f'{replacement} is not a valid option for replacement, select either True or False'

  n = dowellSampleSize(N, e)
  if isinstance(n, int):
    for i in range(1, k+1):
      if allocationType == 'equal':
        ni[stratas[i-1]] = dowellEqualAllocation(n, k)
      
      elif allocationType == 'proportional':
        Ni = len(allStratas[stratas[i-1]])
        ni[stratas[i-1]] = dowellProportionalAllocation(N, n, Ni)
      
      else:
        stratifiedSamplingOutput['message'] = f'{allocationType} is not a valid allocation type, select either equal or proportional allocation type'
  
  else:
    stratifiedSamplingOutput['message'] = n
  simpleRandomSamplingInput = {
            'Yi': Yi,
            'N': int(N),
            'n': n,
            'method': stratifiedSamplingInput['samplingType'],
        }
  simpleRandomSamplingOutput = dowellSimpleRandomSampling(simpleRandomSamplingInput)
  if simpleRandomSamplingOutput['status'] == True:
    stratifiedSamplingOutput['sampleUnits'] = simpleRandomSamplingOutput['sampleUnits']
  else:
    stratifiedSamplingOutput['message'] = simpleRandomSamplingOutput['message']

  return stratifiedSamplingOutput


def dowellmultistagesampling():
    # Define the number of stages
    S = int(input("Enter the number of stages: "))
    if(1<S<=5):
        
    # List to store the selected units at each stage
        sample_values = []

        # Iterate over each stage
        for stage in range(1, S+1):
            print(f"\nStage {stage}:")
            
            # Choose the sampling method for the current stage
            sampling_method = dowellindex()
            
            # Check if the user entered "0" for the current stage
            if sampling_method == 0:
                print("Sampling stopped.")
                break
            
            # Determine the number of units to be selected in the current stage
            si = dowellSampleSize(stage,0.5)
            
            # Check if the selected sampling method is Simple Random Sampling
            if sampling_method == 1:
                sample = dowellSimpleRandomSampling(si)
            # Check if the selected sampling method is Stratified Sampling
            elif sampling_method == 2:
                sample = dowellStratifiedSampling(si)
            else:
                print("Invalid sampling method.")
                continue
            
            # Add the selected sample to the list of sample values
            sample_values.append(sample)
        
        # Process time
        process_time = time.process_time()
        
        # Permutation chosen
        permutation_chosen = None  # Placeholder for permutation chosen
        
        return sample_values, process_time, permutation_chosen
    else:
        return ("enter adequate number of Stages",0,0)

import time

def dowellindex():
    # Display the list of sampling techniques
    methods = {
        0: "No sampling",
        1: "Simple random sampling WR",
        2: "Simple random sampling WOR",
        3: "Stratified random sampling WR",
        4: "Stratified random sampling WOR",
        5: "Systematic (Linear) Sampling",
        6: "Circular Systematic Sampling",
        7: "Cluster Sampling",
        8: "Purposive or judgement sampling",
        9: "PPS WR",
        10: "PPS WOR",
        11: "Snowball sampling",
        12: "Quota Sampling"
    }
    
    print("Sampling Techniques:")
    for num, method in methods.items():
        print(f"{num}. {method}")
    
    while True:
        selected_method = int(input("Choose a sampling technique (0 to 12): "))
        
        if selected_method in methods:
            break
        else:
            print("Enter an appropriate number.")
    
    print(f"Selected Method: {selected_method} - {methods[selected_method]}")
    
    return selected_method

import time

def dowellsnowballsampling(Yi, N, n, Ri):
    sample_units = []
    process_time = 0
    print("Select the first unit to be included in the sample:")
    unit_1 = input()
    sample_units.append(unit_1)
    print(f"Find a connection/reference from {unit_1} to select the second unit in the sample:")
    R1 = input()
    for i in range(2, n+1):
        print(f"Select the {i}th unit to be included in the sample:")
        unit_i = input()

        valid_connection = False
        while not valid_connection:
            print(f"Find a connection/reference from {unit_i} (excluding {R1}) for the {i}th unit:")
            Ri = input()

            if Ri == R1:
                print("Select another connection. It should not be the same as the previous connection.")
            else:
                valid_connection = True

        sample_units.append(unit_i)

    # Calculate the process time
    process_time = time.process_time()

    return sample_units, process_time


def main():
    Yi = input("Enter the population units: ")
    N = int(input("Enter the population size: "))
    n = int(input("Enter the sample size: "))
    Ri = input("Enter the reference: ")

    sample_units, process_time = dowellsnowballsampling(Yi, N, n, Ri)

    print("\nSample units:",sample_units)

    print(f"\nProcess time: {process_time} seconds")


if __name__ == "__main__":
    main()


# Example usage
# sample_values, process_time, permutation_chosen = dowellmultistagesampling()
# print("Sample Values:", sample_values)
# print("Process Time:", process_time)
# print("Permutation Chosen:", permutation_chosen)





# start																									
# 	Call dowellmultistagesampling(Number of Stages,First Stage Units,Second Stage units,...)																								
																									
# 		Define number of stages as variable "S"																							
# 			Input from user																						
# 		Choose sampling method from the list containing all the sampling techniques for First stage units																							
# 			Call dowellindex()																						
# 				input from user or frontend programmer																					
# 		Choose sampling method from the list containing all the sampling techniques for Second stage units																							
# 			Call dowellindex()																						
# 				input from user or frontend programmer																					
# 		Choose sampling method from the list containing all the sampling techniques for Third stage units																							
# 			Call dowellindex()																						
# 				input from user or frontend programmer																					
# 		Continue this depending on number of stages																							
																									
# 		Define number of units to be selected in each stage as variable "si"																							
# 			Call dowellsamplesize() for each stage																						
																									
# 			Check number of stages S																						
# 				if  1<S<=5,then continue																					
# 				if not,prompt " enter adequate number of Stages																					
																									
# 			For first stage,check																						
# 				if user has entered "0",then prompt "not allowed"																					
# 				Choose from 1 to 12																					
																									
# 			If selected sampling method is Simple Random Sampling																						
# 				Call dowellrandomsampling()																					
# 			If selected sampling method is Simple Random Sampling																						
# 				Calldowellstratifiedsampling()																					
# 			Continue this depending on the selections for each stage																						
																									
# 		if for any stage(except first stage) user has entered "0",then the function should stop at that stage only																							
																									
																									
# 	Function output(sample values at each stage,process time,permutation chosen)	