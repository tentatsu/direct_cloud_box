import urllib.request,time,math
import requests
import json, datetime
import logging
import os
import mimetypes

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

    def folderRename(self, name, node):
        endpoint = "/openapp/v1/folders/rename/{}".format(node)
        param = {"name": name}
        return self.__post(endpoint, param)

    def folderDelete(self, node):
        endpoint = "/openapp/v1/folders/delete/{}".format(node)
        param = {}
        return self.__post(endpoint, param)


    def fileGet(self, node, sort = None, limit = None, offset = None):
        endpoint = "/openapp/v1/files/index/{}".format(node)
        param = {}
        if sort:
            param["sort"] = sort
        if limit:
            param["limit"] = limit
        if offset:
            param["offset"] = offset
        return self.__get(endpoint, param)

    def fileUpload(self, file_data, node):
        endpoint = "/openapp/v1/files/upload/{}".format(node)
        fileDataBinary = open(file_data, 'rb')
        param = {"Filedata": (file_data, fileDataBinary, mimetypes.guess_type(file_data)[0])}
        return self.__post(endpoint, {}, param)
    
    def fileRename(self, name, node, file_seq):
        endpoint = "/openapp/v1/files/rename/{}".format(node)
        param = {"name": name, "file_seq": file_seq}
        return self.__post(endpoint, param)

    def fileDownloadUrl(self, node, file_seq):
        endpoint = "/openapp/v1/files/download/{}".format(node)
        param = {"file_seq": file_seq, "flag_direct": "N"}
        return self.__post(endpoint, param)
    
    def fileDownloadBinary(self, node, file_seq):
        endpoint = "/openapp/v1/files/download/{}".format(node)
        param = {"file_seq": file_seq, "flag_direct": "N"}
        return self.__post(endpoint, param)

    def fileDelete(self, node, file_seq):
        endpoint = "/openapp/v1/files/delete/{}".format(node)
        param = {"file_seq": file_seq}
        return self.__post(endpoint, param)

    def fileSearch(self, node, keyword, sort = None, limit = None, offset = None):
        endpoint = "/openapp/v1/files/search/{}".format(node)
        param = {"keyword": keyword}
        if sort:
            param["sort"] = sort
        if limit:
            param["limit"] = limit
        if offset:
            param["offset"] = offset
        return self.__get(endpoint, param)

    def linkCreate(self, target_type, target_seq, view_option, expiration_date, limit_count, password, flag_readable, flag_writable):
        endpoint = "/openapp/v1/links/create"
        param = {
            "target_type": target_type,
            "target_seq": target_seq,
            }
        if view_option:
            param["view_option"] = view_option
        if expiration_date:
            param["expiration_date"] = expiration_date
        if limit_count:
            param["limit_count"] = limit_count
        if password:
            param["password"] = password
        if flag_readable:
            param["flag_readable"] = flag_readable
        if flag_writable:
            param["flag_writable"] = flag_writable
        return self.__post(endpoint, param)

    def fileViewer(self, file_seq):
        endpoint = "/openapp/v1/viewer/create"
        param = {"file_seq": file_seq}
        return self.__post(endpoint, param)


    def __getAccessToken(self):
        if "access_token" in self.access_token_object:
            return self.access_token_object["access_token"]
        return None

    def __get(self, endpoint, params = {}):
        req_header = {}
        if self.__getAccessToken():
            req_header["access_token"] = self.__getAccessToken()
        
        return requests.get(url=domain + endpoint, headers=req_header, params=params).json()
 
    def __post(self, endpoint, param, file = None):
        print("********* {} start".format(endpoint))
        req_header = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        if file:
            req_header = {}
        if self.__getAccessToken():
            req_header["access_token"] = self.__getAccessToken()
        post_form_data = urllib.parse.urlencode(param)
        req = requests.post(domain + endpoint, headers=req_header, data=post_form_data.encode(), files=file)
        return req.json()
        

