import pytest
import requests
import json
# from data import *




# Step 1:  Create a new object and validate its response code and Store the id  (POST API)
#
# Step 2:  Get the object details using id and validate (GET API)
#
# Step 3:update any details for the object created above and validate if it is updated (PUT)
#
# Step 4: delete the created object and validate if its deleted
id = ""

def test_add_obj(request_header,my_baseUrl):
    global id
    Base_URL = my_baseUrl
    header = request_header
    add_obj = Base_URL + "objects"
    file = open("../data/add_obj.json", 'r')
    request_body = file.read()
    response = requests.post(url=add_obj,headers=header, data=request_body)
    data = response.json()
    id = data['id']
    assert response.status_code == 200 , "status code not match"


@pytest.mark.sanity
def test_get_data(my_baseUrl):
    global id
    Base_URl = my_baseUrl
    url = Base_URl+ "objects/" + id
    response = requests.get(url= url)
    data = response.json()
    get_id = data['id']
    assert get_id == id, "object id not match"

def test_update_obj(request_header,my_baseUrl):
    global id
    Base_URl = my_baseUrl
    header = request_header
    url = Base_URl + "objects/" + id
    file = open("../data/update_obj.json", 'r')
    # header = {'accept': 'application/json',
    #           'Content-Type': 'application/json'}
    request_body = file.read()
    response = requests.put(url=url,headers=header, data=request_body)
    data = response.json()
    assert response.status_code == 200, "status_code not match"
    assert data['data']['Hard disk size'] == "2 TB"

def test_del_obj(my_baseUrl):
    global id
    Base_URl = my_baseUrl
    url = Base_URl + "objects/" + id
    response = requests.delete(url = url)
    assert response.status_code == 200, "status_code not match"





