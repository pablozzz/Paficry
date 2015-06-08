#!/usr/bin/python

import sys
from Crypto.Cipher import AES

#inicialize key and aes mode

key = '11111111111111111111111111111111'
c_mode = AES.MODE_ECB
encryptor = AES.new(key, c_mode)
blocksize = 16

def encrypt(text, outfile):
# encrypt function
	count = 0
	block = ""
	for symbol in text:
		count += 1
		block = block + symbol
		if count == blocksize:
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
                if count == blocksize:
                        plainblock = encryptor.decrypt(block)
                        output_file = open(outfile, "ab")
                        output_file.write(plainblock)
                        output_file.close()
                        block = ""
                        count = 0
        print "done"
		

#start program

if len(sys.argv) != 4:
	print "Usage: python paficry.py (-e or -d) input_file output_file"
else: 

#inicialize files

	mode = sys.argv[1]
	input_file_name = sys.argv[2]
	output_file_name = sys.argv[3]
	
	input_file = open(input_file_name, "rb")
	text = input_file.read()
	input_file.close()
 
	if mode == '-e':
		print "start encryption"
		encrypt(text, output_file_name)
	elif mode == '-d':
		print "start decryption"
		decrypt(text, output_file_name)
	else: 
		print "-e : encription mode or -d : decryption mode"
 



