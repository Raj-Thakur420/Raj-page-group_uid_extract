import os
import requests
from colorama import Fore, init
from datetime import datetime, timedelta
import time
import hashlib
import uuid

# Initialize colorama for colored text output
init(autoreset=True)

# Approval system details
APPROVAL_URL = "https://github.com/Raj-Thakur420/Raj-page-group_uid_extract/blob/main/Approval.txt"  # Approval list link
WHATSAPP_NUMBER = "+919695003501"  # Your WhatsApp number

# Function to generate unique key
def generate_unique_key():
    unique_id = str(uuid.uuid4())  
    key = hashlib.sha256(unique_id.encode()).hexdigest()[:15]  
    return key

# Function to send unique key to WhatsApp automatically
def send_whatsapp_message(user_key):
    message = f"🔐 🖤⚔️ HELLO RAJ THAKUR SIR PLEASE MY APPROVAL KEY 🔐 : ANUSHKA ⚔️ RUHI RNDI KE BHAI AAYUSH CHUDWASTAV =>💋KE JIJU [= RAJ THAKUR SIR PLEASE MY APPROVAL KEY [❤️=]!\n\nUnique Key: {user_key}\nApprove this key to grant access."
    whatsapp_api = f"https://api.whatsapp.com/send?phone={WHATSAPP_NUMBER}&text={message}"
    
    print(Fore.YELLOW + "\n\033[1;97m\033[48;5;197m 🔄 Sending unique key to🟢💬'📱WhatsApp \033[0m\033[1;32m")
    time.sleep(2)  
    os.system(f"termux-open-url '{whatsapp_api}'")  
    print(Fore.GREEN + "\033[1;97m\033[48;5;178m ✅ Unique key sent successfully!\033[0m\033[1;32m\n")

# Function to check approval from GitHub link
def check_approval(user_key):
    try:
        response = requests.get(APPROVAL_URL)
        if response.status_code == 200:
            approved_keys = response.text.splitlines()
            return user_key in approved_keys
        else:
            return False
    except:
        return False

# Logo function
def show_logo():
    os.system('clear')  
    logo = """
\033[1;36m$$$$$$$\   $$$$$$\     $$$$$\ 
\033[1;36m$$  __$$\ $$  __$$\    \__$$ |
\033[1;34m$$ |  $$ |$$ /  $$ |      $$ |
\033[1;34m$$$$$$$  |$$$$$$$$ |      $$ |
\033[1;36m$$  __$$< $$  __$$ |$$\   $$ |
\033[1;32m$$ |  $$ |$$ |  $$ |$$ |  $$ |
\033[1;33m$$ |  $$ |$$ |  $$ |\$$$$$$  |
\033[1;33m\__|  \__|\__|  \__| \______/ 
 
          \033[1;33m $$$$$$\  $$$$$$\ $$\   $$\  $$$$$$\  $$\   $$\ 
         \033[1;33m$$  __$$\ \_$$  _|$$$\  $$ |$$  __$$\ $$ |  $$ |
         \033[1;36m$$ /  \__|  $$ |  $$$$\ $$ |$$ /  \__|$$ |  $$ |
         \033[1;36m\$$$$$$\    $$ |  $$ $$\$$ |$$ |$$$$\ $$$$$$$$ |
          \033[1;33m\____$$\   $$ |  $$ \$$$$ |$$ |\_$$ |$$  __$$ |
         \033[1;35m$$\   $$ |  $$ |  $$ |\$$$ |$$ |  $$ |$$ |  $$ |
         \033[1;36m\$$$$$$  |$$$$$$\ $$ | \$$ |\$$$$$$  |$$ |  $$ |
          \033[1;53m\______/ \______|\__|  \__| \______/ \__|  \__|
          
╔═════════════════════════════════════════════════════════════╗
║ \033[1;31mTOOLS      : ACTIVE GROUP UID 
║ \033[1;34mGitHub     : https://github.com/Raj-Thakur420
║ \033[1;32mWHATSAPP   : +919695003501
║ \033[1;82mTOOLS NAME : PAGE TOKEN EXTRACTOR
╚═════════════════════════════════════════════════════════════╝
    """
    print(Fore.YELLOW + logo)
    time.sleep(1)

# Function to fetch active Messenger groups
def get_active_messenger_groups(access_token):
    url = f'https://graph.facebook.com/v17.0/me/conversations?fields=name,updated_time&access_token={access_token}'  
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if 'data' in data:
            print(Fore.GREEN + "\nList of Active Messenger Groups:")
            now = datetime.utcnow()
            active_found = False

            for conversation in data['data']:
                conversation_id = conversation['id']
                conversation_name = conversation.get('name', None)
                updated_time = conversation.get('updated_time', None)

                if updated_time:
                    last_updated = datetime.strptime(updated_time, '%Y-%m-%dT%H:%M:%S%z').replace(tzinfo=None)
                    if now - last_updated <= timedelta(days=30):
                        active_found = True
                        if conversation_name:
                            print(Fore.GREEN + f"\033[1;91m\033[1;41m\033[1;33m\033[1;35m\033[1;37m Group Name\033[;0m\033[1;91m\033[1;92m\033[38;5;46m: {conversation_name} | Group UID: {conversation_id}")
                        else:
                            print(Fore.YELLOW + f"\033[1;92m\033[1;42m\033[1;37m Group UID \033[0m\033[1;92m\033[38;5;46m : {conversation_id} | Group Name: No Name Available")

            if not active_found:
                print(Fore.YELLOW + "No active Messenger groups found in the last 30 days.")
        else:
            print(Fore.YELLOW + "No Messenger groups found or unable to access group data.")
    else:
        print(Fore.RED + f"Error: {response.status_code}")
        print(response.text)

# Function to get token details
def get_token_details(access_token):
    url = f'https://graph.facebook.com/me?access_token={access_token}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if 'name' in data:
            print(Fore.GREEN + f"\nLogged in as: {data['name']} (User ID: {data['id']})")
        else:
            print(Fore.YELLOW + "Unable to retrieve user details from the access token.")
    else:
        print(Fore.RED + "Error: Invalid or expired token.")
        return False
    return True

# Function to fetch Page Tokens
def get_page_tokens(access_token):
    url = f'https://graph.facebook.com/v17.0/me/accounts?fields=name,access_token&access_token={access_token}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if 'data' in data:
            print(Fore.GREEN + "\nList of Pages and Their Access Tokens:")
            for page in data['data']:
                page_name = page.get('name', 'Unknown Page')
                page_token = page.get('access_token', 'No Token Available')
                print(Fore.GREEN + f"\033[1;97m\033[48;5;136m Page 🏳️ Name\033[0m\033[1;32m ===> {page_name} | " + Fore.LIGHTMAGENTA_EX + f"Page Access Token: {page_token}")  
        else:
            print(Fore.YELLOW + "No Pages found or unable to access page data.")
    else:
        print(Fore.RED + f"Error: {response.status_code}")
        print(response.text)

# Main function
def main():
    show_logo()
    user_key = generate_unique_key()
    print(Fore.CYAN + f"\n\033[1;97m\033[48;5;91m 🔐 Your Unique ⚔️ key \033[0m\033[1;32m ===> {user_key}")
    send_whatsapp_message(user_key)

    approved_key = input(Fore.BLUE + "\033[1;97m\033[48;5;89m Enter your approved 🔐 key \033[0m\033[1;32m ===>")
    if not check_approval(approved_key):
        print(Fore.RED + "❌ Access Denied!")
        exit()

    print(Fore.GREEN + "✅ Access Granted!\n")
    access_token = input(Fore.BLUE + "\033[1;97m\033[48;5;18m Enter your Facebook Access Token \033[0m\033[1;31m ===> ")

    if not get_token_details(access_token):
        exit()

    get_active_messenger_groups(access_token)
    get_page_tokens(access_token)

if __name__ == "__main__":
    main()
