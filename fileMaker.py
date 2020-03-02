# Main method
if __name__ == '__main__':
    filename = "testFile.txt"
    size = 2049
    f0 = open(filename, "w")
    count = 0
    while count < size:
        f0.write("a")
        count += 1
    f0.close()