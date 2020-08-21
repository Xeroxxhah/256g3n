import hashlib


def c2hash(string):
    return hashlib.sha256(string.encode()).hexdigest()


def convert(ctpath, oufile):
        file = open(ctpath, 'r')
        ofile = open(oufile, 'a+')
        for clear in file:
                ciphertext = c2hash(clear)
                print(ciphertext)
                ofile.write(ciphertext+'\n')
        ofile.close()
        file.close()


def main():
    ctpath = input('Enter plain text file path: ')
    outfile = input('Enter output file path: ')
    convert(ctpath, outfile)


main()


