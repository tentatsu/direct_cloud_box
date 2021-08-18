import urllib.request,time,math
import requests
import json, datetime
import logging
import os


domain = 'https://api.directcloud.jp'

class directCloudBox:
    access_token_object = {}
    def __init__(self, service, service_key, code, id, password):
        self.service = service
        self.service_key = service_key
        self.code = code
        self.id = id
        self.password = password
        param = {
            "service": service,
            "service_key": service_key,
            "code": code,
            "id": id,
            "password": password,
        }
        self.access_token_object = self.__post("/openapi/jauth/token", param)

    def tokenExpire(self):
        param = {
            "service": self.service,
            "service_key": self.service_key,
            "access_token": self.__getAccessToken()
        }
        self.access_token_object = self.__post("/openapi/jauth/tokenExpire", param)

    def folderGet(self, node):
        endpoint = "/openapp/v1/folders/index/{}".format(node)
        return self.__get(endpoint)

    def folderCreate(self, name, node):
        endpoint = "/openapp/v1/folders/create/{}".format(node)
        param = {"name": name}
        return self.__post(endpoint, param)


    def __getAccessToken(self):
        if "access_token" in self.access_token_object:
            return self.access_token_object["access_token"]
        return None

    def __get(self, endpoint):
        print("get {} start".format(endpoint))
        req_header = {}
        if self.__getAccessToken():
            req_header["access_token"] = self.__getAccessToken()
        
        return requests.get(url=domain + endpoint, headers=req_header).json()
 
    def __post(self, endpoint, param):
        print("post {} start".format(endpoint))
        req_header = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        if self.__getAccessToken():
            req_header["access_token"] = self.__getAccessToken()
        post_form_data = urllib.parse.urlencode(param)
        req = requests.post(domain + endpoint, headers=req_header, data=post_form_data.encode()).json()

        print(req)
        return req
        # print(req.get_header("access_token"))
        # print(req.get_header("Content-Type"))

        # try:
        #     with urllib.request.urlopen(req) as response:
        #         body = json.loads(response.read().decode('utf-8'))
        #         headers = response.getheaders()
        #         status = response.getcode()
        #         print(body)
        #         return body
        # except urllib.error.URLError as e:
        #     print(e.reason)
        #     print(e)


        








