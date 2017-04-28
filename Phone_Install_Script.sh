

#Phone Installation Script for VOIP
# setup.py - python script for parsing. needs to be in same directory as bash script.
# 
#@ WYung


#ENTER PATH FOR FILES: mac-template, dnsmasq.conf, sip.conf
location_mac-template=smb://rt-n56u-e4c9/root/Workspace/mac-template
location_dnsmasq.conf=smb://rt-n56u-e4c9/root/Workspace/dnsmasq.conf
locaton_sip.conf=smb://rt-n56u-e4c9/root/Workspace/sip.conf
location_newphones=

# Sanity Check
######################
if [ ! -e $location_dnsmasq.conf ]; then
	echo "Missing dnsmasq.conf file, ask rubber duck:ERROR 0001"
	exit
fi
######################
if [ ! -e $location_mac-template ]; then

	echo "Missing mac-template file, ask rubber duck:ERROR 0010"
	exit
fi
######################
if [ ! -e $locaton_sip.conf ]; then
	echo "Missing sip.conf file, ask rubber duck:ERROR 0011"
	exit
fi
######################
if [ ! -e $setup.py ]; then
	echo "Missing Python script, ask rubber duck:ERROR 0100"
	exit
fi
######################
if [ ! -e $newphones ]; then
	echo "Missing new phone list, ask rubber duck:ERROR 0101"
	exit
fi
######################
if [ -e $piconf ]; then
  	echo "Config file config found!"
  	#ideally pass setup info to the 
  	python setup.py location_dnsmasq location_mac-template locaton_sip location_newphones
else
	echo "Missing config file, ask rubber duck:   00110"
	echo "Manually remaking config file, rerun script."
  	echo >> piconf
  	#obtain info
fi
######################
#Load Config



# DNS
# if [ -e $location_dnsmasq.conf ]; then
#   	echo "Config file piconf found!"
#   	i=1
# 	while read line;do
#         run = $line
#         ((i++))
# 	done < piconf
# 	$run
# else
#   echo "Missing dnsmasq.conf!"
#   echo "Script Ending"
#   exit 1;
# fi