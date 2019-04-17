from remote.status_codes import StatusCode


class RemoteClass(object):

    def __init__(self, cl):
        self.__rm_class = cl

    @staticmethod
    def __get_resp(status, data):
        resp = dict()
        resp["status"] = status
        resp["data"] = data

        return resp

    def call_method(self, method_name, *args, **kwargs):
        try:
            method = self.__rm_class.__class__.__dict__[method_name]
        except Exception as e:
            return RemoteClass.__get_resp(StatusCode.ERROR, repr(e))

        if isinstance(method, staticmethod):
            try:
               resp = method.__func__(*args, **kwargs)
               return RemoteClass.__get_resp(StatusCode.OK, resp)
            except Exception as e:
                return RemoteClass.__get_resp(StatusCode.ERROR, repr(e))
        else:
            try:
                resp = method(self.__rm_class, *args, **kwargs)
                return RemoteClass.__get_resp(StatusCode.OK, resp)
            except Exception as e:
                return RemoteClass.__get_resp(StatusCode.ERROR, repr(e))
