######### Author: Raj Prasad Kuiri ################
######### email: prasadraj954@gmail.com ##########
# Nmap port scanner

import nmap
scanner = nmap.PortScanner()
print("welcome to the port scanner")
print("<------------------------------------------->")
ip = input('enter the IP address for port scanning')
type(ip)
resp = input(''' \n enter the option for scanning
                  1. SYN scan
                  2. UDP scan
                  3. comprensive scan\n''')

print("your option is:",resp)

if resp=='1':
    print("Nmap version:",scanner.nmap_version())
    scanner.scan(ip,'1-1024','-v -sS')
    print(scanner.scaninfo())
    print("IP status:",scanner[ip].state())
    print("prolocols:", scanner[ip].all_protocols())
    print("open ports:", scanner[ip]['tcp'].keys())

elif resp== '2':
    print("Nmap version:", scanner.nmap_version())
    scanner.scan(ip,'1-1024','-v -sU')
    print(scanner.scaninfo())
    print("IP status:", scanner[ip].state())
    print("protocols:",scanner[ip].all_protocols())
    print("open ports:", scanner[ip]['UDP'].keys())

elif resp== '3':
    print("Nmap version", scanner.nmap_version())
    scanner.scan(ip,'1-1024','-v -sS -sV -sC -A -O')
    print("IP status:", scanner[ip].state())
    print("protocols:",scanner[ip].all_protocols())
    print("open ports:", scanner[ip]['UDP'].keys())

elif resp >='3':
    print(" invalid option") 



