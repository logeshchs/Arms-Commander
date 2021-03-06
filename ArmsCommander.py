#!/usr/bin/env python
# coding=UTF-8

#The first line allows this script to be executable

import os
import socket
import operator
from termcolor import colored
import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen


os.system('cat /root/ArmsCommander/banners/ACBanner.txt')

def MT_host_recon():
    os.system('python /root/ArmsCommander/recon/multi_tool_recon.py')
    return

def CornHarvester():
    os.system('python /root/ArmsCommander/recon/CornHarvester.py')
    return

def NMap_Auto():
    os.system('python /root/ArmsCommander/recon/nmap.py')
    return

def SQLMap():
    os.system("gnome-terminal -e 'bash -c \"python /root/ArmsCommander/networkdefenses/proxychainsTest.py; exec bash\"'")
    os.system('python /root/ArmsCommander/recon/SQLMapCustom.py')
    return

def OWASP_zaproxy():
    os.system("gnome-terminal -e 'bash -c \"zaproxy; exec bash\"'")
    main()
    return

def burpsuite():
    os.system("gnome-terminal -e 'bash -c \"burpsuite; exec bash\"'")
    main()
    return

def output_data():

    print 'For further reference, all data was saved in your /root/ArmsCommander/logs/ directory if you wanted to access them or back it up manually'
    opt_List = [
        '\n\t#0. Return to Previous Menu',
        '#1. Output all MULTI-TOOL SCAN DATA',
        '#2. Output all CORNHARVESTER DATA',
        '#3. Output all NMAP DATA',
        '#4. Make a logfile backup of the data using RSYNC (unintrusive, wont copy over files)',
        '#5. IMPORT logfile backups from a specified directory'
    ]

    print("\n\t".join(opt_List))

    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "1":
        os.system('clear')
        os.system('cat /root/ArmsCommander/logs/multi_tool_recon/*')
        output_data()
    elif opt_Choice == "2":
        os.system('clear')
        os.system('cat /root/ArmsCommander/logs/CornHarvester/*')
        output_data()
    elif opt_Choice == "3":
        os.system('clear')
        os.system('cat /root/ArmsCommander/logs/nmap/*')
        output_data()
    elif opt_Choice == "0":
        os.system('clear')
        one_recon_and_vuln_scan()
    elif opt_Choice == "4":
        os.system('clear')
        cmd_String = "rsync -v -r /root/ArmsCommander/logs /root/Documents/ArmsCommander_logs_backup"
        os.system(cmd_String)
        user_String = 'All files backed up in folder: /root/Documents/ArmsCommander_logs_backup'
        print colored(user_String,'red','on_white')
        output_data()
    elif opt_Choice == "5":
        import_directory = str(raw_input("Enter the full directory path where the to-be-imported files are located: "))
        import_path = import_directory + '/*'
        cmd_String = "rsync -v -r %s /root/ArmsCommander/logs" % import_path
        os.system(cmd_String)
        print colored('All log files imported to /root/ArmsCommander/logs','red','on_white')
        output_data()
    else:
        print 'You have entered a invalid option'
        output_data()

    return
def one_recon_and_vuln_scan():
    opt_List = [
        '\n\t#0. Return to Main Menu',
        '#1. Multi-Tool Single Host Recon, use Dig, NSLookup, fierce, and theharvester against a single target',
        '#2. CornHarvester, mass-harvest emails for phishing/Spear-Phishing',
        '#3. NMap Scans (preset for maximum information discovery), starts with FIN scan, then XMAS scan, and finally a comprehensive scan',
        '#4. Run SQLMap (Automatically set to route traffic through Tor)',
        '#5. OWASP Zaproxy (Alternative vulnerability scanner, much faster than SQLMap)',
        '#6. BurpSuite',
        '#7. OUTPUT/BACKUP ALL DATA collected from Multi-Tool, CornHarvester, and NMap'
    ]
    print ("\n\t".join(opt_List))

    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "0":
        os.system('clear')
        main()
    elif opt_Choice == "1":
        os.system('clear')
        MT_host_recon()
    elif opt_Choice == "2":
        os.system('clear')
        CornHarvester()
    elif opt_Choice == "3":
        os.system('clear')
        NMap_Auto()
    elif opt_Choice == "4":
        os.system('clear')
        SQLMap()
        # NMap_Custom()
    elif opt_Choice == "5":
        os.system('clear')
        OWASP_zaproxy()
        # SQLMap()
    elif opt_Choice == "6":
        os.system('clear')
        burpsuite()
    elif opt_Choice == "7":
        os.system('clear')
        output_data()
    else:
        print 'You have entered a invalid option'
        one_recon_and_vuln_scan()
    return

def tor_and_proxychains():
# /root/ArmsCommander/networkdefenses/proxychainsTest.py
    os.system("gnome-terminal -e 'bash -c \"python /root/ArmsCommander/networkdefenses/proxychainsTest.py; exec bash\"'")
    main()
    return

def network_monitor_tools():
    #Snort
    print colored('Launching Intrusion Detection System','red','on_white')
    os.system("gnome-terminal -e 'bash -c \"sudo snort -q -A console -c /etc/snort/snort.conf; exec bash\"'")

    #p0f
    print colored('Starting p0f, passive OS fingerprinter','red','on_white')
    os.system("gnome-terminal -e 'bash -c \"sudo p0f; exec bash\"'")
    #viewActiveConnections
    print colored('Listing Real Time Active Connections','red','on_white')
    os.system("gnome-terminal -e 'bash -c \"sudo watch -b -c ss -tp; exec bash\"'")
    main()

    return

def cover_tracks():
    print 'Clearing bash history'
    os.system('rm -rf /root/.bash_history')
    print 'Clearing thumbnails'
    os.system('rm -rf /root/.cache/thumbnails')

    print colored('Both your bash shell history and your thumbnails cache has been WIPED. Warning, the data can still be recovered, you must overwrite the disk with zeroes using the Kali Installer to fully eliminate forensic recovery','red','on_white')
    print"""
    Furthermore, using this does not completely eliminate the need to...

    1. Delete your trash
    2. Clean out your auth logs

    This only prevents LE from finding the most incriminating information in five minutes
    """
    print colored('Retain a lawyer before you resort to doing anything bad','red','on_white')
    main()
    return

def TCPKill():
# /root/ArmsCommander/networkdefenses/TCPKill.py
    os.system("gnome-terminal -e 'bash -c \"python /root/ArmsCommander/networkdefenses/TCPKill.py; exec bash\"'")


    return

def NGrep():
# /root/ArmsCommander/networkdefenses/NGrepCustom.py
    os.system("gnome-terminal -e 'bash -c \"python /root/ArmsCommander/networkdefenses/NGrepCustom.py; exec bash\"'")

    return

def macchanger():
# /root/ArmsCommander/networkdefenses/macChanger.py
    os.system("gnome-terminal -e 'bash -c \"python /root/ArmsCommander/networkdefenses/macChanger.py; exec bash\"'")

    return

def fuser():
    opt_List = [
                '\n\t#1. LOOKUP all process IDs of a port and protocol',
                '#2. Terminate all connections of a port/protocol'
    ]

    print ("\n\t".join(opt_List))
    opt_Choice = str(raw_input("Enter a OPTION: "))
    if opt_Choice == "1":
        fuser_port = str(raw_input("Enter a PORT: "))
        fuser_protocol = str(raw_input("Enter a PROTOCOL(tcp/udp): "))
        fuser_cmd_string = "fuser %s/%s" % (fuser_port, fuser_protocol)
        os.system(fuser_cmd_string)
    elif opt_Choice == "2":
        fuser_port = str(raw_input("Enter a PORT: "))
        fuser_protocol = str(raw_input("Enter a PROTOCOL(tcp/udp): "))
        fuser_cmd_string = "fuser -k %s/%s" % (fuser_port, fuser_protocol)
        os.system(fuser_cmd_string)
    elif opt_Choice == "0":
        main()
    else:
        print colored('You have entered a invalid option','red','on_white')
    main()
    return

def IDS_Flooder():
# /root/ArmsCommander/networkdefenses/IDS_flood.py
    os.system("gnome-terminal -e 'bash -c \"python /root/ArmsCommander/networkdefenses/IDS_flood.py; exec bash\"'")

    return

def two_net_defense_traffic_monitor():
    opt_List = [
        '\n\t#0 Return to Main Menu',
        '#1. Tor + Proxychains, conceal your outbound traffic',
        '#2. Network Monitoring Tools, p0f, Snort, and view active network connections',
        '#3. Cover your tracks, clear your bash history and wipe your thumbnails cache',
        '#4. TCP Kill a connection by host, IP, or port',
        '#5. NGrep or "Network Grep", investigate a suspicious connection',
        '#6. MacChanger, change your network card MAC address temporarily',
        '#7. Fuser, identify and kill processes within a port range',
        '#8. IDS Flooder, overwhelm a Intrusion Detection System with false-flag DDoS attacks to draw attention away from your actual activity'
    ]
    print ("\n\t".join(opt_List))
    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "0":
        os.system('clear')
        main()
    elif opt_Choice == "1":
        os.system('clear')
        tor_and_proxychains()
        # MT_host_recon()
    elif opt_Choice == "2":
        os.system('clear')
        network_monitor_tools()
        # CornHarvester()
    elif opt_Choice == "3":
        os.system('clear')
        cover_tracks()
        # NMap_Auto()
    elif opt_Choice == "4":
        os.system('clear')
        TCPKill()
        # NMap_Custom()
    elif opt_Choice == "5":
        os.system('clear')
        NGrep()
        # SQLMap()
    elif opt_Choice == "6":
        os.system('clear')
        macchanger()
        # OWASP_zaproxy()
    elif opt_Choice == "7":
        os.system('clear')
        fuser()
        # burpsuite()
    elif opt_Choice == "8":
        os.system('clear')
        IDS_Flooder()
    else:
        print 'You have entered a invalid option'
        two_net_defense_traffic_monitor()

    return

def metasploit():
    os.system('python /root/ArmsCommander/remoteexploits/Metasploit.py')
    main()
    return

def armitage():
    os.system('chmod 777 /root/ArmsCommander/remoteexploits/ArmitageWithProxychains.sh')
    os.system('/root/ArmsCommander/remoteexploits/ArmitageWithProxychains.sh')
    main()
    return

def easy_peasey():
    os.system('python /root/ArmsCommander/remoteexploits/EZPZ.py')
    main()
    return

def veil_evasion():
    os.system('veil-evasion')
    main()
    return

def social_engineers_toolkit():
    os.system('setoolkit')
    main()
    return

def pupy_menu():
    os.system('python /root/ArmsCommander/remoteexploits/Pupy_Menu.py')
    main()
    return

def DPMB():
    os.system('python /root/ArmsCommander/remoteexploits/DPMB.py')
    main()
    return

def VT_Checker():
    os.system('cat /root/ArmsCommander/banners/disclaimer_VT_Checker.txt')

    opt_List = [
        '\n\t#0. Return to Main Menu',
        '#1. Submit a single HASH checksum to Virus Total',
        '#2. Check a entire directory at a time (probably filled with generated malware)'
    ]
    print("\n\t".join(opt_List))
    opt_Choice = str(raw_input("Enter a OPTION: "))
    if opt_Choice == "1":
        sample_file = str(raw_input("Enter the full path of the file you want to check: "))
        cmd_String = "ruby /usr/share/veil-evasion/tools/vt-notify/vt-notify.rb -s %s" % sample_file
        os.system(cmd_String)
    elif opt_Choice == "2":
        sample_directory = str(raw_input("Enter the full path of the directory that you want to check: "))
        cmd_String = "ruby /usr/share/veil-evasion/tools/vt-notify/vt-notify.rb -d %s" % sample_directory
        os.system(cmd_String)
    elif opt_Choice == "0":
        main()
    else:
        print 'You have entered a invalid option'
        VT_Checker()
    main()
    return

def embed_payload_pdf():
    os.system('python /root/ArmsCommander/remoteexploits/embed_pdf_pupy.py')
    main()
    return


def three_remote_exploits():
    opt_List = [
        '\n\t#0. Return to Main Menu',
        '#1. Metasploit Framework, with a Manual-Start Script to overcome any database init issues',
        '#2. Armitage',
        '#3. Easy-Peasey, msfvenom payload generator',
        '#4. Veil-Evasion, changes signature of msfvenom type payloads',
        '#5. Social Engineers Toolkit (SET), a expansive toolkit by itself that covers spearphishing attacks to SMS spoofing to Arduino-attacks',
        '#6. Pupy, Cross-Platform, Pythonic version of a Remote Access Trojan (RAT) with abilities that are comparable/superior to Meterpreter shells, with added benefits of being rarer and therefore harder to detect, and supports powershell injection',
        '#7. Dont Patch Me Bro :(, the easy-mode inject.bin generator for Hak5 USB Rubber Duckies',
        '#8. Virus-Total Checker, safely check whether or not your custom payload is detectable without alerting Virus-Total and AV developers',
        '#9. Embed a custom made payload into a PDF file'

    ]

    print ("\n\t".join(opt_List))

    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "0":
        os.system('clear')
        main()
    elif opt_Choice == "1":
        os.system('clear')
        metasploit()
        # MT_host_recon()
    elif opt_Choice == "2":
        os.system('clear')
        armitage()
        # CornHarvester()
    elif opt_Choice == "3":
        os.system('clear')
        easy_peasey()
        # NMap_Auto()
    elif opt_Choice == "4":
        os.system('clear')
        veil_evasion()
        # NMap_Custom()
    elif opt_Choice == "5":
        os.system('clear')
        social_engineers_toolkit()
        # SQLMap()
    elif opt_Choice == "6":
        os.system('clear')
        pupy_menu()
        # OWASP_zaproxy()
    elif opt_Choice == "7":
        os.system('clear')
        DPMB()
    elif opt_Choice == "8":
        os.system('clear')
        VT_Checker()
        # burpsuite()
    elif opt_Choice == "9":
        os.system('clear')
        embed_payload_pdf()
    else:
        print 'You have entered a invalid option'
        three_remote_exploits()

def APK_Malware_Injection():
    os.system('python /root/ArmsCommander/mobiledevices/APKmalwareInjector.py')
    main()
    return

def DIAMONDSHARK():
    os.system('python /root/ArmsCommander/mobiledevices/DIAMOND_SHARK/DS_Menu.py')
    main()
    return

def four_mobile_dev_hacking():
    opt_List = [
        '\n\t#0 Return to Main Menu',
        '#1. Android APK file Malware Injection',
        '#2. DIAMONDSHARK, Easy-to-use readaption of the Stagefright Exploit (mp4 file, shellcode injection)'
     ]
    print ("\n\t".join(opt_List))

    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "0":
        main()
    elif opt_Choice == "1":
        APK_Malware_Injection()
    elif opt_Choice == "2":
        DIAMONDSHARK()
        # MT_host_recon()
    else:
        print 'You have entered a invalid option'
        four_mobile_dev_hacking()
    return

def cylon_raider():
    os.system('python /root/ArmsCommander/wirelessattacks/Cylon-Raider/Cylon_Raider_Main.py')
    main()
    return

def heavy_raider():
    os.system('python /root/ArmsCommander/wirelessattacks/Heavy-Raider/HeavyRaider.py')
    main()
    return

def router_sploit():
    opt_List = [
        '\n\t#0. Return to Main Menu',
        'INSTALL. Install the RouterSploit Framework',
        '#1. Run the RouterSploit Framework'
    ]

    print ("\n\t".join(opt_List))
    opt_Choice = str(raw_input("Enter a OPTION, or type INSTALL in all caps to install RouterSploit: "))

    if opt_Choice == "1":
        os.system('clear')
        os.system("gnome-terminal -e 'bash -c \"python /root/routersploit/rsf.py; exec bash\"'")
        main()
    elif opt_Choice == "INSTALL":
        os.system('clear')
        print 'Git Cloning RouterSploit into your Cylon-Raider Installation'
        os.system('cd /root')
        os.system('git clone https://github.com/reverse-shell/routersploit.git')
        print 'Routersploit install complete'
        main()
    return

def ARP_injection_test():
    os.system('airmon-ng start wlan1')
    cmd_String = "aireplay-ng -9 wlan1mon --ignore-negative-one"
    print cmd_String
    os.system(cmd_String)
    main()

    return

def hidden_network_decloaker():
    os.system('python /root/ArmsCommander/wirelessattacks/Cylon-Raider/sniffHidden.py')
    return

def five_wireless_attacks():
    opt_List = [
        '\n\t#0. Return to Main Menu',
        '#1. Cylon-Raider, automate wireless "Replay-Attacks" from the Aircrack-ng Suite',
        '#2. Cylon Heavy-Raider, automate the WPS PIN brute-forcing vulnerability with Reaver',
        '#3. Router-Sploit, Post-Exploitation hacking of APs that you cracked the passwords of',
        '#4. ARP Injection Test, seeing if your external wireless card is working properly',
        '#5. Hidden Network Decloaker, uncover hidden wireless APs'
    ]
    print ("\n\t".join(opt_List))

    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "0":
        os.system('clear')
        main()
    elif opt_Choice == "1":
        os.system('clear')
        cylon_raider()
        # MT_host_recon()
    elif opt_Choice == "2":
        os.system('clear')
        heavy_raider()
        # CornHarvester()
    elif opt_Choice == "3":
        os.system('clear')
        router_sploit()
        # NMap_Auto()
    elif opt_Choice == "4":
        os.system('clear')
        ARP_injection_test()
        # NMap_Custom()
    elif opt_Choice == "5":
        os.system('clear')
        hidden_network_decloaker()
        # SQLMap()
    else:
        print 'You have entered a invalid option'
        five_wireless_attacks()

def aircrack():
    os.system('python /root/ArmsCommander/wirelessattacks/Cylon-Raider/CrackHead_Aircrack.py')
    main()
    return

def six_password_attacks():
    opt_List = [
        '\n\t#0 Return to Main Menu',
        '#1. Aircrack-ng, crack captured WPA handshakes'
    ]
    print ("\n\t".join(opt_List))

    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "0":
        main()
    elif opt_Choice == "1":
        os.system('clear')
        aircrack()
        # MT_host_recon()
    else:
        print 'You have entered a invalid option'
        six_password_attacks()
    return

def Violent_Python_Menu():
    os.system('python /root/ArmsCommander/booklearning/Violent-Python-POCs/Violent_Python_Menu.py')
    main()
    return

def Black_Hat_Python_Menu():
    print 'In Construction, Check back soon!'
    main()
    return

def seven_book_learning():
    opt_List = [
        '\n\t#0. Return to Main Menu',
        '#1. Violent Python POCs',
        '#2. Black Hat Python POCs'
    ]
    print ("\n\t".join(opt_List))

    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "0":
        main()
    elif opt_Choice == "1":
        os.system('clear')
        Violent_Python_Menu()
    elif opt_Choice == "2":
        os.system('clear')
        Black_Hat_Python_Menu()
        # MT_host_recon()
    else:
        print 'You have entered a invalid option'
        seven_book_learning()
    return

def main():
    os.system('cat /root/ArmsCommander/banners/banner_mainmenu.txt\n\n')
    opt_List = [
        '\n\t#1. Reconnaissance Tools & Vulnerability Scanners',
        '#2. Network Defenses & Traffic Monitoring',
        '#3. Remote Exploitation/Hacking',
        '#4. Mobile Device Hacking',
        '#5. Wireless Attacks',
        '#6. Password Attacks',
        '#7. Book Learning'
    ]

    print ("\n\t".join(opt_List))

    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "1":
        os.system('clear')
        one_recon_and_vuln_scan()
    elif opt_Choice == "2":
        os.system('clear')
        two_net_defense_traffic_monitor()
    elif opt_Choice == "3":
        os.system('clear')
        three_remote_exploits()
    elif opt_Choice == "4":
        os.system('clear')
        four_mobile_dev_hacking()
    elif opt_Choice == "5":
        os.system('clear')
        five_wireless_attacks()
    elif opt_Choice == "6":
        os.system('clear')
        six_password_attacks()
    elif opt_Choice == "7":
        os.system('clear')
        seven_book_learning()
    else:
        print 'You have entered a invalid option'
        main()
    main()
    return
main()
