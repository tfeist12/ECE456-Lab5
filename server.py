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
    ip, port, buffSize = "0.0.0.0", 25010, 1024

    # Parse all command line inputs, test them, then read data
    testArgLength()
    filename = str(sys.argv[1])

    # Perform TCP socket programming for server side
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sInfo = (ip, port)
    sock.bind(sInfo)

    print("Waiting for packets from client file\n")
    sock.listen(1) # 1 = number of sockets
    data = []
    while True:
        connection, client_address = sock.accept()
        try:
            while True:
                message = connection.recv(buffSize)
                messageStr = str(message)[2:][:len(message)]
                if len(message) != 0:
                    print("Received: \"{message}\"".format(message=messageStr))
                    data.append(message)
                    connection.send(bytes("OK", 'utf-8'))
                else:
                    print("Client closed connection")
                    break
        finally:
            connection.close()
            break

    # Confirm user wants to receive the file
    print("\nDo you want to receive this file?")
    while True:
        print("Type y for yes and n for no: ")
        resp = input()
        resp = resp.lower()
        if resp == "y":
            print("\nReceiving the file, it will be saved as " + filename)
            break
        elif resp == "n":
            print("Response was no, Exiting!")
            sys.exit()
        else:
            print("Invalid response. Try again")

    # Save the file to local machine
    file = open(filename, "wb")
    for a in range(0, len(data)):
        file.write(data[a])
    file.close()





