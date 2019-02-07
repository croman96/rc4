import fileinput
import math

# Receive key and return a list with the ASCII value of each char.
def convertKey(key):
    lst = []
    for c in key:
        lst.append(ord(c))
    return lst

# Generate key-scheduling algorithm.
def KSA(key):
    keylength = len(key)
    S = range(256)
    j = 0
    # Straight outta algorithm.
    for i in range(256):
        j = (j + S[i] + key[i % keylength]) % 256
        S[i], S[j] = S[j], S[i]
    return S

# Receive KSA and generate K list containing the keystream.
def PRGA(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        yield K

# Use KSA and PRGA to generate keystream for RC4.
def RC4(key):
    S = KSA(key)
    return PRGA(S)

# Receive keystream and plaintext. Encrypt plaintext using keystream.
def encrypt(keystream, plaintext):
    lst = []
    # Iterate over plain text message char by char.
    for c in plaintext:
        # Append the value formatted as hexadecimal.
        lst.append("%02X" % (ord(c) ^ keystream.next()))
    # Convert list to string.
    return ''.join(lst)

def main():
    instructions = []
    for line in fileinput.input():
        try:
            instructions.append(line[:-1])
        except:
            break
    # Format the key.
    key = convertKey(instructions[0])
    # Generate keystream given key.
    keystream = RC4(key)
    # Encrypt message.
    encrypted = encrypt(keystream, instructions[1])
    # Print output.
    print(encrypted)

if __name__ == '__main__':
    main()
