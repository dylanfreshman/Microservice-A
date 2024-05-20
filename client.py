import zmq
# ZMQ is the module used for interacting between apps.

context = zmq.Context()
# The context object is required to be made for all apps.
# It is a container that holds all created sockets in your process.

print("Connecting to Program server...")
socket = context.socket(zmq.REQ)
# This creates a new socket within the context with REQ that creates it
# as a Request socket. It sends requests and waits to receive a reply.
socket.connect("tcp://localhost:5555")
# This indicates the connection being made, meaning it will connect using
# the TCP protocol to the local machine on port 5555.

"""
Define all functions above the main in order to ensure
they interact properly.

def [your_function]():
"""

if __name__ == "__main__":

    while True:
        socket.send_string("Hi server")
        response = socket.recv().decode('utf-8')

        print(response)

    #   These are other options for sending different data to the server.
    #   socket.send_pyobj(obj)
    #   socket.send()


