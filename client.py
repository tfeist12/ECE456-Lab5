import os
import sys
import math
import socket
import helper
import L1


# Test length of command line args for client
def testArgLength():
    if len(sys.argv) != 3:
        print("Must use 2 command line arguments for client, Exiting!")
        sys.exit()


# Test validity of arguments read in
def testArgs(sIP, inFile):
    sIP = helper.testIP(sIP)
    file = L1.testFile(inFile)
    return [sIP, file]


# Main method
if __name__ == '__main__':

    # Set port and buffer size
    port, buffSize = 12345, 1024

    # Parse all command line inputs, test them, then read data
    testArgLength()
    sIP, inFile = str(sys.argv[1]), str(sys.argv[2])
    sIP, file = testArgs(sIP, inFile)

    # Get file size and number of packets which need to be sent
    dirPath = os.getcwd()
    filePath = dirPath + "/" + inFile
    size = os.path.getsize(filePath)
    iterNum = math.ceil(size / buffSize)
    print(size)

    # Read 1024 bytes at a time from the file
    data = []
    for a in range(0, iterNum):
        data.append(file.read(buffSize))
    file.close()

    # Perform TCP socket programming for client side
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sInfo = (str(sIP), port)
    sock.connect(sInfo)

    try:
        print("Connection established")
        for a in range(0, len(data)):
            print('sending "{message}"'.format(message=data[a]))
            sock.send(data[a])

            while True:
                servResp = sock.recv(buffSize)
                print('received "{data}"'.format(data=servResp))
                break
    finally:
        print('Closing socket')
        sock.close()


