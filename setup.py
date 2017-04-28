# Opens the config files, stores the data in a library
import sys
from os import path
from ast import literal_eval
import string
import random
# Enter path to files in shell script
dnsmasq = path.relpath("dnsmasq.conf")
sipconf = path.relpath("sip.conf")
mactemplate = path.relpath("mac-template")
new_phones = path.relpath("new_phones")
# dnsmasq = path.relpath($1)
# mactemplate = path.relpath($2)
# sipconf = path.relpath($3)
# new_phones = path.relpath($4)
#
# random password generator from http://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))
# 	
#Load up data from previous runs
#
#	TODO: implement
#
#Open's DNSMASQ.CONF and obtains the largest valid range
#	TODO: convert data structure to dictionary
#	TODO: find bug allowing two copies of a mac address to be in dnsmaq.conf
#
mac_addresses = set( [])
ip_addresses = set( [])
taken_ranges = set( [])
with open( dnsmasq) as f:
	for line in f:
 		#print "Is this line dhcp? %s" % line[:10]
		if line[:10] == "dhcp-host=" :
			mac_addresses.add( line[10:27])
			#print "Line 36-39: %s" % line[36:39]
			ip_addresses.add( eval( line[36:39]))
			pos = line.find("PN: ",40)
			if pos != -1:
				taken_ranges.add( eval( line[pos +4 :pos +7]))
			else:
				taken_ranges.add( -999)

# Appends to DNSMASQ from a list of mac_addresses and ranges with the format
# xx:xx:xx:xx:xx:xx [1-9]00 [device name] from file "new_phones" 
# adds new entry to sip.conf using a password generator
with open( new_phones) as mew:
	for line in mew:
                mac_addr = line[:17]
                if mac_addr in mac_addresses:
                    print "Mac %s already exinsting in dnsmasq" % mac_addr
                    sys.exit()
		pw = id_generator(10)
		pn = line[18:21]
		with open( dnsmasq, 'a+') as f:
                        #print( "dhcp-host=" +  mac_addr + ",10.11.6." )
                        f.write( "dhcp-host=" +  mac_addr + ",10.11.6." )
			next_available_ip = str( max( ip_addresses) + 1)
			ip_addresses.add(eval(next_available_ip))
                        #print( next_available_ip.ljust(3) + "# " + line[21:].strip() + " PN: ") # 21: is the device name
                        f.write( next_available_ip.ljust(3) + "# " + line[21:].strip() + " PN: ") # 21: is the device name
			f.write (pn)
			f.write( "\n")
		with open( sipconf, 'a+') as f:
			#print( "\n[" + pn + "](people)\nsecret=" + pw + "\n")
			f.write( "\n[" + pn + "](people)\nsecret=" + pw + "\n")
                with open ("tftp/" + line[:17].replace(":",''), 'w+') as f:
			#print( "[VOIP]" + \
			f.write( "[VOIP]" + \
                                "\nline1_displayname " + pn +\
                                "\nline1_name " + pn + \
                                "\nline1_authname " + pn + \
                                "\nline1_password " + pw)
