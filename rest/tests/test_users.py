import requests
import json
from requests.auth import HTTPBasicAuth
from theamTest.settings import TEST_INFO
from rest_framework.test import APITestCase

#NOTE: oauth2_django_toolkit has direct unit tests limitations. Tests will be done to the API functions published in URL.
#NOTE2: Client keys are manually taken from URL/rest/oauth/applications/ please refer to those.
#NOTE3: adminUser and normalUser information is also taken directly from URL/admin/.
#NOTE4: Either have environment variable TEST_INFO or fill the variables below to perform tests.

cId = TEST_INFO.get("cId")
cS = TEST_INFO.get("cS")

adminUser = TEST_INFO.get("adminUser")
adminPass = TEST_INFO.get("adminPass")

normalUser = TEST_INFO.get("normalUser")
normalPass = TEST_INFO.get("normalPass")

URL = TEST_INFO.get("URL")


# Create your tests here.

class UsersTest(APITestCase):

	@classmethod
	def setUpTestData(cls):
		url = URL+"/rest/oauth/token/"
		data = {"grant_type":"password",
				"username":adminUser,
				"password":adminPass}
		auth = HTTPBasicAuth(cId,cS)

		# Get admin Access Token
		response = requests.post(url, data=data, auth=auth)
		response = json.loads(response.content)
		cls.adminToken = response['access_token']

		# Get normal user Access Token
		data["username"] = normalUser
		data["password"] = normalPass	

		response = requests.post(url, data=data, auth=auth)
		response = json.loads(response.content)
		cls.userToken = response['access_token']

	def testWrongKey(self):
		url = URL+"/rest/users/"
		headers = {'Content-Type':'application/json', 'Authorization': 'Bearer '+self.adminToken+"X"}

		response = requests.get(url, headers=headers)

		self.assertEqual(response.status_code,401)		
		
	def testNotAdmin(self):
		url = URL+"/rest/users/"
		headers = {'Content-Type':'application/json', 'Authorization': 'Bearer '+self.userToken}

		response = requests.get(url, headers=headers)

		self.assertEqual(response.status_code,403)

	def testListUsers(self):
		url = URL+"/rest/users/"
		headers = {'Content-Type':'application/json', 'Authorization': 'Bearer '+self.adminToken}

		response = requests.get(url, headers=headers)

		self.assertEqual(response.status_code,200)

	def testCreateDeleteUser(self):

		url = URL+"/rest/users/"
		headers = {'Content-Type':'application/json', 'Authorization': 'Bearer '+self.adminToken}
		data = json.dumps({"username":"user2", "first_name":"", "last_name":"", "email":"", "is_staff":False, "password":"12345"})

		response = requests.post(url, data=data, headers=headers)

		self.assertEqual(response.status_code,201)

		# Delete the created user
		newId = json.loads(response.content)["id"]
		url += str(newId) + "/"

		response = requests.delete(url, headers=headers)

		self.assertEqual(response.status_code, 204)

	def testGetUser(self):

		url = URL+"/rest/users/2/"
		headers = {'Content-Type':'application/json', 'Authorization': 'Bearer '+self.adminToken}

		response = requests.get(url, headers=headers)

		self.assertEqual(response.status_code,200)

	def testUpdateUserToAdmin(self):

		url = URL+"/rest/users/2/"
		headers = {'Content-Type':'application/json', 'Authorization': 'Bearer '+self.adminToken}
		data = json.dumps({"is_staff":True})

		response = requests.patch(url, data=data, headers=headers)

		self.assertEqual(response.status_code,200)

		# Test to see if it works as admin by listing users
		url = URL+"/rest/users/"
		response = requests.get(url, headers=headers)
		self.assertEqual(response.status_code,200)

		# Reverse update
		url = URL+"/rest/users/2/"
		data = json.dumps({"is_staff":False})
		response = requests.patch(url, data=data, headers=headers)
		self.assertEqual(response.status_code,200)

	def testEditUser(self):

		url = URL+"/rest/users/2/"
		headers = {'Content-Type':'application/json', 'Authorization': 'Bearer '+self.adminToken}
		data = json.dumps({"username":"user1", "first_name":"user1", "last_name":"user1", "email":"", "is_staff":False, "password":"12345"})

		response = requests.put(url, data=data, headers=headers)

		self.assertEqual(response.status_code,200)