#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author : D4RKSH4D0WS
# Rikod boleh. Tapi jangan hapus author ya kampank
import requests,time,os,random,sys
G0 = "\033[0;32m"
G1 = "\033[1;32m"
C0 = "\033[0;36m"
C1 = "\033[1;36m"
P0 = "\033[0;35m"
P1 = "\033[1;35m"
W0 = "\033[0;37m"
W1 = "\033[1;37m"
B0 = "\033[0;34m"
B1 = "\033[1;34m"
R0 = "\033[0;31m"
R1 = "\033[1;31m"
Y1 = "\033[1;33m"
Y0 = "\033[0;33m"
BG = "\033[1;97;41m"
RE = "\033[0m"
def ketik(teks):
	for i in teks + "\n":
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(0.001)
def logo():
	os.system('clear')
	ketik("""
%s _____ %s_           _      %s__    %s_     _
%s|   __%s| |_ ___ ___| |_   %s|  |  %s|_|___| |_
%s|__   %s|   | . |  _|  _|  %s|  |__%s| |   | '_|
%s|_____%s|_|_|___|_| |_|    %s|_____%s|_|_|_|_,_|
"""%(G1,W1,G1,W1,G1,W1,G1,W1,G1,W1,G1,W1,G1,W1,G1,W1,))
def main():
	try:
		os.system('git pull')
		logo()
		url = raw_input('\033[1;32m[\033[1;33m?\033[1;32m]\033[0;37m Masukkan URL: ')
		if url == '':
			print('%s[%s!%s] %sJangan kosong cok'%(W1,R1,W1,W0))
			time.sleep(0.8)
			main()
		ua = requests.get('https://pastebin.com/raw/QckwZTMc').text.split('\n')
		acak = random.choice(ua)
		r=requests.get('https://is.gd/create.php?format=simple&url='+url,headers={"user-agent": "{acak}"})
		print "\033[1;32m[\033[1;33m√\033[1;32m] \033[0;37mResult : ",r.text
		print ("\033[1;32m[\033[1;33m!\033[1;32m] \033[0;37mPilih cok\n   \033[1;37m[\033[1;32m1\033[1;37m] \033[0;37mKunjungi link hasil shorten\n   \033[1;37m[\033[1;32m2\033[1;37m] \033[0;37mShorten lagi\n   \033[1;37m[\033[1;31m0\033[1;37m] \033[0;37mExit")
		y=raw_input("\033[1;32m[\033[1;33m?\033[1;32m] \033[0;37mPilih > ")
		if y == '1':
			os.system('xdg-open '+r.text)
		if y == '2':
			main()
		if y == '0':
			exit("%s[%sx%s] %sExiting program"%(W1,R1,W1,W0))
		else:
			exit("%s[%sx%s] %sExiting program"%(W1,R1,W1,W0))
	except requests.exceptions.ConnectionError:
		exit("%s[%sx%s] %sTidak ada koneksi"%(W1,R1,W1,W0))
if __name__=='__main__':
	main()
