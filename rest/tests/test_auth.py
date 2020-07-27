import requests
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

class OAuthTest(APITestCase):

	def testLoginAdmin(self):

		url = URL+"/rest/oauth/token/"
		data = {"grant_type":"password",
				"username":adminUser,
				"password":adminPass}
		auth = HTTPBasicAuth(cId,cS)

		response = requests.post(url, data=data, auth=auth)

		self.assertEqual(response.status_code,200)

	def testLoginUser(self):

		url = URL+"/rest/oauth/token/"
		data = {"grant_type":"password",
				"username":normalUser,
				"password":normalPass}
		auth = HTTPBasicAuth(cId,cS)

		response = requests.post(url, data=data, auth=auth)

		self.assertEqual(response.status_code,200)

	def testBadKeys(self):

		url = URL+"/rest/oauth/token/"
		data = {"grant_type":"password",
				"username":normalUser,
				"password":normalPass}
		auth = HTTPBasicAuth(cId+"X",cS+"X")

		response = requests.post(url, data=data, auth=auth)

		self.assertEqual(response.status_code,401)

	def testBadUser(self):

		url = URL+"/rest/oauth/token/"
		data = {"grant_type":"password",
				"username":normalUser+"X",
				"password":normalPass}
		auth = HTTPBasicAuth(cId,cS)

		response = requests.post(url, data=data, auth=auth)

		self.assertEqual(response.status_code,400)

	def testWrongPass(self):

		url = URL+"/rest/oauth/token/"
		data = {"grant_type":"password",
				"username":normalUser,
				"password":normalPass+"X"}
		auth = HTTPBasicAuth(cId,cS)

		response = requests.post(url, data=data, auth=auth)

		self.assertEqual(response.status_code,400)

