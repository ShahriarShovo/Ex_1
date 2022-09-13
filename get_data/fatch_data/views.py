from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests



@api_view(['POST'])
def login_view(request):

    headers={
        "Accept": "application/json",
        "Content-Type" : "application/json"
    }

    login_api = "http://127.0.0.1:8000/account/login/"
    username=request.POST.get('username')
    password=request.POST.get('password')
    data={
        "username": username,
        "password": password
       
    }

    print(data)
    
    response = requests.post(login_api, json=data , headers=headers)
    print("Response", response)
    #print(response.json()['access'])
    
    return Response(data=response.json())





# @api_view(['POST'])
# def login_view_token(request,username,password):

#     headers={
#         "Accept": "application/json",
#         "Content-Type" : "application/json"
#     }

#     login_api = "http://127.0.0.1:8000/account/login/"
#     username=username
#     password=password
#     data={
#         "username": username,
#         "password": password
       
#     }

#     print(data)
    
#     response = requests.post(login_api, json=data , headers=headers)
#     print("Response", response)
#     print(response.json())
#     access_token=response.json()['token']['access']
#     return access_token






# # Get  cities
@api_view(['GET'])
def get_profile(request):

    # login_view(request,'Shovo','shovo')
    # if login_view:
    #     return Response({'messg':'success'})
    # else:
    #     return Response({'messg':'Not success'})

    # pathao_accesstoken_api='https://oyster-app-7ulvb.ondigitalocean.app/courier/pathao/'
    # pathao_api_accesstoken_response=requests.post(pathao_accesstoken_api)
    # pathao_api_accesstoken_response_json=pathao_api_accesstoken_response.json()
    

    # headers={
    #     "Accept": "application/json",
    #     "Content-Type" : "application/json",
    #     "Authorization" : "Bearer {}".format(pathao_api_accesstoken_response_json['access_token']),
    # }

    profile_api = "http://127.0.0.1:8000/account/profile/"
    response = requests.get(profile_api)
    return Response(data=response.json())