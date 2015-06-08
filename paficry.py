#!/usr/bin/python

import sys
try:
    from Crypto.Cipher import AES
except ImportError:
    print 'Install PyCrypto'
 
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
		

def __main__(mode, input_file, output_file):
		
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
 
#start program

if __name__ == '__main__':
	if len(sys.argv) == 4:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print "Usage: python %s (-e or -d) input_file output_file" % sys.argv[0]

	



