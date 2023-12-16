def XUcrypt(XEcryptString):
    XEcryptValues = XEcryptString[1:].split(".")  # remove first "." character and put numbers into array
    XEcryptChars = []  # create array for encrypted characters
    modeMap = {}  # create map of array occurrences
    maxCount = 1  # create count var for tracking highest
    mode = None  # create mode var to keep track of which is the highest occurring character
    decoded = ""  # create decoded var for the decoded string

    """ loop adds sum of each group of three numbers to array and creates a map of the values
     and the number of times they occur to calculate the mode-average """
    for i in range(len(XEcryptValues) // 3):
        j = sum(int(XEcryptValues[k + 3 * i]) for k in range(3))
        XEcryptChars.append(j)
        if modeMap.get(j) is None:
            modeMap[j] = 1
        else:
            modeMap[j] += 1
            if modeMap[j] > maxCount:
                maxCount = modeMap[j]
                mode = j

    key = mode - 32  # the key is the number of the mode common encrypted character minus the ASCII code for a space

    for char in XEcryptChars:
        decoded += chr(char - key)  # for every array entry, type the decoded ASCII character

    return decoded

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, "r") as file:
            encrypted_input = file.read().strip()

        decrypted_output = XUcrypt(encrypted_input)

        print("Decrypted Output:", decrypted_output)

    except FileNotFoundError:
        print("Error: File not found")
        sys.exit(1)
