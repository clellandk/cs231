import hashlib
import binascii

def main():
    passwords = loadWords('wordfile.txt')
    encFile = open('pass1.txt','r')
    decFile = open('passwords1.txt','w')
    lines = [line.strip() for line in encFile]
    lines2 = []
    for line in lines:
        line2 = line.split(":")
        lines2.append(line2)
    findWords(passwords, lines2, decFile)
    
    
def loadWords(inpFile):
    words = [line.strip().lower() for line in open(inpFile)]
    return words

    
def findWords(words, lines, writeFile):
    for password in words:
        #password = 'moose'
        encodedPassword = password.encode('utf-8') # type=bytes

        md5 = hashlib.md5(encodedPassword)
        passwordHash = md5.digest() # type=bytes

        passwordHashAsHex = binascii.hexlify(passwordHash) # weirdly, still type=bytes

        final = passwordHashAsHex.decode('utf-8') # type=string
        for row in lines:
            if (row[1] == final):
                writeFile.write(row[0]+":"+password+"\n")

    
    
if __name__ == '__main__':
    main()