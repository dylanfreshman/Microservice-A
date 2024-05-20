import time
import zmq

context = zmq.Context()
# The server is being set up as a reply socket, which waits for a request
# then cannot receive another request until it replies.
socket = context.socket(zmq.REP)
# Creating the server on the localhost.
socket.bind("tcp://*:5555")

"""
ENTER VARIABLES HERE
"""

# This is to keep the server running.
while True:
    message = socket.recv().decode('utf-8')
    print(f"Received Message: {message}")

    time.sleep(1)

    socket.send_string("Hello client!")

