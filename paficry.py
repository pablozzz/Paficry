#!/usr/bin/python

import sys
from Crypto.Cipher import AES

#inicialize key and aes mode
key = '11111111111111111111111111111111'
c_mode = AES.MODE_ECB
encryptor = AES.new(key, c_mode)

#inicialize files

mode = sys.argv[1]
input_file_name = sys.argv[2]
output_file_name = sys.argv[3]

input_file = open(input_file_name, "rb")
text = input_file.read()
input_file.close()

def encrypt(text, outfile):
# encrypt function
	count = 0
	block = ""
	for symbol in text:
		count += 1
		block = block + symbol
		if count == 16:
			cipherblock = encryptor.encrypt(block)
			output_file = open(outfile, "ab")
			output_file.write(cipherblock)
			output_file.close()
			block = ""
			count = 0
	print "done"			

def decrypt(text, outfile):
# decrypt function
	count = 0
	block = ""
	for symbol in text:
		count += 1
        block = block + symbol
        if count == 16:
            plainblock = encryptor.decrypt(block)
            output_file = open(outfile, "ab")
            output_file.write(plainblock)
            output_file.close()
            block = ""
            count = 0
    print "done"
		

#start program

if mode == '-e':
	print "start encryption"
	encrypt(text, output_file_name)
elif mode == '-d':
	print "start decryption"
	decrypt(text, output_file_name)
 



