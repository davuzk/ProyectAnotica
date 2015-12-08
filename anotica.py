import os, sys, traceback, subprocess
def wenURedy():
	print 'Press enter when you are done'
	raw_input()
	main()
def main():
	print '''
      ___               _   _           
     /$$$\             |$| ($)          
    /$/_\$\_ __    ___ |$|_ _  ___   __  _ 
    |$ _ $|$'$$$\/$$$$\|$$$|$|/$$$$ /$$_`$|
    |$| |$|$| |$|$(_)$||$| |$|$|    |$(_|$|
    \$| |$/$| |$|\$$$$/\$$$|$|\$$$$ \$$,$$|

    =[ ~ | Created by: Spirit / Davuzk [Secret Services] | ~ ]=

	'''
	print '''
    1) Update the packages		2) Install Proxychains
    3) Install TOR service      \t4) View Proxychains configuration
    5) Install everything and update packages

    '''

	alternative = raw_input('\n[Choise]~>')
        if alternative == '1':
             os.system('apt-get update')
	     wenURedy()
        elif alternative == '2':
             os.system('apt-get install proxychains')
             wenURedy()
	elif alternative == '3':
             os.system('apt-get install tor')
             wenURedy()
	elif alternative == '4':
             os.system('cat /etc/proxychains.conf')
	     wenURedy()
	elif alternative == '5':
                subprocess.call(['apt-get update','apt-get install proxychains', 'apt-get install tor'])
if __name__ == '__main__':
			main()
