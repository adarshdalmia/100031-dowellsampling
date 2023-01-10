from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
import json
from API.functions.stratifiedSampling import dowellStratifiedSampling

@csrf_exempt
def stratifiedSamplingAPI(request):
    if (request.method=="POST"):
        request_data=json.loads(request.body)
        Name = request_data['name']
        LastName= request_data['lastname']
        fullName = f"Your name is {Name} {LastName}"
        return JsonResponse ({"Answer":fullName})
    else:
        return HttpResponse("Method Not Allowed")   

'''
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

'''