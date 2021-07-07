#!/usr/bin/python3

##THIS IS THE IMPORTING OS LIBRARY
import readline
import os,sys
from colorama import Fore,init
init()
from termcolor import colored
from getpass import getpass

#logo printer
def logo():
    logo = """
         ██████╗  █████╗ ███████╗███████╗██╗    ██╗██████╗ ██████╗ 
         ██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔══██╗██╔══██╗
         ██████╔╝███████║███████╗███████╗██║ █╗ ██║██║  ██║██████╔╝
         ██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║  ██║██╔══██╗
         ██║     ██║  ██║███████║███████║╚███╔███╔╝██████╔╝██████╔╝
         ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝ ╚═════╝ ╚═════╝ """
    print(colored(text=logo, color='yellow'))
    print("\t"*4,colored(text="passwdb v1.0", color='yellow', attrs=['blink']))

# this function saved the passwords and hashs on databases 
def sqliteW(sname,name,passwd,hash):
	os.system("clear") if os.name=="posix" else os.system("cls")
	logo()
	pwd=os.getcwd()
	import sqlite3
	try:
		dname=sname
		db=sqlite3.connect(".%s"%(dname))
		db.execute("CREATE TABLE hashs (name varchar(20),password INT,hashs varchar(256))")
		db.execute("INSERT INTO hashs VALUES('%s','%s','%s')"%(name,passwd,hash))
		db.commit()
		print(Fore.LIGHTBLUE_EX+" Query 1,OK")
		db.close()
		input(Fore.LIGHTBLUE_EX+" press enter to back "+Fore.LIGHTRED_EX+"✗ "+Fore.LIGHTBLUE_EX)
		passwdb(sname)
	except Exception as e:
		db=sqlite3.connect(".%s"%(dname))
		db.execute("INSERT INTO hashs VALUES('%s','%s','%s')"%(name,passwd,hash))
		db.commit()
		db.close()
		print(Fore.LIGHTBLUE_EX+" Query 1, OK")
		input(Fore.LIGHTBLUE_EX+" press enter to back "+Fore.LIGHTRED_EX+"✗ "+Fore.LIGHTBLUE_EX)
		passwdb(sname)
		
# database reader		
def sqliteR(sname):
	import sqlite3
	os.system("clear") if os.name=="posix" else os.system("cls")
	logo()
	pwd=os.getcwd()
	print(Fore.LIGHTBLUE_EX+" name of password or all")
	cms=input(Fore.LIGHTBLUE_EX+" passwdb "+Fore.LIGHTRED_EX+"✗ "+Fore.LIGHTBLUE_EX)
	dname=sname
	flash = f"{Fore.YELLOW}➜{Fore.LIGHTCYAN_EX}"
	if cms == "all":
		try:
			db=sqlite3.connect(".%s"%dname) 
			hashs=db.execute("SELECT * FROM hashs")
			for name,passwd,phash in hashs:
				print(Fore.LIGHTCYAN_EX+f"\tname {flash} %s\n\tpassword {flash} %s\n\tmd5 {flash} %s\n"%(name,passwd,phash))
			db.close()
			input(Fore.LIGHTBLUE_EX+" press enter to back "+Fore.LIGHTRED_EX+"✗ "+Fore.LIGHTBLUE_EX)
			passwdb(sname)
		except:
			print(Fore.LIGHTRED_EX+"➜"+Fore.LIGHTBLUE_EX+" isn't any password on database !")
			input(" press enter to back ")
			passwdb(sname)
	elif cms == "quit":
		os.chdir(pwd)
		sys.exit()
	else:
		try:
			db=sqlite3.connect(".%s"%(dname)) 
			hashs=db.execute("SELECT *  FROM hashs WHERE name='%s'"%(cms))
			for name,passwd,phash in hashs:
				print(Fore.LIGHTCYAN_EX+f"\tname {flash} %s\n\tpassword {flash} %s\n\tmd5 {flash} %s"%(name,passwd,phash))
			db.close()
			input(Fore.LIGHTBLUE_EX+" press enter to back "+Fore.LIGHTRED_EX+"✗ "+Fore.LIGHTBLUE_EX)
			passwdb(sname)
		except:
				db.close()
				input(Fore.LIGHTBLUE_EX+" press enter to back "+Fore.LIGHTRED_EX+"✗ "+Fore.LIGHTBLUE_EX)
				passwdb(sname)
# password deleter				
def sqliteD(sname):
	os.system("clear") if os.name=="posix" else os.system("cls")
	logo()
	pwd=os.getcwd()
	from time import sleep
	inec=["[0]- one", "[1]- all"]
	for i in inec:
		print(Fore.YELLOW+"➜"+Fore.LIGHTBLUE_EX+" "+i,"\n")
		sleep(0.2)
	ind=input(Fore.LIGHTBLUE_EX+" passwdb "+Fore.LIGHTRED_EX+"✗ "+Fore.LIGHTBLUE_EX)
	dname=sname
	if ind == "0":
		os.system("clear") if os.name=="posix" else os.system("cls")
		logo()
		name=input(Fore.LIGHTBLUE_EX+" enter name "+Fore.LIGHTRED_EX+"✗ "+Fore.LIGHTBLUE_EX)
		passwd=input(Fore.LIGHTBLUE_EX+" enter password "+Fore.LIGHTRED_EX+"✗ "+Fore.LIGHTBLUE_EX)
		es=input(Fore.LIGHTBLUE_EX+" do you want to delete it ? [y/n] "+Fore.LIGHTRED_EX+"✗ "+Fore.LIGHTBLUE_EX).upper()
		if es == "Y":
			import sqlite3
			db=sqlite3.connect(".%s"%(dname)) 
			db.execute("DELETE FROM hashs WHERE name='%s' AND password='%s' "%(name,passwd))
			db.commit()
			db.close()
			print(Fore.LIGHTBLUE_EX+" Query 1, OK")
			input(Fore.LIGHTBLUE_EX+" press enter to back "+Fore.LIGHTRED_EX+"✗ "+Fore.LIGHTBLUE_EX)
			passwdb(sname)
		else:
			passwdb(sname)
	elif ind == "1":
		os.system("clear") if os.name=="posix" else os.system("cls")
		logo()
		es=input(Fore.LIGHTBLUE_EX+" do you want to delete it ? [y/n] "+Fore.LIGHTRED_EX+"✗ "+Fore.LIGHTBLUE_EX).upper()
		if es == "Y":
			import sqlite3
			db=sqlite3.connect(".%s"%(dname)) 
			db.execute("DELETE FROM hashs")
			db.commit()
			db.close()
			input(Fore.CYAN+"➜"+Fore.LIGHTBLUE_EX+" press enter to back "+Fore.LIGHTRED_EX+"✗ "+Fore.LIGHTBLUE_EX)
			passwdb(sname)
		else:
			input(Fore.LIGHTBLUE_EX+" press enter to back" +Fore.LIGHTRED_EX+"✗ "+Fore.LIGHTBLUE_EX)
			passwdb(sname)
	elif ind == "exit" or "quit":
		os.chdir(pwd)
		sys.exit()
	else:
		print(Fore.LIGHTRED_EX+"➜"+Fore.LIGHTRED_EX+" not Found !")
		input(Fore.LIGHTBLUE_EX+" press enter to back "+Fore.LIGHTRED_EX+"✗ "+Fore.LIGHTBLUE_EX)
		passwdb(sname)
		
# this function hashs the passwords
def hash(sname,name,passwd):
	import hashlib
	hsh=hashlib.md5()
	hsh.update(passwd.encode("utf-8"))
	hash=hsh.hexdigest()
	sqliteW(sname,name,passwd,hash)

# account creator 
def account():
    os.system("clear") if os.name == "posix" else os.system("cls")
    logo()
    pwd=os.getcwd()
    name=input(Fore.LIGHTBLUE_EX+" enter name "+Fore.LIGHTRED_EX+"✗ "+Fore.LIGHTBLUE_EX+"")
	#passwd=input(Fore.LIGHTBLUE_EX+" enter password "+Fore.LIGHTRED_EX+"✗ "+Fore.LIGHTBLUE_EX)
    passwd = getpass(Fore.LIGHTBLUE_EX+" enter name "+Fore.LIGHTRED_EX+"✗ "+Fore.LIGHTBLUE_EX+"")
    print(Fore.LIGHTBLUE_EX+" ok !, please wite ...")
    import hashlib
    hsh=hashlib.md5()
    hsh.update(passwd.encode("utf-8"))
    hash=hsh.hexdigest()
    import sqlite3
    db=sqlite3.connect(".li.db")
    
    try:
	    db.execute("CREATE TABLE li (name varchar(20),password INT,hashs varchar(256))")
	    db.execute("INSERT INTO li VALUES('%s','%s','%s')"%(name,passwd,hash))
	    db.commit()
	    print(Fore.LIGHTBLUE_EX+" Query 1,OK")
	    db.close()
    except Exception:
	    db.execute("INSERT INTO li VALUES('%s','%s','%s')"%(name,passwd,hash))
	    db.commit()
    except:
        print(Fore.LIGHTRED_EX+"➜"+Fore.LIGHTBLUE_EX+" this account is already exists !")
    finally:
        login()
		
def login():
    from time import sleep 
    os.system("clear") if os.name == "posix" else os.system("cls")
    pwd=os.getcwd()
    logo()
    print(Fore.LIGHTBLUE_EX+" WELCOME TO PASSWDB ! :)\n")
    incm=["[0]- login ","[1]- account"] 
    for e in incm:
        print(Fore.YELLOW+" ➜"+Fore.LIGHTBLUE_EX+" "+e,"\n")
    com=(input(Fore.LIGHTBLUE_EX+" passwdb "+Fore.LIGHTRED_EX+"✗ "+Fore.LIGHTBLUE_EX))
    if com == "0":
        os.system("clear") if os.name == "posix" else os.system("cls")
        logo()
        name=input(Fore.LIGHTBLUE_EX+" enter name "+Fore.LIGHTRED_EX+"✗ "+Fore.LIGHTBLUE_EX+"")
		#passwd=input(Fore.LIGHTBLUE_EX+" enter password "+Fore.LIGHTRED_EX+"✗ "+Fore.LIGHTBLUE_EX)
        passwd = getpass(Fore.LIGHTBLUE_EX+" enter password "+Fore.LIGHTRED_EX+"✗ "+Fore.LIGHTBLUE_EX)
        print(Fore.LIGHTBLUE_EX+" ok !, please wite ...")
        import sqlite3
        try:
            db=sqlite3.connect(".li.db")
            ac=db.execute("SELECT * FROM li")
            sname=name
        except:
            print(Fore.LIGHTRED_EX+" ➜"+Fore.LIGHTBLUE_EX+" account is not exists !")
            input(Fore.LIGHTBLUE_EX+" press enter to back "+Fore.LIGHTRED_EX+"✗ "+Fore.LIGHTBLUE_EX)
            loginer()
        for pname,ppasswd,phash in ac:
            nname=pname
            npasswd=ppasswd
            nhash=phash
        if name == nname:
            if passwd == npasswd:
                passwdb(sname)
            else:
                print(Fore.LIGHTRED_EX+" ➜"+Fore.LIGHTBLUE_EX+" name or password is wrong ! ")
                input(Fore.LIGHTBLUE_EX+" press enter to back "+Fore.LIGHTRED_EX+"✗ "+Fore.LIGHTBLUE_EX)
                loginer()
        else:
            print(Fore.LIGHTRED_EX+" ➜"+Fore.LIGHTBLUE_EX+" name or password is wrong ! ")
            input(Fore.LIGHTBLUE_EX+" press enter to back "+Fore.LIGHTRED_EX+"✗ "+Fore.LIGHTBLUE_EX)
            loginer()

    elif com == "1":
        account()
    elif com == "exit" or "quit":
        os.chdir(pwd)
        sys.exit()
def loginer():
	os.system("clear")
	login()
	
def passwdb(sname):
    from time import sleep 
    pwd=os.getcwd()
    os.system("clear") if os.name == "posix" else os.system("cls")
    logo()
    incm=["[0]- write","[1]- read","[2]- delete"]
    for e in incm:
        print(Fore.YELLOW+" ➜"+Fore.LIGHTBLUE_EX+" "+e,"\n")
        sleep(0.2)
    com=(input(Fore.LIGHTBLUE_EX+" passwdb "+Fore.LIGHTRED_EX+"✗ "+Fore.LIGHTBLUE_EX))  
    if com == "0":
        os.system("clear") if os.name == "posix" else os.system("cls")
        logo()
        name=input(Fore.LIGHTBLUE_EX+" enter name "+Fore.LIGHTRED_EX+"✗ "+Fore.LIGHTBLUE_EX).strip()
		#passwd=input(Fore.LIGHTBLUE_EX+" enter password "+Fore.LIGHTRED_EX+"✗ "+Fore.LIGHTBLUE_EX).strip()
        passwd = getpass(Fore.LIGHTBLUE_EX+" enter password "+Fore.LIGHTRED_EX+"✗ "+Fore.LIGHTBLUE_EX)	
        print(Fore.LIGHTBLUE_EX+" ok, please wite ...")
        hash(sname,name,passwd)
    elif com == "1":
        sqliteR(sname)
    elif com == "2":
        sqliteD(sname)
    elif com =="exit" or "quit":
        os.chdir(pwd)
        sys.exit()
    else:
        print(Fore.LIGHTRED_EX+" ➜"+Fore.LIGHTBLUE_EX+" this is no found !")
        input(Fore.LIGHTBLUE_EX+" press enter to back "+Fore.LIGHTRED_EX+"✗ "+Fore.LIGHTBLUE_EX)
        passwdb(sname)
loginer()
sname=""
if __name__ == "__passwdb__":passwdb(sname)
if __name__ == "__account__":account()
if __name__ == "__login__":login()
if __name__ == "__loginer__":loginer()
