import os,sys,getopt
#check for internet
pyvers = '2'
user = os.geteuid()
verbose = 0
binprefix = ""
logpath = "/var/log/"
usage = 0
workdir = os.getcwd()


if user != 0 :
	print "You must be root to install this program.  Try logging is as root (su -) or using sudo.\n"
	sys.exit()

if os.path.exists ('./sysmon.py') == False:
	print "sysmon.py not found.  It must be in the same folder as this installer.  Cannot continue\n"
	sys.exit() 
	
if os.path.exists('/sys/class/thermal/thermal_zone0/temp') == False:
	print "Sorry, your hardware is not yet supported.\nProceed with alternate installation? [Y/n]"
	i = str(input())
	if i != 'n' or i != 'N':
		print "Proceeding..."
	else:
		sys.exit()
	
if usage == 1:
	print "sysmon installation options:\n"
	print "-v/--verbose			Verbose (not currently used)"
	print "-h/--help			Display this usage info"
	print "--binprefix			Specify bin prefix (ie: /usr or /local)\n"
	sys.exit()

print "Installing sysmon:"
try:
	import psutil
	print "Modules already installed!"
except:
	print "Installing modules: "
	os.system('apt-get install pip')
	#os.system('Y')
	print "Updating..."
	os.system('apt-get update')
	os.system('pip install psutil')
	print "Installed modules!"

print "Copying program to /usr/local/bin"
os.system('chmod a+x ./sysmon.py')
os.system('cp ./sysmon.py /usr/local/bin/')
os.system('mv /usr/local/bin/sysmon.py /usr/local/bin/sysmon')
os.system('chmod 0777 /usr/local/bin/sysmon')
print "Copying icons"
os.system('cd ~')

os.system('mkdir /usr/local/share/sysmon')
os.system('chmod 0777 ./gear-1.png')
os.system('cp ./gear-1.png /usr/local/share/sysmon')
os.system('chmod 0777 /usr/local/share/sysmon/gear-1.png')
os.system('chmod +x ./sysmon.desktop')
os.system('cp ./sysmon.desktop ~/Desktop')
os.system('chmod 0777 ~/Desktop/sysmon.desktop')
os.system('cp ~/Desktop/sysmon.desktop ~/.local/share/applications') # may not work
os.system('chmod 0777 ~/.local/share/applications/sysmon.desktop')
print "Done!"
	

print "Checking if log exists:  " ,
while os.path.exists (logpath + "/sysmon.log") == True: 
	open (logpath + "/sysmon.log", 'r+' ).write("sysmon log    \n\n")
	print "Yes"
	break
while os.path.exists (logpath + '/sysmon.log') == False: 
	print "No\n   ***Creating Log:  " ,
	open (logpath + "/sysmon.log", 'w' ).write("sysmon log    \n\n")
	os.system('chmod 666 ' + logpath + '/sysmon.log')
	print "Done."

print "Installation finished.  Type sysmon as any user to run."
sys.exit()
