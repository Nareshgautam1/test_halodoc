import pytest
import requests

@pytest.fixture()
def request_header():
    header = {'accept': 'application/json',
     'Content-Type': 'application/json'}
    return header


# @pytest.fixture(sco)
# def add_obj(request_header):
#     add_obj = "https://api.restful-api.dev/objects"
#     header = {'accept': 'application/json',
#               'Content-Type': 'application/json'}
#     file = open("../data/add_obj.json", 'r')
#     request_body = file.read()
#     response = requests.post(url=add_obj,headers=header, data=request_body)
#     data = response.json()
#     id = data['id']
#     return id

@pytest.fixture()
def my_baseUrl():
    Base_URl = "https://api.restful-api.dev/"
    return Base_URl

