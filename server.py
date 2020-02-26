import sys
import helper
import L1


# Test length of command line args for server
def testArgLength():
    if len(sys.argv) != 2:
        print("Must use 1 command line argument for server, Exiting!")
        sys.exit()


# Main method
if __name__ == '__main__':

    # Parse all command line inputs, test them, then read data
    testArgLength()
    filename = str(sys.argv[1])