import requests
import os
import argparse
import time as t
import socket
import ipaddress
import random
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Back, Style

red =  Fore.RED

green = Fore.GREEN

magenta = Fore.MAGENTA

cyan = Fore.CYAN

mixed = Fore.RED + Fore.BLUE

blue = Fore.BLUE

yellow = Fore.YELLOW

white = Fore.WHITE

reset = Style.RESET_ALL

colors = [green, cyan, blue]

random_color = random.choice(colors)


banner = f"""

                       _______                       
                      / ____(_)___  ___  _____                      
                     / /   / / __ \/ _ \/ ___/
                    / /___/ / /_/ /  __/ /                       
                    \____/_/ .___/\___/_/     
                          /_/                 
                           
                          
                          
                                 Author: D.Sanjai Kumar @CyberRevoltSecurities
                          
                           

"""

def check_version():
    
    version = "v1.0.0"
    
    url = f"https://api.github.com/repos/sanjai-AK47/Ciper/releases/latest"
    
    try:
        
        response = requests.get(url)
        
        if response.status_code == 200:
            
            data = response.json()
            
            latest = data.get('tag_name')
            
            if latest == version:
                
                
                print(f"[{blue}Version{reset}]: Ciper current version {version} ({green}latest{reset})")
                
                t.sleep(1)
                
                
            else:
                
                print(f"[{blue}Version{reset}]: Ciper current version {version} ({red}outdated{reset})")
                
                print(f"[{red}ALERT{reset}]: Ciper new version detected update to latest version of Ciper")
                
                t.sleep(1)
                
        else:
            
            pass
                
    except Exception as e:
        
        pass

def socket_network(ip):
    
    try:
            ip_string = str(ip)
            
            
            domain = socket.gethostbyaddr(ip_string)
            
            domain = domain[0]
            
            
            
            if args.verbose:
                
                
                print(f"[{green}INFO{reset}]: {domain} [{cyan}{ip}{reset}]")
            
            save(domain, ip)
            
            t.sleep(1)
            
            
    except Exception as e:
        
        if args.verbose:
            
            
            print(f"[{blue}INFO{reset}]: [{cyan}{ip}{reset}] - [{blue}No valid host found{reset}]")
            
            save_invalid(ip)
            
        if not args.verbose:
            
            save_invalid(ip)
            
            
    
    

def main_work(cidr):
    
    try:
        
        network = ipaddress.IPv4Network(cidr, strict=False)
        
        with ThreadPoolExecutor(max_workers=args.concurrent) as executor:
            
            futures = {executor.submit(socket_network, ip)for ip in network }
            
            
            
        
    except Exception as e:
        
        pass
        
        

def speed_call(cidr_notation):
    
    try:
    
        with ThreadPoolExecutor(max_workers=args.concurrent) as executor:
        
            futures = {executor.submit(main_work, cidr) for cidr in cidr_notation}
            
    except KeyboardInterrupt as e:
        
        print(f"[{cyan}INFO{reset}]: Ciper says BYE!")
        
        exit()
        
        
        
        
def save(domain, ip):
    
    if args.output:
        
        with open(args.output, "a") as w:
            
            w.write(f"{domain} - {ip}\n")
            
    else:
        
        filename = f"ciper_results.txt"
        
        with open(filename, "a") as w:
            
            w.write(f"{domain} - {ip}\n")
            
            
def save_invalid(ip):
    
    if args.output:
        
        with open(args.output, "a") as w:
            
            w.write(f"{ip} - No valid host found\n")
            
    else:
        
        filename = f"ciper_results.txt"
        
        with open(filename, "a") as w:
            
            w.write(f"{ip} - No valid host found \n")



parser = argparse.ArgumentParser(description=f"[{cyan}INFO{reset}]: CIPER Tool dig deep and found domains of the target organisation")

parser.add_argument("-s", "--single", help=f"[{cyan}INFO{reset}]: A single range of ip address with CIDR notation (eg:127.0.0.q/24)", type=str or int)

parser.add_argument("-f", "--filename", help=f"[{cyan}INFO{reset}]: File that contains range of ipaddress with CIDR notation", type=str or int)

parser.add_argument("-c", "--concurrent", help=f"[{cyan}INFO{reset}]: Conncurrent features for level up the process with multiple process", type=int, default=30)

parser.add_argument("-v", "--verbose", help=f"[{cyan}INFO{reset}]: Show the found domains from the cidr notations", action="store_true")

parser.add_argument("-o", "--output", help=f"[{cyan}INFO{reset}]: save the found domain from the network")

args = parser.parse_args()

def main():
    
    print(f"{random_color}{banner}{reset}")
    
    check_version()
    
    if args.single:
        
        
        
        if args.verbose:
            
            t.sleep(2)
            
            print(f"[{cyan}INFO{reset}]: Verbose enabled output will be shown to user")
            
        elif not args.verbose:
            
            t.sleep(2)
            
            print(f"[{red}ALERT{reset}]: Verbose not enabled output will be now shown to user")
            
        if args.concurrent:
            
            t.sleep(2)
            
            print(f"[{cyan}INFO{reset}]: Concurrent started to running with value of: {args.concurrent}")
            
        if not args.concurrent:
            
            t.sleep(2)
            
            print(f"[{red}ALERT{reset}]: Concurrent features running not enabled running with defaults value of: {args.concurrent}")
            
        
        t.sleep(5)
        
        cidr_notation = [args.single]
        
        speed_call(cidr_notation)
        
    elif args.filename:
        
        try:
            
            
            if args.verbose:
            
                t.sleep(2)
            
                print(f"[{cyan}INFO{reset}]: Verbose enabled output will be shown to user")
            
            elif not args.verbose:
            
                t.sleep(2)
            
                print(f"[{red}ALERT{reset}]: Verbose not enabled output will be now shown to user")
            
            if args.concurrent:
            
                t.sleep(2)
            
                print(f"[{cyan}INFO{reset}]: Concurrent started to running with value of: {args.concurrent}")
            
            if not args.concurrent:
            
                t.sleep(2)
            
                print(f"[{red}ALERT{reset}]: Concurrent features running not enabled running with defaults value of: {args.concurrent}")
        
            t.sleep(2)
            
            filename = args.filename
            
            temp_list = []
            
            with open(filename, "r") as e:
                
                cidrs = e.read().splitlines()
            
            for cidr in cidrs:
                
                cidr = [cidr]
                
                
                speed_call(cidr)
            
        except FileNotFoundError as e:
            
            print(f"{random_color}{banner}{reset}")
            
            print(f"[{red}ALERT{reset}]: Error occurred due to the {filename} file not found. Please check the path or if the file exists.")
            
            exit()
            
        except Exception as e:
            
            print(f"[{red}ALERT{reset}]: Ciper met with an  unknown error and If you face this error continuously report this Ciper's github page")
            
            
            
if __name__ == "__main__":
    
    main()