#!bin/python
import os
import socket
import requests
os.system('clear')
main='''\033[1;36;40m
────────╔╗─╔╗───────╔╗
────────║║─║║───────║║
╔╗╔╦══╦═╝║─║╚═╦══╦══╣║╔╦══╦═╦══╗
║╚╝║╔╗║╔╗║─║╔╗║╔╗║╔═╣╚╝╣║═╣╔╣══╣
║║║║╔╗║╚╝╠╗║║║║╔╗║╚═╣╔╗╣║═╣║╠══║
╚╩╩╩╝╚╩══╩╝╚╝╚╩╝╚╩══╩╝╚╩══╩╝╚══╝
───────────────────╔╗
──────────────────╔╝╚╗
╔══╦══╦╗╔╦╗╔╦╗╔╦═╗╠╗╔╬╗─╔╗
║╔═╣╔╗║╚╝║╚╝║║║║╔╗╬╣║║║─║║
║╚═╣╚╝║║║║║║║╚╝║║║║║╚╣╚═╝║
╚══╩══╩╩╩╩╩╩╩══╩╝╚╩╩═╩═╗╔╝
─────────────────────╔═╝║
─────────────────────╚══╝
              ╱╱╱╱╱╱╱╱╱╱╱╱╭━╮╱╱╭╮
              ╭┳┳━┳━┳━┳━┳┳┫━╋━╮┣╋━╮
              ┃╭┫┻╋╮┃╭┫┻┫╭╋━┃┻┫┃┃╋┃
              ╰╯╰━╯╰━╯╰━┻╯╰━┻━╯╰┫╭╯
              ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯
'''

print("\033[1;34;40m=============================================")
print("\033[1;33;40m|     DEVELOPED BY MAD HACKERS COMMUNITY    |")
print("\033[1;34;40m=============================================")
print(main)
print("\033[1;34;40m=============================================")
print("\033[1;33;40m|     DEVELOPED BY MAD HACKERS COMMUNITY    |")
print("\033[1;34;40m=============================================")

print("\033[1;33;40mCODE NAME: H0rn3t Sp1d3rs || Mr. R013X 404  ")
print("\033[1;33;40mAuthor : Mad Hackers Community")
print("GITHUB : HTTPS://GITHUB.COM/H0rn3t-Sp1d3rs")
print("Website : https://www.h0rn3t-sp1d3rs.tk")

print("\033[1;34;40m=============================================")
print("\033[1;33;40m|     DEVELOPED BY MAD HACKERS COMMUNITY    |")
print("\033[1;34;40m=============================================")
print()
print("\033[1;31;40m[\033[1;32;40m01\033[1;31;40m]\033[1;32;40m REVERSE IP : ")

print("\033[1;31;40m[\033[1;32;40m02\033[1;31;40m]\033[1;32;40m CONTACT OWNER :")

opton=input("\033[1;36;40m[##] SELECT YOUR OPTION ==> \033[1;32;40m")
os.system('clear')
if opton=='01' or opton=='1':

	os.system('clear')
	print(main)
	print("=============================================\033[1;32;40m")
	file = open('url.txt').read().split()
	for url in file:
	   	domain = url.split('//')[1].replace('www.', '').replace('/', '').replace('//', '')
	   	try :
	   	   ipadrre = socket.gethostbyname(domain)
	   	   response = requests.get(f"https://sonar.omnisint.io/reverse/{ipadrre}").json()
	   	   print("\033[1;32;40m")
	   	   print(response) 
	   	           	
	   	   
	   	   print(len(response))
	   	   for urldata in response:
	   	           with open("url.txt", "a") as f:
	   	           	f.write(urldata+"\n")
	   	           	
	   	           	
	   	except:
	   	           		pass
	   	           		

	

elif opton=='2' or opton=='02':
	os.system(" xdg-open https://www.facebook.com/H0rn3t.Sp1d3rs")
	os.system('python bads.py')


else:
	print('\033[1;31;40mWRONG')
