#!python3
# Created by MDE 01.31/2018
# Command line python to decrypt encrypt using ascii characters
# CC3 not verified


import os, sys, getopt

global c

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

def decrypt(text,intkey,shift,c):
    decryptedtext = ""
    for i in range(len(text)):
        decryptedtext = decryptedtext + antivinegere(text[i],intkey,i,shift,c)
    return decryptedtext
        
def encrypt(text,intkey,shift,c):
    encryptedtext = ""
    for i in range(len(text)):
        encryptedtext = encryptedtext + vinegere(text[i],intkey,i,shift,c)
    return encryptedtext

def writefile(outputfile,content):
    f = open(outputfile,"w+")
    f.write(content)
    f.close()
    
def val(key,c):
    intkey = []
    for i in range(len(key)):
        for z in range(c):
            if key[i] == chr(z):
                intkey.append(z)
    return intkey

def vinegere(l,intkey,count,shift,c):
    for i in range(c): # get numeric value of character
        if l == chr(i):
            x = i
    count = count + len(intkey) # so no 0/x 
    remain = count % len(intkey) # incriments through key based on len
    z = x + intkey[remain] + shift
    if z >= c:
        z = z - c #if out of range keep in range
    print("char val " + str(x),"r is " + str(remain),"mod num " + str(z),"zs char " + chr(z))
    return chr(z)

def antivinegere(l,intkey,count,shift,c):
    for i in range(c): # get numeric value of character
        if l == chr(i):
            x = i
    count = count + len(intkey) # avoid 0/x erros
    remain = count % len(intkey) # incriments through key based on len
    z = x - intkey[remain] - shift
    if z < 0:
        z = z + c # if out of range keep in range
    return chr(z)

def main(argv):
    c = 128
    key = ''
    inputfile = ''
    outputfile = ''
    keyfile = ''
    shift = False
    manualKey = True
    manualText = True
    de = False
    en = False
    try:
        opts, args = getopt.getopt(argv,"edhto:i:s:k:c:",["ofile=","ifile=","shift=","keyfile=","charsize="])
    except getopt.GetoptError:
        print('mde128.py -i <inputfile> -o <outputfile> -e/-d (encrypte/decrypt)')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('#################################################################')
            print('                    MDE128.py Help File')
            print('#################################################################')
            print('    -i <filename> specify input file as source text to decypt/encrypt')
            print('    -o <filename> specify outputfile for the result')
            print('            note: text does not work right if in clipboard use output file')
            print('    -e used to specify to encrypt')
            print('    -d used to specify to decrypt')
            print('    -s <int> used to specify a shift ammount in the cypher')
            print('            note: integer values over 128 have not been tested')
            print('    -k <filename> used to specify key file')
            print('            if no k parameter given it will ask you to type a key')
            print('    -c used to specify character range 128 is default')
            print('            note some characters get an error over 128 if saving to file')
            print('            which is hard coded so it will probably happen')
            print()
            print()
            print('    Examples of use:')
            print('        mde128.py -i random.txt -o output.txt -e')
            print('        mde128.py -i raw.txt -o result.txt -d -k key.txt -s 10')
            print('        mde128.py -i lorum.txt -o scratch.txt -e -c 256')
            sys.exit(1)
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-s", "--shift"):
            shift = int(arg)
        elif opt in ("-k", "--keyfile"):
            keyfile = arg
        elif opt in ("-c", "--charsize"):
            c = int(arg)
        elif opt == '-e':
            en = True
        elif opt == '-d':
            de = True

    if de == False and en == False:
        print("please use -e encrypt or -d decrypt")
        sys.exit(2)
    if keyfile == '':
        print("please input the encoder phrase")
        key = input()
    else:
        key = keyfile

    if not shift:
        print("enter an interger if you wish to shift the cypher")
        try:
            shift = int(input())
        except:
            print("please use an integer to shift the cypher")
            sys.exit(2)

    # Get the ASCII numeric values of the key
    intkey = val(key,c)

    # Get the text to be encoded / decoded
    textFile = open(inputfile)
    text = textFile.read()
    #text = input()

    if en == True:
        # Encrypt Text
        content = encrypt(text,intkey,shift,c)
    elif de == True:    
        # Decrypt Text
        content = decrypt(text,intkey,shift,c)



    #Need to define content of what to write
    writefile(outputfile,content)

    print(content)
        
if __name__ == "__main__":
   main(sys.argv[1:])
    
