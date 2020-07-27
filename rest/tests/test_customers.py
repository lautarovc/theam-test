import requests
import json
from urllib.request import urlopen
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

class CustomersTest(APITestCase):

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
		url = URL+"/rest/customers/"
		headers = {'Content-Type':'application/json', 'Authorization': 'Bearer '+self.userToken+"X"}

		response = requests.get(url, headers=headers)

		self.assertEqual(response.status_code,401)		

	def testAdmin(self):
		url = URL+"/rest/customers/"
		headers = {'Content-Type':'application/json', 'Authorization': 'Bearer '+self.adminToken}

		response = requests.get(url, headers=headers)

		self.assertEqual(response.status_code,200)

	def testListCustomers(self):
		url = URL+"/rest/customers/"
		headers = {'Content-Type':'application/json', 'Authorization': 'Bearer '+self.userToken}

		response = requests.get(url, headers=headers)

		self.assertEqual(response.status_code,200)

	def testCreateIncompleteCustomer(self):

		url = URL+"/rest/customers/"
		headers = {'Content-Type':'application/json', 'Authorization': 'Bearer '+self.userToken}
		data = json.dumps({"id":"1234567", "name":"name1"})

		response = requests.post(url, data=data, headers=headers)

		self.assertEqual(response.status_code,400)

	
	def testCreateDeleteCustomer(self):

		# Upload data and photo, Content-Type deleted to allow requests can create the corresponding boundaries
		url = URL+"/rest/customers/"
		headers = {'Authorization': 'Bearer '+self.userToken}
		data = {"id":"1234567", "name":"name1", "surname":"name1"}
		photo = {'photo': open('rest/tests/test.png', 'rb')}

		response = requests.post(url, data=data, files=photo, headers=headers)

		self.assertEqual(response.status_code,201)

		# Delete the created customer
		newId = json.loads(response.content)["id"]
		url += str(newId) + "/"

		response = requests.delete(url, headers=headers)

		self.assertEqual(response.status_code, 204)
	

	def testGetCustomer(self):

		url = URL+"/rest/customers/12345/"
		headers = {'Content-Type':'application/json', 'Authorization': 'Bearer '+self.userToken}

		response = requests.get(url, headers=headers)

		self.assertEqual(response.status_code,200)

	def testUpdateCustomer(self):

		# Upload photo, Content-Type deleted to allow requests can create the corresponding boundaries
		url = URL+"/rest/customers/12345/"
		headers = {'Authorization': 'Bearer '+self.userToken}
		data = {'photo': open('rest/tests/test.png', 'rb')}

		response = requests.patch(url, files=data, headers=headers)
		
		photoUrl = json.loads(response.content)["photo"]
		print("PHOTO URL: " + photoUrl)

		self.assertEqual(response.status_code,200)

	def testEditCustomer(self):

		url = URL+"/rest/customers/12345/"
		headers = {'Content-Type':'application/json', 'Authorization': 'Bearer '+self.userToken}
		data = json.dumps({"id":"12345", "name":"name2", "surname":"name2"})

		response = requests.put(url, data=data, headers=headers)

		self.assertEqual(response.status_code,200)