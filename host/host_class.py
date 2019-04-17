import requests


class Class(object):

    def __init__(self, host, port):
        self.__host = host
        self.__port = port
        self.__calling_method_name = None

    def __call__(self, *args, **kwargs):
        data = dict()
        data["method"] = self.__calling_method_name
        data["args"] = list(args)
        data["kwargs"] = kwargs

        url = "http://%s:%s/" % (self.__host, self.__port)

        resp = requests.post(url, json=data)

        resp_json = resp.json()
        if resp_json["status"] == "OK":
            return resp_json["data"]
        else:
            raise Exception(str(resp_json["data"]))

    def __getattr__(self, key):
        self.__calling_method_name = key
        return self.__call__
