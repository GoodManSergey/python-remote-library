from Examples.server.rm_class import Calculator
from remote.remote_server import RemoteServer

if __name__ == '__main__':
    cl = Calculator()
    server = RemoteServer("0.0.0.0", 8080, cl)

    server.serve_forever()
