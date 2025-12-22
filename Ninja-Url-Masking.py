import sys
import time
import pyshorteners
from urllib.parse import urlparse
import re

# Rangi
R = '\033[31m'  # red
G = '\033[32m'  # green
C = '\033[36m'  # cyan
W = '\033[0m'   # white
Y = '\033[33m'  # yellow

def show_loading_screen():
    """Display an animated loading screen with varied messages"""
    frames = ["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷"]
    for _ in range(10):  # Loop for a few seconds
        for frame in frames:
            sys.stdout.write(f"\r{G}Processing... {frame}{W}")
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write("\r\033[K")  # Clear line after animation

# Taarifa zako mpya
creator = "Cyber Ninja"
instagram = 'https://www.instagram.com/cyberninja200/'
linkedin = 'linkedin.com/in/nobody-error-3a8534399'
youtube = 'https://www.youtube.com/@nobodyerror-q7w2n'
github = 'https://github.com/CyberNinja-Tz'

# Banner mpya ya Ninja-Url-Masking
banner = r'''
███╗   ██╗██╗███╗   ██╗     ██╗ █████╗     ██╗   ██╗██████╗ ██╗     
████╗  ██║██║████╗  ██║     ██║██╔══██╗    ██║   ██║██╔══██╗██║     
██╔██╗ ██║██║██╔██╗ ██║     ██║███████║    ██║   ██║██████╔╝██║     
██║╚██╗██║██║██║╚██╗██║██   ██║██╔══██║    ██║   ██║██╔══██╗██║     
██║ ╚████║██║██║ ╚████║╚█████╔╝██║  ██║    ╚██████╔╝██║  ██║███████╗
╚═╝  ╚═══╝╚═╝╚═╝  ╚═══╝ ╚════╝ ╚═╝  ╚═╝     ╚═════╝ ╚═╝  ╚═╝╚══════╝

███╗   ███╗ █████╗ ███████╗██╗  ██╗██╗███╗   ██╗ ██████╗ 
████╗ ████║██╔══██╗██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝ 
██╔████╔██║███████║███████╗█████╔╝ ██║██╔██╗ ██║██║  ███╗
██║╚██╔╝██║██╔══██║╚════██║██╔═██╗ ██║██║╚██╗██║██║   ██║
██║ ╚═╝ ██║██║  ██║███████║██║  ██╗██║██║ ╚████║╚██████╔╝
╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
        The Ultimate URL Masking Tool by Cyber Ninja
'''

def print_banners():
    """
    prints the program banners
    """
    print(f'{G}{banner}{W}\n')
    print(f'{G}╰➤ {C}Created by   : {W}{creator}')
    print(f'{G}╰➤ {C}Instagram    : {W}{instagram}')
    print(f'{G}╰➤ {C}LinkedIn     : {W}{linkedin}')
    print(f'{G}╰➤ {C}YouTube      : {W}{youtube}')
    print(f'{G}╰➤ {C}Github       : {W}{github}\n')

################
print_banners()

# Initialize the URL shorteners
s = pyshorteners.Shortener()

# Add the additional URL shortener to the list
shorteners = [
    s.tinyurl,
    s.dagd,
    s.clckru,
    s.osdb,
]

def mask_url(domain, keyword, url):
    parsed_url = urlparse(url)
    return f"{parsed_url.scheme}://{domain}-{keyword}@{parsed_url.netloc}{parsed_url.path}"

try:
    while True:
        web_url = input(f"{G}Enter the original link {W}(ex: https://www.ngrok.com): {W}")
        if re.match(r'^(https?://)[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(:\d{1,5})?(/.*)?$', web_url):
            break
        print(f"{R}Invalid URL format. Please provide a valid web URL.{W}")

    while True:
        custom_domain = input(f"\n{Y}Enter your custom domain {W}(ex: gmail.com): {W}")
        if re.match(r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', custom_domain):
            break
        print(f"{R}Invalid custom domain. Please provide a valid domain name.{W}")

    while True:
        phish = input(f"\n{Y}Enter phishing keywords {W}(ex: account, login): {W}")
        if " " not in phish and len(phish) <= 15:
            break
        print(f"{R}Phishing keywords should not contain spaces and must be under 15 characters.{W}")

    show_loading_screen()
    short_urls = []
    for i, shortener in enumerate(shorteners):
        try:
            short_url = shortener.short(web_url)
            short_urls.append(short_url)
        except pyshorteners.exceptions.ShorteningErrorException as e:
            print(f"{R}Error shortening URL with Shortener {i + 1}: {W}{str(e)}")
            continue
        except Exception as e:
            print(f"{R}An unexpected error occurred with Shortener {i + 1}: {W}{str(e)}")
            continue

    print(f"\n{R}Original URL:{W}", web_url, "\n")
    print(f"{G}[~] {G}Masked URL {Y}(using multiple shorteners):{W}")
    for i, short_url in enumerate(short_urls):
        masked_url = mask_url(custom_domain, phish, short_url)
        print(f"{G}╰➤ {C}Shortener {W} {i + 1}: {masked_url}")

except Exception as e:
    print(f"{R}An error occurred: {W}{str(e)}")
