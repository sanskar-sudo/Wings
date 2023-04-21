import requests
import concurrent.futures
import colorama
from colorama import Fore, Back, Style
from termcolor import colored
colorama.init()



ascii_text = r"""


██╗    ██╗██╗███╗   ██╗ ██████╗ ███████╗
██║    ██║██║████╗  ██║██╔════╝ ██╔════╝
██║ █╗ ██║██║██╔██╗ ██║██║  ███╗███████╗
██║███╗██║██║██║╚██╗██║██║   ██║╚════██║
╚███╔███╔╝██║██║ ╚████║╚██████╔╝███████║
 ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝
    ░░                                                  ░░    
    ████                                              ████    
    ██▓▓██                                          ██  ██    
    ██▓▓▓▓██                                      ██    ██    
██████▓▓▓▓▓▓██████████████████████████████████████      ██████
██░░░░░░▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░      ░░░░░░██
██▓▓▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒      ▒▒▒▒▒▒  ██
██▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒      ░░▒▒▒▒    ██
██░░▓▓▓▓▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒    ▒▒▒▒▒▒    ░░██
██░░▓▓▓▓▓▓▓▓▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒        ░░██
██░░▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒        ▒▒░░██
██▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒░░▒▒▒▒▒▒    ▒▒▒▒        ▒▒▒▒  ██
██▓▓▓▓▓▓▒▒▒▒▓▓▓▓▒▒▒▒▒▒▓▓▓▓▒▒▒▒░░▒▒▒▒    ▒▒▒▒▒▒    ▒▒▒▒      ██
██░░▓▓▓▓▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▓▓▒▒▒▒░░▒▒    ░░▒▒  ▒▒  ░░▒▒      ░░██
██▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓    ▒▒  ▒▒▒▒    ▒▒▒▒▒▒      ▒▒  ██
██▓▓▓▓▒▒▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▒▒      ▒▒▒▒▒▒      ▒▒▒▒      ▒▒    ██
██░░▓▓▓▓▒▒▒▒▓▓▒▒▓▓▒▒▒▒▓▓        ▒▒▒▒    ▒▒▒▒  ▒▒  ▒▒▒▒    ░░██
██░░▓▓▓▓▓▓▓▓▒▒▒▒▓▓▒▒▒▒      ░░░░▒▒▒▒  ░░▒▒    ▒▒▒▒        ░░██
██░░▒▒▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓    ▒▒▒▒░░  ▒▒▒▒▒▒    ▒▒▒▒        ▒▒░░██
██░░░░░░▓▓▓▓▓▓░░░░░░▓▓  ░░░░      ░░      ░░░░░░      ░░░░░░██
██░░▒▒▒▒▒▒▓▓▓▓░░▒▒▒▒▒▒▒▒▒▒      ░░▒▒    ░░    ▒▒    ░░▒▒▒▒░░██
██░░▓▓▓▓▒▒▒▒▓▓▒▒▓▓▓▓▓▓▒▒    ▒▒░░  ▒▒▒▒▒▒      ▒▒  ▒▒▒▒    ░░██
██░░▒▒▓▓▓▓▓▓▒▒▒▒▒▒▓▓▓▓    ▒▒      ▒▒▒▒      ▒▒▒▒▒▒      ▒▒░░██
██░░▒▒▓▓▓▓▓▓▓▓▒▒▓▓▒▒▓▓  ▒▒      ▒▒▒▒      ▒▒  ▒▒        ▒▒░░██
██░░▒▒▒▒▒▒▓▓▓▓▒▒▓▓▓▓▒▒▒▒    ▒▒░░  ▒▒    ▒▒    ▒▒    ▒▒▒▒▒▒░░██
██░░▒▒▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒  ▒▒      ▒▒▒▒▒▒      ▒▒▒▒▒▒▒▒  ▒▒░░██
██░░▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒▓▓  ▒▒      ▒▒▒▒      ▒▒▒▒▒▒        ▒▒░░██
██░░▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒░░    ▒▒░░▒▒▒▒    ░░▒▒  ▒▒      ▒▒▒▒░░██
██░░▒▒▒▒▒▒▒▒▓▓▒▒▓▓▓▓▓▓▒▒  ▒▒      ▒▒▒▒▒▒      ▒▒  ▒▒▒▒▒▒▒▒░░██
██░░▒▒▒▒▓▓▓▓▒▒▒▒▒▒▓▓▓▓  ▒▒      ▒▒▒▒        ▒▒▒▒▒▒    ▒▒▒▒░░██
██░░▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒░░  ▒▒▒▒░░▒▒▒▒    ░░▒▒▒▒      ░░▒▒▒▒░░██
██░░▒▒▒▒▒▒▒▒▓▓▓▓▒▒▓▓▓▓  ▒▒▒▒      ▒▒▒▒▒▒    ▒▒    ▒▒▒▒▒▒▒▒░░██
██░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒  ▒▒░░▒▒        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░██
██░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒    ▒▒    ░░▒▒▒▒      ▒▒▒▒▒▒▒▒░░██
██░░░░▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒      ░░▒▒▒▒      ▒▒    ▒▒▒▒▒▒▒▒░░░░██
██████░░░░▒▒▒▒▒▒▓▓▒▒▒▒    ▒▒▒▒░░        ▒▒▒▒  ▒▒▒▒▒▒░░░░██████
      ████░░░░▒▒▒▒▒▒    ░░          ▒▒░░▒▒▒▒▒▒▒▒░░░░████      
          ████░░░░▒▒      ▒▒    ▒▒▒▒▓▓▓▓▓▓▒▒░░░░████          
              ██      ▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓██              
            ██    ████░░░░▒▒▒▒░░▒▒▒▒░░░░████▓▓▓▓██            
          ██    ██    ████░░░░░░░░░░████    ██▓▓▓▓██          
        ████████          ████░░████          ████████        
                              ██                              




-CreatedBy- Sanskar AKA MedussA





""" 
print("")
print("")
print("")
print("")
print("")
print("")
lines = ascii_text.strip().split('\n')


# Split each line into two parts and apply colors
for line in lines:
    line_length = len(line)
    split_index = line_length // 2
    line_part1 = line[:split_index]
    line_part2 = line[split_index:]
    print(Fore.BLUE + line_part1 + Fore.WHITE + line_part2 + Style.RESET_ALL)









import os

def check_subdomain(subdomain, domain, wordlist, show_alive_only):
    url = f"https://{subdomain}.{domain}"

    try:
        response = requests.get(url)
        if response.status_code == 200 and len(response.text) > 0:
            message = colored("200 OK", "green")
            if not show_alive_only:
                message += f" ({response.headers['server']})"
            print(f"[+] Found: {url} - {message}")
        elif not show_alive_only:
            print(f"[-] {url} - {colored('down', 'red')}")
    except:
        if not show_alive_only:
            print(f"[-] {url} - {colored('down', 'red')}")

if __name__ == "__main__":
    domain = input("Enter the domain to scan: ")

    # Ask user if they want to change the wordlist file
    change_wordlist = input("Do you want to change the wordlist file? (y/n): ")
    if change_wordlist.lower() == 'y':
        # Take the file name as input and replace the current wordlist
        wordlist_file = input("Enter the new wordlist file name: ")
        if os.path.isfile(wordlist_file):
            with open(wordlist_file) as f:
                wordlist = [line.strip() for line in f]
        else:
            print("File not found. Using default wordlist.")
            with open("subdomains-top1million-5000.txt") as f:
                wordlist = [line.strip() for line in f]
    else:
        # Use the default wordlist
        with open("subdomains-top1million-5000.txt") as f:
            wordlist = [line.strip() for line in f]

    # Ask user if they want to show only alive subdomains
    show_alive_only = input("Do you want to show only alive subdomains? (y/n): ")
    if show_alive_only.lower() == 'y':
        show_alive_only = True
    else:
        show_alive_only = False

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        for subdomain in wordlist:
            executor.submit(check_subdomain, subdomain, domain, wordlist, show_alive_only)