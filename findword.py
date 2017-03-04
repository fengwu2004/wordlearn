import zerorpc

class HelloRPC(object):
    def hello(self, name):
        return "Hello, yanli"

s = zerorpc.Server(HelloRPC())
s.bind("tcp://127.0.0.1:4242")
s.run()