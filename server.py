from pip._vendor.distlib.compat import raw_input
import sys
import socket
import helper
import L1


# Test length of command line args for server
def testArgLength():
    if len(sys.argv) != 2:
        print("Must use 1 command line argument for server, Exiting!")
        sys.exit()


# Main method
if __name__ == '__main__':

    # Set ip, port, and buffer size
    ip, port, buffSize = socket.gethostname(), 12345, 1024

    # Parse all command line inputs, test them, then read data
    testArgLength()
    filename = str(sys.argv[1])

    # Perform TCP socket programming for server side
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sInfo = (ip, port)
    sock.bind(sInfo)

    sock.listen(1) # 1 = number of sockets
    while True:
        connection, client_address = sock.accept()
        try:
            while True:
                data = connection.recv(buffSize)
                print('message received: {data}'.format(data=data))
                connection.send(bytes("ok"))
        finally:
            connection.close()



