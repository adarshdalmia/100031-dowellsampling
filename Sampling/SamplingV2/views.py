import os
import pandas as pd
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
import json
import requests
from API.functions.stratifiedSampling import dowellStratifiedSampling
from API.functions.sampleSize import dowellSampleSize
from API.functions.systematic_sampling import dowellSystematicSampling
from API.functions.simpleRandomSampling import dowellSimpleRandomSampling
from API.functions.clusterSampling import dowellClusterSampling
from API.functions.purposiveSampling import dowellPurposiveSampling


def processApikey(api_key):
    url = f'https://100105.pythonanywhere.com/api/v3/process-services/?type=api_service&api_key={api_key}'
    payload = {
        "service_id": "DOWELL10011"
        # "service_id": "DOWELL10011"
    }

    response = requests.post(url, json=payload)
    return response.text


@csrf_exempt
def get_event_id():
    url = "https://uxlivinglab.pythonanywhere.com/create_event"

    data = {
        "platformcode": "FB",
        "citycode": "101",
        "daycode": "0",
        "dbcode": "pfm",
        "ip_address": "192.168.0.41",  # get from dowell track my ip function
        "login_id": "lav",  # get from login function
        "session_id": "new",  # get from login function
        "processcode": "1",
        "location": "22446576",  # get from dowell track my ip function
        "objectcode": "1",
        "instancecode": "100051",
        "context": "afdafa ",
        "document_id": "3004",
        "rules": "some rules",
        "status": "work",
        "data_type": "learn",
        "purpose_of_usage": "add",
        "colour": "color value",
        "hashtags": "hash tag alue",
        "mentions": "mentions value",
        "emojis": "emojis",
        "bookmarks": "a book marks",
    }

    r = requests.post(url, json=data)
    if r.status_code == 201:
        return json.loads(r.text)
    else:
        return json.loads(r.text)["error"]


@csrf_exempt
def get_YI_data():
    header = {"content-type": "application/json"}
    data = json.dumps({"insertedId": "646d188771d319c4cf8e182a"})
    url = "http://100061.pythonanywhere.com/function/"
    response = requests.request("POST", url, data=data, headers=header).json()
    data = response["finalOutput"]
    return data


def get_YI_data_systematic():
    hardcoded_data = [
        "Apple", "Banana", "Cherry", "Date", "Fig",
        "Grape", "Kiwi", "Lemon", "Mango", "Orange",
        "Peach", "Pear", "Quince", "Raspberry", "Strawberry",
        "Watermelon", "Blueberry", "Pineapple", "Pomegranate", "Guava"
    ]
    return hardcoded_data


def get_YI_data_simplerandom():
    hardcoded_data = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    return hardcoded_data


@csrf_exempt
def systematic_sampling(request, api_key):
    validate_api_count = processApikey(api_key)
    data_count = json.loads(validate_api_count)
    if data_count['success']:
        if data_count['total_credits'] >= 0:
            if request.method == "POST":
                json_data = request.POST.get('json_data')  # Retrieve the JSON data as a string
                print("json_data", json_data)
                try:
                    # Parse JSON data from the request body
                    json_data = json.loads(json_data)
                    inserted_id = json_data.get("insertedId")
                    population_size = json_data.get("populationSize")
                    result = json_data.get("result")
                    data_type = json_data.get("data")

                    if data_type == "api":
                        Yi = get_YI_data_systematic()
                    elif data_type == "upload":
                        uploaded_file = request.FILES.get('file')
                        if uploaded_file:
                            df = pd.read_excel(uploaded_file)
                            list_of_lists = df.values.T.tolist()
                            Yi = list_of_lists
                        else:
                            return JsonResponse({"error": "No file uploaded."})
                    elif data_type == "link":
                        excel_link = json_data.get("link")
                        if excel_link:
                            df = pd.read_excel(excel_link)
                            list_of_lists = df.values.T.tolist()
                            Yi = list_of_lists
                        else:
                            return JsonResponse({"error": "No link provided."})
                    else:
                        return JsonResponse({"error": "Invalid data option."})

                    systematicSamplingInput = {
                        "insertedId": inserted_id,
                        "population": Yi,
                        "population_size": population_size,
                    }

                    samples = dowellSystematicSampling(systematicSamplingInput)
                    response = {"samples": samples}

                    if result == "Table":
                        return render(request, "result.html", {"response": response})
                    return JsonResponse(response, safe=False)

                except Exception as e:
                    return JsonResponse({"error": str(e)})
            return JsonResponse({"error": "Invalid request method."})
        else:
            return JsonResponse({
                "success": False,
                "message": data_count['message'],
                "credits": data_count['total_credits']
            })
    else:
        return JsonResponse({
            "success": False,
            "message": data_count['message']
        })


@csrf_exempt
def simple_random_sampling(request, api_key):
    validate_api_count = processApikey(api_key)
    data_count = json.loads(validate_api_count)
    if data_count['success']:
        if data_count['total_credits'] >= 0:
            if request.method == "POST":
                json_data = request.POST.get('json_data')
                try:
                    data = json.loads(json_data)
                    print(data)
                    inserted_id = data.get("insertedId")
                    N = data.get("populationSize")
                    e = data.get("e")
                    method = data.get("samplingType")
                    n = dowellSampleSize(int(N), float(e))
                    result = data.get("result")
                    data_type = data.get("data")

                    if data_type == "api":
                        Yi = get_YI_data_simplerandom()

                    elif data_type == "upload":
                        uploaded_file = request.FILES.get('file')
                        if uploaded_file:
                            df = pd.read_excel(uploaded_file)
                            list_of_lists = df.values.T.tolist()
                            Yi = list_of_lists
                        else:
                            return JsonResponse({"error": "No file uploaded."})
                    elif data_type == "link":
                        excel_link = data.get("link")
                        if excel_link:
                            df = pd.read_excel(excel_link)
                            list_of_lists = df.values.T.tolist()
                            Yi = list_of_lists
                        else:
                            return JsonResponse({"error": "No link provided."})
                    else:
                        return JsonResponse({"error": "Invalid data option."})

                    simpleRandomSamplingInput = {
                        "insertedId": inserted_id,
                        "Yi": Yi,
                        "N": int(N),
                        "e": float(e),
                        "method": method,
                        "n": n,
                    }

                    samples = dowellSimpleRandomSampling(simpleRandomSamplingInput)
                    response = {"samples": samples["sampleUnits"]}

                    if result == "Table":
                        return render(request, "result.html", {"response": response})
                    return JsonResponse(response, safe=False)

                except Exception as e:
                    return JsonResponse({"error": str(e)})
            return JsonResponse({"error": "Invalid request method."})
        else:
            return JsonResponse({
                "success": False,
                "message": data_count['message'],
                "credits": data_count['total_credits']
            })
    else:
        return JsonResponse({
            "success": False,
            "message": data_count['message']
        })


@csrf_exempt
def purposive_sampling(request, api_key):
    validate_api_count = processApikey(api_key)
    data_count = json.loads(validate_api_count)
    if data_count['success']:
        if data_count['total_credits'] >= 0:
            if request.method == "POST":
                try:
                    json_data = request.POST.get('json_data')
                    data = json.loads(json_data)
                    # data = json.loads(request.body)
                    print(data)
                    inserted_id = data.get("insertedId")
                    unit = data.get("unit")
                    e = data.get("e")
                    N = data.get("N")
                    result = data.get("result")

                    if data["data"] == "api":
                        Yi = get_YI_data()  # Make sure you have a function for this
                    elif data["data"] == "upload":
                        uploaded_file = request.FILES.get("file")
                        if uploaded_file:
                            df = pd.read_excel(uploaded_file)
                            list_of_lists = df.values.T.tolist()
                            Yi = list_of_lists
                        else:
                            return JsonResponse({"error": "No file uploaded."})
                    elif data["data"] == "link":
                        excel_link = data.get("link")
                        if excel_link:
                            df = pd.read_excel(excel_link)
                            list_of_lists = df.values.T.tolist()
                            Yi = list_of_lists
                        else:
                            return JsonResponse({"error": "No link provided."})
                    else:
                        return JsonResponse({"error": "Invalid data option."})

                    new_yi = sum(Yi, [])
                    purposiveSamplingInput = {
                        "insertedId": inserted_id,
                        "Yi": new_yi,
                        "unit": unit,
                        "e": float(e),
                        "N": int(N),
                    }

                    # print(f"purposiveSamplingInput : {purposiveSamplingInput}")

                    samples = dowellPurposiveSampling(purposiveSamplingInput)
                    print(f"samples : {samples}")
                    id = get_event_id()  # Make sure you have a function for this
                    response = {"event_id": id["event_id"], "samples": samples}
                    # response = {"event_id": id["event_id"], "samples": samples["sampleUnits"]}

                    # response = {}

                    if result == "Table":
                        return render(request, "result.html", {"response": response})
                    return JsonResponse(response, safe=False)

                except Exception as e:
                    return JsonResponse({"error": str(e)})
            return JsonResponse({"error": "Invalid request method."})
        else:
            return JsonResponse({
                "success": False,
                "message": data_count['message'],
                "credits": data_count['total_credits']
            })
    else:
        return JsonResponse({
            "success": False,
            "message": data_count['message']
        })


@csrf_exempt
def cluster_sampling(request, api_key):
    validate_api_count = processApikey(api_key)
    data_count = json.loads(validate_api_count)
    if data_count['success']:
        if data_count['total_credits'] >= 0:
            if request.method == "POST":
                try:
                    json_data = request.POST.get('json_data')
                    data = json.loads(json_data)

                    # data = json.loads(request.body)

                    inserted_id = data.get("insertedId")
                    numberOfClusters = data.get("numberOfClusters")
                    M = data.get("numberOfClusters")  # Same as numberOfClusters
                    N = data.get("populationSize")
                    e = data.get("e")
                    sizeOfCluster = data.get("sizeOfCluster")
                    result = data.get("result")

                    if data["data"] == "api":
                        Yi = get_YI_data()  # Make sure you have a function for this
                    elif data["data"] == "upload":
                        uploaded_file = request.FILES.get("file")
                        if uploaded_file:
                            df = pd.read_excel(uploaded_file)
                            list_of_lists = df.values.T.tolist()
                            Yi = list_of_lists
                        else:
                            return JsonResponse({"error": "No file uploaded."})
                    else:
                        return JsonResponse({"error": "Invalid data option."})

                    clusterSamplingInput = {
                        "Yi": Yi,
                        "e": float(e),
                        "N": int(N),
                        "M": int(M),
                        "hi": int(sizeOfCluster),  # Using sizeOfCluster as hi
                    }

                    samples = dowellClusterSampling(clusterSamplingInput)

                    print(f"samples : {samples}")

                    id = get_event_id()  # Make sure you have a function for this
                    # response = {"event_id": id["event_id"], "samples": samples["sampleUnits"]}
                    response = {"event_id": id["event_id"], "samples": samples}

                    if result == "Table":
                        return render(request, "result.html", {"response": response})
                    return JsonResponse(response, safe=False)

                except Exception as e:
                    return JsonResponse({"error": str(e)})
            return JsonResponse({"error": "Invalid request method."})
        else:
            return JsonResponse({
                "success": False,
                "message": data_count['message'],
                "credits": data_count['total_credits']
            })
    else:
        return JsonResponse({
            "success": False,
            "message": data_count['message']
        })


@csrf_exempt
def stratified_sampling(request, api_key):
    validate_api_count = processApikey(api_key)
    data_count = json.loads(validate_api_count)
    if data_count['success']:
        if data_count['total_credits'] >= 0:
            if request.method == "POST":
                try:
                    json_data = request.POST.get('json_data')
                    data = json.loads(json_data)

                    inserted_id = data.get("insertedId")
                    allocation_type = data.get("allocationType")
                    sampling_type = data.get("samplingType")
                    replacement = data.get("replacement")
                    populationSize = data.get("populationSize")
                    result = data.get("result")

                    if data["data"] == "api":
                        Yi = get_YI_data()  # Make sure you have a function for this
                    elif data["data"] == "upload":
                        uploaded_file = request.FILES.get("file")
                        if uploaded_file:
                            df = pd.read_excel(uploaded_file)
                            list_of_lists = df.values.T.tolist()
                            Yi = list_of_lists
                        else:
                            return JsonResponse({"error": "No file uploaded."})
                    else:
                        return JsonResponse({"error": "Invalid data option."})

                    stratifiedSamplingInput = {
                        "insertedId": inserted_id,
                        "e": 0.1,
                        "allocationType": allocation_type,
                        "samplingType": sampling_type,
                        "replacement": replacement,
                        "Yi": Yi,
                        "populationSize": populationSize,
                    }

                    samples = dowellStratifiedSampling(stratifiedSamplingInput)
                    id = get_event_id()  # Make sure you have a function for this
                    response = {"event_id": id["event_id"], "samples": samples["sampleUnits"]}

                    if result == "Table":
                        return render(request, "result.html", {"response": response})
                    return JsonResponse(response, safe=False)

                except Exception as e:
                    return JsonResponse({"error": str(e)})
            return JsonResponse({"error": "Invalid request method."})
        else:
            return JsonResponse({
                "success": False,
                "message": data_count['message'],
                "credits": data_count['total_credits']
            })
    else:
        return JsonResponse({
            "success": False,
            "message": data_count['message']
        })


# from django.core.files.storage import default_storage


# @csrf_exempt
# @api_view(["POST"])
# def dowell_search(request):
#     if request.method == "POST":
#         payload = request.data
#         print("payload", payload)
#         data_type = payload.get("data_type")
#         if data_type == "api":
#             search_count = int(payload.get("search_count", 0))
#             search_criteria = []
#             manual_data = None
#             user_field = payload.get("user_field", {})

#             for i in range(search_count):
#                 key = payload.get(f"key{i}", "")
#                 value = payload.get(f"value{i}", "")
#                 search_criteria.append((key, value))

#             sample_values = dowell_purposive_sampling(
#                 search_criteria, user_field, manual_data
#             )
#             return Response(sample_values)
#         elif data_type == "upload":
#             print("upload data")
#             search_count = int(payload.get("search_count", 0))
#             uploaded_data = request.FILES.get("_file")
#             user_field = {
#                 "cluster": "license",
#                 "database": "license",
#                 "collection": "licenses",
#                 "document": "licenses",
#                 "team_member_ID": "689044433",
#                 "function_ID": "ABCDE",
#                 "command": "fetch",
#                 "field": {},
#                 "update_field": None,
#                 "platform": "bangalore",
#             }
#             search_criteria = []
#             manual_data = None

#             for i in range(search_count):
#                 key = payload.get(f"key{i}", "")
#                 value = payload.get(f"value{i}", "")
#                 search_criteria.append((key, value))

#             if uploaded_data:
#                 print("uploaded_data", uploaded_data)
#                 file_path = default_storage.save(
#                     uploaded_data.name, uploaded_data
#                 )  # Save the uploaded file
#                 try:
#                     with default_storage.open(file_path, "r") as file:
#                         json_data = json.load(file)
#                         manual_data = json_data
#                         sample_values = dowell_purposive_sampling(
#                             search_criteria, user_field, manual_data
#                         )
#                         return Response(sample_values)
#                 finally:
#                     os.remove(file_path)
#         else:
#             return Response({"error": "Invalid data type select api or upload"})
#     else:
#         return Response({"error": "Invalid request method."})


# @csrf_exempt
# def search(request):
#     return render(request, "search_function.html")


def sampling_input(request, api_key):
    validate_api_count = processApikey(api_key)
    data_count = json.loads(validate_api_count)
    if data_count['success']:
        if data_count['total_credits'] >= 0:
            return render(request, "sampling_inputs.html")
        else:
            return JsonResponse({
                "success": False,
                "message": data_count['message'],
                "credits": data_count['total_credits']
            })
    else:
        return JsonResponse({
            "success": False,
            "message": data_count['message']
        })


# def stratified_sampling_input(request):
#     return render(request, "stratified_sampling_input.html")


# def systematic_sampling_input(request):
#     return render(request, "systematic_sampling_input.html")


# def simple_random_sampling_input(request):
#     return render(request, "simple_random_sampling_input.html")


# def cluster_sampling_input(request):
#     return render(request, "cluster_sampling_input.html")


# def purposive_sampling_input(request):
#     return render(request, "purposive_sampling_input.html")


"""
Types of sampling
1. Stratified Random Sampling
Request
{

}

Response
{

}

2. Systematic Sampling
Request
{

}

Response
{

}

3. Purposive Sampling
Request
{

}

Response
{

}

4. Cluster
Request
{

}

Response
{

}

"""
