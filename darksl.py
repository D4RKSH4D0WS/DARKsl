#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author D4RKSH4D0WS
# Belajar lah dari yg mudah 
# Rikod jangan hapus author ya anjenk !
import requests,time,os,random,sys,json
import subprocess as sp
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
def spin():
        try:
                L="\|/-"
                for q in range(10):
                        time.sleep(0.1)
                        sys.stdout.write("\r\033[1;32m[\033[1;33m"+L[q % len(L)]+"\033[1;32m]\033[0;37m Loading please wait...")
                        sys.stdout.flush()
        except:
                exit()
def logo():
	os.system('clear')
	ketik("""
%s _____ %s_           _      %s__    %s_     _
%s|   __%s| |_ ___ ___| |_   %s|  |  %s|_|___| |_
%s|__   %s|   | . |  _|  _|  %s|  |__%s| |   | '_|
%s|_____%s|_|_|___|_| |_|    %s|_____%s|_|_|_|_,_|
"""%(G1,W1,G1,W1,G1,W1,G1,W1,G1,W1,G1,W1,G1,W1,G1,W1))
def s1():
	try:
		logo()
		url = raw_input('\033[1;32m[\033[1;33m?\033[1;32m]\033[0;37m Masukkan URL: ')
		if url == '':
			print('%s[%s!%s] %sJangan kosong cok'%(W1,R1,W1,W0))
			time.sleep(0.8)
			s1()
		ua = requests.get('https://pastebin.com/raw/QckwZTMc').text.split('\n')
		acak = random.choice(ua)
		r=requests.get('https://is.gd/create.php?format=simple&url='+url,headers={"user-agent": "{acak}"})
		if 'valid' in r.text:
			print '%s[%s!%s] %sInput yg bener !'%(W1,R1,W1,W0)
			time.sleep(0.8)
			s1()
		print "\033[1;32m[\033[1;33m√\033[1;32m] \033[0;37mResult : ",r.text
		print ("\033[1;32m[\033[1;33m!\033[1;32m] \033[0;37mPilih cok\n   \033[1;37m[\033[1;32m1\033[1;37m] \033[0;37mKunjungi link hasil shorten\n   \033[1;37m[\033[1;32m2\033[1;37m] \033[0;37mShorten lagi\n   \033[1;37m[\033[1;32m3\033[1;37m] \033[0;37mBack\n   \033[1;37m[\033[1;31m0\033[1;37m] \033[0;37mExit")
		y=raw_input("\033[1;32m[\033[1;33m?\033[1;32m] \033[0;37mPilih > ")
		if y == '1':
			os.system('xdg-open '+r.text)
			main()
		elif y == '2':
			s1()
		elif y == '3':
			main()
		elif y == '0':
			exit("%s[%sx%s] %sExiting program"%(W1,R1,W1,W0))
		else:
			main()
	except requests.exceptions.ConnectionError:
		exit("%s[%sx%s] %sTidak ada koneksi"%(W1,R1,W1,W0))
def s2():
	try:
		logo()
		url = raw_input('\033[1;32m[\033[1;33m?\033[1;32m]\033[0;37m Masukkan URL: ')
		if url == '':
			print('%s[%s!%s] %sJangan kosong cok'%(W1,R1,W1,W0))
			time.sleep(0.8)
			s2()
		ua = requests.get('https://pastebin.com/raw/QckwZTMc').text.split('\n')
		acak = random.choice(ua)
		a=requests.post('https://rel.ink/api/links/',headers={"user-agent": "{acak}"},data={'url':url}).text
		if 'valid' in a:
			print '%s[%s!%s] %sInput yg bener !'%(W1,R1,W1,W0)
			time.sleep(0.8)
			s2()
		b=json.loads(a)
		c="https://rel.ink/"+b["hashid"]
		print "\033[1;32m[\033[1;33m√\033[1;32m] \033[0;37mResult : ",c
		print ("\033[1;32m[\033[1;33m!\033[1;32m] \033[0;37mPilih cok\n   \033[1;37m[\033[1;32m1\033[1;37m] \033[0;37mKunjungi link hasil shorten\n   \033[1;37m[\033[1;32m2\033[1;37m] \033[0;37mShorten lagi\n   \033[1;37m[\033[1;32m3\033[1;37m] \033[0;37mBack\n   \033[1;37m[\033[1;31m0\033[1;37m] \033[0;37mExit")
		y=raw_input("\033[1;32m[\033[1;33m?\033[1;32m] \033[0;37mPilih > ")
		if y == '1':
			os.system('xdg-open '+c)
			main()
		elif y == '2':
			s2()
		elif y == '3':
			main()
		elif y == '0':
			exit("%s[%sx%s] %sExiting program"%(W1,R1,W1,W0))
		else:
			main()
	except requests.exceptions.ConnectionError:
		exit("%s[%sx%s] %sTidak ada koneksi"%(W1,R1,W1,W0))
def s3():
	try:
		logo()
		url = raw_input('\033[1;32m[\033[1;33m?\033[1;32m]\033[0;37m Masukkan URL (use http/https): ')
		if url == '':
			print('%s[%s!%s] %sJangan kosong cok'%(W1,R1,W1,W0))
			time.sleep(0.8)
			s3()
		key = raw_input('\033[1;32m[\033[1;33m?\033[1;32m]\033[0;37m Masukkan keyword: ')
		if key == '':
			print('%s[%s!%s] %sJangan kosong cok'%(W1,R1,W1,W0))
			time.sleep(0.8)
			s3()
		a=requests.get('https://u.nu/api.php?action=shorturl&format=simple&url='+url+'&keyword='+key)
		print "\033[1;32m[\033[1;33m√\033[1;32m] \033[0;37mResult : ",a.text
		print ("\033[1;32m[\033[1;33m!\033[1;32m] \033[0;37mPilih cok\n   \033[1;37m[\033[1;32m1\033[1;37m] \033[0;37mKunjungi link hasil shorten\n   \033[1;37m[\033[1;32m2\033[1;37m] \033[0;37mShorten lagi\n   \033[1;37m[\033[1;32m3\033[1;37m] \033[0;37mBack\n   \033[1;37m[\033[1;31m0\033[1;37m] \033[0;37mExit")
		y=raw_input("\033[1;32m[\033[1;33m?\033[1;32m] \033[0;37mPilih > ")
		if y == '1':
			os.system('xdg-open '+a.text)
			main()
		elif y == '2':
			s3()
		elif y == '3':
			main()
		elif y == '0':
			exit("%s[%sx%s] %sExiting program"%(W1,R1,W1,W0))
		else:
			main()
	except requests.exceptions.ConnectionError:
		exit("%s[%sx%s] %sTidak ada koneksi"%(W1,R1,W1,W0))
def s4():
	try:
		logo()
		url = raw_input('\033[1;32m[\033[1;33m?\033[1;32m]\033[0;37m Masukkan URL: ')
		if url == '':
			print('%s[%s!%s] %sJangan kosong cok'%(W1,R1,W1,W0))
			time.sleep(0.8)
			s4()
		ua = requests.get('https://pastebin.com/raw/QckwZTMc').text.split('\n')
		acak = random.choice(ua)
		a=requests.get('http://wiki.sh/index.php?api=1&return_url_text=1&longUrl='+url,headers={"user-agent": "{acak}"})
		print "\033[1;32m[\033[1;33m√\033[1;32m] \033[0;37mResult : ",a.text
		print ("\033[1;32m[\033[1;33m!\033[1;32m] \033[0;37mPilih cok\n   \033[1;37m[\033[1;32m1\033[1;37m] \033[0;37mKunjungi link hasil shorten\n   \033[1;37m[\033[1;32m2\033[1;37m] \033[0;37mShorten lagi\n   \033[1;37m[\033[1;32m3\033[1;37m] \033[0;37mBack\n   \033[1;37m[\033[1;31m0\033[1;37m] \033[0;37mExit")
		y=raw_input("\033[1;32m[\033[1;33m?\033[1;32m] \033[0;37mPilih > ")
		if y == '1':
			os.system('xdg-open '+a.text)
			main()
		elif y == '2':
			s4()
		elif y == '3':
			main()
		elif y == '0':
			exit("%s[%sx%s] %sExiting program"%(W1,R1,W1,W0))
		else:
			main()
	except requests.exceptions.ConnectionError:
		exit("%s[%sx%s] %sTidak ada koneksi"%(W1,R1,W1,W0))
def s5():
	try:
		logo()
		url = raw_input('\033[1;32m[\033[1;33m?\033[1;32m]\033[0;37m Masukkan URL: ')
		if url == '':
			print('%s[%s!%s] %sJangan kosong cok'%(W1,R1,W1,W0))
			time.sleep(0.8)
			s4()
		ua = requests.get('https://pastebin.com/raw/QckwZTMc').text.split('\n')
		acak = random.choice(ua)
		semawur='https://semawur.com/st/?api=7e03f770c2a31272c0752474d0606ad1313ea1d6&url='
		b = semawur+url
		c = 'https://tinyurl.com/api-create.php?url='+b
		d = requests.get(c,headers={"user-agent": "{acak}"}).text
		print "\033[1;32m[\033[1;33m√\033[1;32m] \033[0;37mResult : ",d
		print ("\033[1;32m[\033[1;33m!\033[1;32m] \033[0;37mPilih cok\n   \033[1;37m[\033[1;32m1\033[1;37m] \033[0;37mKunjungi link hasil shorten\n   \033[1;37m[\033[1;32m2\033[1;37m] \033[0;37mShorten lagi\n   \033[1;37m[\033[1;32m3\033[1;37m] \033[0;37mBack\n   \033[1;37m[\033[1;31m0\033[1;37m] \033[0;37mExit")
		y=raw_input("\033[1;32m[\033[1;33m?\033[1;32m] \033[0;37mPilih > ")
		if y == '1':
			os.system('xdg-open '+a.text)
			main()
		elif y == '2':
			s5()
		elif y == '3':
			main()
		elif y == '0':
			exit("%s[%sx%s] %sExiting program"%(W1,R1,W1,W0))
		else:
			main()
	except requests.exceptions.ConnectionError:
		exit("%s[%sx%s] %sTidak ada koneksi"%(W1,R1,W1,W0))
def s6():
	try:
		logo()
		url = raw_input('\033[1;32m[\033[1;33m?\033[1;32m]\033[0;37m Masukkan URL: ')
		if url == '':
			print('%s[%s!%s] %sJangan kosong cok'%(W1,R1,W1,W0))
			time.sleep(0.8)
			s6()
		ua = requests.get('https://pastebin.com/raw/QckwZTMc').text.split('\n')
		acak = random.choice(ua)
		a=requests.post('http://gg.gg/check',data={'custom_path':'','use_norefs':'0','long_url':url,'app':'site','version':'0.1'},headers={"user-agent": "{acak}"})
		if 'ok' in a.text:
			b=requests.post('http://gg.gg/create',data={'custom_path':'','use_norefs':'0','long_url':url,'app':'site','version':'0.1'},headers={"user-agent": "{acak}"})
			print "\033[1;32m[\033[1;33m√\033[1;32m] \033[0;37mResult : ",b.text
			print ("\033[1;32m[\033[1;33m!\033[1;32m] \033[0;37mPilih cok\n   \033[1;37m[\033[1;32m1\033[1;37m] \033[0;37mKunjungi link hasil shorten\n   \033[1;37m[\033[1;32m2\033[1;37m] \033[0;37mShorten lagi\n   \033[1;37m[\033[1;32m3\033[1;37m] \033[0;37mBack\n   \033[1;37m[\033[1;31m0\033[1;37m] \033[0;37mExit")
			y=raw_input("\033[1;32m[\033[1;33m?\033[1;32m] \033[0;37mPilih > ")
			if y == '1':
				os.system('xdg-open '+b.text)
				main()
			elif y == '2':
				s6()
			elif y == '3':
				main()
			elif y == '0':
				exit("%s[%sx%s] %sExiting program"%(W1,R1,W1,W0))
			else:
				main()
		else:
			print('%s[%s!%s] %sInput url yg bener !'%(W1,R1,W1,W0))
			time.sleep(0.8)
			s6()
	except requests.exceptions.ConnectionError:
		exit("%s[%sx%s] %sTidak ada koneksi"%(W1,R1,W1,W0))
def main():
	try:
		os.system('git pull')
		logo()
		print ("%s{%s01%s} %sShortlink is.gd\n%s{%s02%s} %sShortlink rel.ink\n%s{%s03%s} %sShortlink u.nu\n%s{%s04%s} %sShortlink wiki.sh\n%s{%s05%s} %sShortlink tinyurl\n%s{%s06%s} %sShortlink gg.gg\n%s{%s07%s} %sContact (Whatsapp)\n%s{%s00%s} %sExit"%(W1,G1,W1,W0,W1,G1,W1,W0,W1,G1,W1,W0,W1,G1,W1,W0,W1,G1,W1,W0,W1,G1,W1,W0,W1,G1,W1,W0,W1,R1,W1,W0))
		no=["1","2","3","4","5","6","7","0","01","02","03","04","05","06","07","00"]
		chc=raw_input("\n%s╔%s[%sD4RK5H4D0W5%s]\n%s╚═══%s[%sChoice%s]> %s"%(C1,W1,P1,W1,C1,W1,P1,W1,W0))
		while chc not in no:
			logo()
			print ("%s{%s01%s} %sShortlink is.gd\n%s{%s02%s} %sShortlink rel.ink\n%s{%s03%s} %sShortlink u.nu\n%s{%s04%s} %sShortlink wiki.sh\n%s{%s05%s} %sShortlink tinyurl\n%s{%s06%s} %sShortlink gg.gg\n%s{%s07%s} %sContact (Whatsapp)\n%s{%s00%s} %sExit"%(W1,G1,W1,W0,W1,G1,W1,W0,W1,G1,W1,W0,W1,G1,W1,W0,W1,G1,W1,W0,W1,G1,W1,W0,W1,G1,W1,W0,W1,R1,W1,W0))
			print("\n%s[%sx%s] %sPilihan Anda salah"%(W0,R0,W0,R0))
			chc=raw_input("%s╔%s[%sD4RK5H4D0W5%s]\n%s╚═══%s[%sChoice%s]> %s"%(C1,W1,P1,W1,C1,W1,P1,W1,W0))
		if chc == '1' or chc == '01':
			s1()
		if chc == '2' or chc == '02':
			s2()
		if chc == '3' or chc == '03':
			s3()
		if chc == '4' or chc == '04':
			s4()
		if chc == '5' or chc == '05':
			s5()
		if chc == '6' or chc == '06':
			s6()
		if chc == '7' or chc == '07':
			print
			chat = raw_input('\033[1;32m[\033[1;33m#\033[1;32m] \033[0;37mIsi pesan mu : ')
			chat.replace(' ', '%20')
			spin()
			sp.check_output(['am', 'start','https://api.whatsapp.com/send?phone=628996604524&text=Report : ' +chat+''])
			main()
		if chc == '0' or chc == '00':
			exit("%s[%sx%s] %sExiting program"%(W1,R1,W1,W0))
	except requests.exceptions.ConnectionError:
		exit("%s[%sx%s] %sTidak ada koneksi"%(W1,R1,W1,W0))
if __name__=='__main__':
	main()
