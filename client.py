import sys
import helper
import L1


# Test length of command line args for client
def testArgLength():
    if len(sys.argv) != 3:
        print("Must use 2 command line arguments for client, Exiting!")
        sys.exit()


# Main method
if __name__ == '__main__':
    # Parse all command line inputs, test them, then read data
    testArgLength()
    sIP, inFile = str(sys.argv[1]), str(sys.argv[2])
