import json
import requests

url = "http://100072.pythonanywhere.com/api"

params = {
    "deck": 100,  # enter any number more than 100
    "error": 0.168,  # any float number
    "test_num": 7,  # intecdger number
    "deck_items": '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100' #items to be shuffled, replace with data from database
}


get_response = requests.post(url, params)

data = get_response.text
parse_json = json.loads(data)

series = parse_json['SeriesDataframe']
optimum_series = parse_json['OptimumSeries']
means = parse_json['MeansDataframe']
number = parse_json['CentralLimitTheorem']
image_file = parse_json['image']

print(f'Optimum Shuffled Series Data:\n {optimum_series}')
print(f'Series Dataframe:\n {series}')
print(f'Means Dataframe: \n {means}')
print(f'Number of Iterations = {number}')
print(f'Image file byte code: \n{image_file}')
# replace deck items with the data and the deck with size of the data