#
#
#
#
# Chat DNMX - A product made for fun.
#
# CodClever Chat DNMX
#
# ©️ Copyright 2024 Arinjay Kumar
#
# Product by CodClever
#
# A part of Zodiac
#
# Dear Viwers, This is note to you that: Please credit me if you want to share or use this code in
# any type of medium.
#
# Enjoy!
#
#
#
#

from Crypto import Random # pip install crypto / pip install cryptography/ pip install pycryptodome
from Crypto.Cipher import AES # pip install crypto / pip istall cryptography/ pip install pycryptodome
import re # pip install bcrypt
import wikipedia  # pip install wikipedia
import datetime  # pip install datetime
import os  
import webbrowser  # pip install webbrowser
import sys 
from openai import OpenAI # pip install openai
import google.generativeai as genai # pip install google-generativeai
from groq import Groq # pip install groq
from mistralai.client import MistralClient # pip install mistralai
from mistralai.models.chat_completion import ChatMessage # pip install mistralai
import anthropic # pip install anthropic
import base64 
import requests # pip install requests
from dotenv import load_dotenv


def check_Existence_Of_ENV_File():
    if os.path.exists(".env"):
        print("")
    else:
        with open('.env', 'w+') as file:
            file.write("")
check_Existence_Of_ENV_File()


# Password Hashed and Encryped using Advanced Encryption Standard (AES) 256-bit Encryption - The Most strongest and most robust encryption standard that is commercially available today.# PKCS7 padding function
def pad(message):
    padding_length = AES.block_size - len(message) % AES.block_size
    padding = bytes([padding_length]) * padding_length
    return message + padding

# PKCS7 unpadding function
def unpad(padded_message):
    padding_length = padded_message[-1]
    return padded_message[:-padding_length]


# Encrypt function with AES-256 and PKCS7 padding
def encrypt(message, key):
    # Convert message to bytes if it's not already
    if isinstance(message, str):
        message = message.encode()

    # Apply padding
    padded_message = pad(message)

    # Generate a random initialization vector (IV)
    iv = Random.new().read(AES.block_size)

    # Create AES cipher object
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Encrypt the padded message
    encrypted_message = cipher.encrypt(padded_message)

    # Encode the result using base64 for easy storage/transfer
    return base64.b64encode(iv + encrypted_message)


# Decrypt function with AES-256 and PKCS7 padding removal
# def decrypt(encrypted_message, key):
#     # Decode the base64-encoded message
#     encrypted_message = base64.b64decode(encrypted_message)

#     # Extract the IV from the encrypted message
#     iv = encrypted_message[:AES.block_size]
    
#     # Extract the actual encrypted message
#     encrypted_message = encrypted_message[AES.block_size:]

#     # Create AES cipher object for decryption
#     cipher = AES.new(key, AES.MODE_CBC, iv)

#     # Decrypt the message and remove padding
#     padded_message = cipher.decrypt(encrypted_message)
    
#     return unpad(padded_message).decode()  # Decode to return the original message

def authentication():

    # Define the file path
    username_file_path = 'D:\\donotopenthisfolder\\Arinjay\\CONFIDENTIAL\\Zodiac\\ChatDNMX\\logs\\username_log.txt'

    # Ensure the directory exists, if not, create it
    os.makedirs(os.path.dirname(username_file_path), exist_ok=True)

    # Ensure the file exists, if not, create it
    if not os.path.exists(username_file_path):
        with open(username_file_path, "w") as u:
            # Write an empty string to create the file
            u.write("")


    # Define the file path
    password_file_path = 'D:\\donotopenthisfolder\\Arinjay\\CONFIDENTIAL\\Zodiac\\ChatDNMX\\logs\\password_log.txt'

    # Ensure the directory exists, if not, create it
    os.makedirs(os.path.dirname(password_file_path), exist_ok=True)

    # Ensure the file exists, if not, create it
    if not os.path.exists(password_file_path):
        with open(password_file_path, "w") as u:
            # Write an empty string to create the file
            u.write("")


    # Define the file path
    email_file_path = 'D:\\donotopenthisfolder\\Arinjay\\CONFIDENTIAL\\Zodiac\\ChatDNMX\\logs\\email_log.txt'

    # Ensure the directory exists, if not, create it
    os.makedirs(os.path.dirname(email_file_path), exist_ok=True)

    # Ensure the file exists, if not, create it
    if not os.path.exists(email_file_path):
        with open(email_file_path, "w") as u:
            # Write an empty string to create the file
            u.write("")


    # Define the file path
    exit_file_path = 'D:\\donotopenthisfolder\\Arinjay\\CONFIDENTIAL\\Zodiac\\ChatDNMX\\logs\\exit_log.txt'

    # Ensure the directory exists, if not, create it
    os.makedirs(os.path.dirname(exit_file_path), exist_ok=True)

    # Ensure the file exists, if not, create it
    if not os.path.exists(exit_file_path):
        with open(exit_file_path, "w") as u:
            # Write an empty string to create the file
            u.write("")


    # Prompt the user to enter their credentials
    my_list = ["logs/username_log.txt",
               "logs/password_log.txt",
               "logs/email_log.txt",
               "logs/exit_log.txt"]
    if len(my_list) == 0:
        None
    else:
        return

    username = input("Enter username: ")
    def validate_username(username):
        # Validate username length and characters
        return 1 <= len(username) <= 64 and username.isalnum() and username.islower()
    validate_username(username)

    email = input("Enter email: ")
    def validate_email(email):
        # Validate email format using a regular expression
        email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        return bool(email_pattern.match(email))
    validate_email(email)

    password = input("Enter password: ")
    def validate_password(password):
        # Validate password length and complexity
        return 8 <= len(password) <= 20 and password.isdigit()
    validate_password(password)

    confirm_password = input("Confirm password: ")

    def create_log_files():
        try:
            # Directory 
            directory = "logs"
            
            # Parent Directory path 
            parent_dir = ""
            
            # Path 
            path = os.path.join(parent_dir, directory) 
            
            # Create the directory 
            # 'logs' in 
            # 'C://' ("C" Directory)

            os.makedirs(path, exist_ok=True)  

            # Username
            load_dotenv()
            user_Key = os.getenv("user_Key")
            user_Message = username

            encrypted_username = encrypt(user_Message, user_Key)

            # Password
            load_dotenv()
            pass_Key = os.getenv("pass_Key")
            pass_Message = password

            encrypted_password = encrypt(pass_Message, pass_Key)

            # Email
            load_dotenv()
            email_Key = os.getenv("email_Key")
            email_Message = email

            encrypted_email = encrypt(email_Message, email_Key)


            with open("logs/username_log.txt", "wb") as file:
                file.write(encrypted_username)

            with open("logs/password_log.txt", "wb") as file:
                file.write(encrypted_password)

            with open("logs/email_log.txt", "wb") as file:
                file.write(encrypted_email)  

            with open("logs/exit_log.txt", "w+") as file:
                file.write("Singed Up/Signed In successfully!")
        except Exception:       
            print("Error: Unable to create log files.")


    create_log_files()  # Creates log files if they don't exist

    def user_sign_up_def():
        try:

            # Your validation and account creation logic here
            def validation():
                # Validate username
                if not validate_username(username):
                    raise ValueError("Invalid username. Username must be 1-64 characters long. Please try again by re-opening the app.")

                # Validate email
                if not validate_email(email):
                    raise ValueError("Invalid email address. Please try again by re-opening the app.")

                # Validate password
                if not validate_password(password):
                    raise ValueError(
                        "Invalid password. Password must be 8-20 characters long. Please try again by re-opening the app.")

                if password != confirm_password:
                    raise ValueError("Passwords do not match. Please try again by re-opening the app.")

            validation()

            print("Success", "Account successfully created.")
        except ValueError as ve:
            print("Error", f"Error: {ve}")
    
    user_sign_up_def()


authentication()

username_file_path = os.path.join(os.path.dirname(__file__), "logs", "username_log.txt")
password_file_path = os.path.join(os.path.dirname(__file__), "logs", "password_log.txt")
email_file_path = os.path.join(os.path.dirname(__file__), "logs", "email_log.txt")
exit_file_path = os.path.join(os.path.dirname(__file__), "logs", "exit_log.txt")

with open(username_file_path, "r") as u:
    username = u.read()

with open(password_file_path, "r") as p:
    password = p.read()

with open(email_file_path, "r") as e:
    email = e.read()

with open(exit_file_path, "r") as en:
    end = en.read()


# Greeting  :-

I = str(
    input(
        "ChatDNMX -> Hello! Welcome to ChatDNMX*  Press 'ENTER' key on your keyboard to continue  *    "
    )
)

# Introduction  :-

N = str(
    input("ChatDNMX -> I am ChatDNMX.    *  Press 'ENTER' key on your keyboard to continue  *    ")
)
T = str(
    input(
        "ChatDNMX -> An A.I. created by my founder which is Arinjay Kumar.    *  Press 'ENTER' key on your keyboard to "
        "continue  *    "
    )
)
R = str(
    input(
        "ChatDNMX -> I would be happy if you like to chat with me!    *  Press 'ENTER' key on your keyboard to "
        "continue  *"
        "  "
    )
)
O = str(
    input(
        "ChatDNMX -> I am meant to only chat with you.    *  Press 'ENTER' key on your keyboard to continue  *    "
    )
)
D = str(
    input(
        "ChatDNMX -> I have restrictions.    *  Press 'ENTER' key on your keyboard to continue  *    "
    )
)
U = str(
    input(
        "ChatDNMX -> *  Important Note  *  :-    *  Press 'ENTER' key on your keyboard to continue  *    "
    )
)
C = str(
    input(
        "ChatDNMX -> 1.) When asking any questions, do not use any type of punctuation marks when writing.    *  Press "
        "'ENTER' key on your keyboard to continue  *    "
    )
)
E = str(
    input(
        "ChatDNMX -> 2.) Press enter to continue.    *  Press"
        "'ENTER' key on your keyboard to continue  *    "
    )
)


# Chatting  :-


def wishMe():
    try:
        hour = int(datetime.datetime.now().hour)
        if 0 <= hour < 12:
            print("ChatDNMX -> Good Morning!")

        elif 12 <= hour < 18:
            print("ChatDNMX -> Good Afternoon!")

        else:
            print("ChatDNMX -> Good Evening!")
    except Exception:
        print("ChatDNMX -> Some problem occurred!")
        wishMe()


wishMe()

# Stage  -  1  :-

userinput1 = input("ChatDNMX -> Can I ask your name?  :  ")


def chat1():
    try:
        if "YES" in userinput1:
            userinput2 = input("ChatDNMX -> Ok. Write a name for yourself now  :  ")
            try:
                if userinput2 == "Arinjay":
                    print("ChatDNMX -> Your name is same as our founder i.e. Arinjay Kumar")
                elif userinput2 == "":
                    print("ChatDNMX -> Please write your preffered username:")
                elif userinput2 == "arinjay":
                    print("ChatDNMX -> Your name is same as our founder i.e. Arinjay Kumar")
                elif userinput2 == "Arinjay Kumar":
                    print("ChatDNMX -> Your name is same as our founder i.e. Arinjay Kumar")
                elif userinput2 == "arinjay kumar":
                    print("ChatDNMX -> Your name is same as our founder i.e. Arinjay Kumar")
                elif userinput2 == "Arinjay kumar":
                    print("ChatDNMX -> Your name is same as our founder i.e. Arinjay Kumar")
                elif userinput2 == "arinjay Kumar":
                    print("ChatDNMX -> Your name is same as our founder i.e. Arinjay Kumar")
            except Exception:
                print("ChatDNMX -> Some problem occurred!")
                chat1()
            print("ChatDNMX -> Hello, ", userinput2)
        elif "yes" in userinput1:
            userinput2 = input("ChatDNMX -> Ok. Please enter your name  :  ")
            try:
                if userinput2 == "Arinjay":
                    print("ChatDNMX -> Your name is same as our founder i.e. Arinjay Kumar")
                elif userinput2 == "":
                    print("ChatDNMX -> Please write your preffered username:")
                elif userinput2 == "arinjay":
                    print("ChatDNMX -> Your name is same as our founder i.e. Arinjay Kumar")
                elif userinput2 == "Arinjay Kumar":
                    print("ChatDNMX -> Your name is same as our founder i.e. Arinjay Kumar")
                elif userinput2 == "arinjay kumar":
                    print("ChatDNMX -> Your name is same as our founder i.e. Arinjay Kumar")
                elif userinput2 == "Arinjay kumar":
                    print("ChatDNMX -> Your name is same as our founder i.e. Arinjay Kumar")
                elif userinput2 == "arinjay Kumar":
                    print("ChatDNMX -> Your name is same as our founder i.e. Arinjay Kumar")
            except Exception:
                print("ChatDNMX -> Some problem occurred!")
                chat1()
            print("ChatDNMX -> Hello, ", userinput2)
        elif "Yes" in userinput1:
            userinput2 = input("ChatDNMX -> Ok. Please enter your name  :  ")
            try:
                if userinput2 == "Arinjay":
                    print("ChatDNMX -> Your name is same as our founder i.e. Arinjay Kumar")
                elif userinput2 == "":
                    print("ChatDNMX -> Please write your preffered username:")
                elif userinput2 == "arinjay":
                    print("ChatDNMX -> Your name is same as our founder i.e. Arinjay Kumar")
                elif userinput2 == "Arinjay Kumar":
                    print("ChatDNMX -> Your name is same as our founder i.e. Arinjay Kumar")
                elif userinput2 == "arinjay kumar":
                    print("ChatDNMX -> Your name is same as our founder i.e. Arinjay Kumar")
                elif userinput2 == "Arinjay kumar":
                    print("ChatDNMX -> Your name is same as our founder i.e. Arinjay Kumar")
                elif userinput2 == "arinjay Kumar":
                    print("ChatDNMX -> Your name is same as our founder i.e. Arinjay Kumar")
            except Exception:
                print("ChatDNMX -> Some problem occurred!")
                chat1()
            print("ChatDNMX -> Hello, ", userinput2)
        elif "yEs" in userinput1:
            userinput2 = input("ChatDNMX -> Ok. Please enter your name  :  ")
            try:
                if userinput2 == "Arinjay":
                    print("ChatDNMX -> Your name is same as our founder i.e. Arinjay Kumar")
                elif userinput2 == "":
                    print("ChatDNMX -> Please write your preffered username:")
                elif userinput2 == "arinjay":
                    print("ChatDNMX -> Your name is same as our founder i.e. Arinjay Kumar")
                elif userinput2 == "Arinjay Kumar":
                    print("ChatDNMX -> Your name is same as our founder i.e. Arinjay Kumar")
                elif userinput2 == "arinjay kumar":
                    print("ChatDNMX -> Your name is same as our founder i.e. Arinjay Kumar")
                elif userinput2 == "Arinjay kumar":
                    print("ChatDNMX -> Your name is same as our founder i.e. Arinjay Kumar")
                elif userinput2 == "arinjay Kumar":
                    print("ChatDNMX -> Your name is same as our founder i.e. Arinjay Kumar")
            except Exception:
                print("ChatDNMX -> Some problem occurred!")
                chat1()
            print("ChatDNMX -> Hello, ", userinput2)
        elif "yeS" in userinput1:
            userinput2 = input("ChatDNMX -> Ok. Please enter your name  :  ")
            try:
                if userinput2 == "Arinjay":
                    print("ChatDNMX -> Your name is same as our founder i.e. Arinjay Kumar")
                elif userinput2 == "":
                    print("ChatDNMX -> Please write your preffered username:")
                elif userinput2 == "arinjay":
                    print("ChatDNMX -> Your name is same as our founder i.e. Arinjay Kumar")
                elif userinput2 == "Arinjay Kumar":
                    print("ChatDNMX -> Your name is same as our founder i.e. Arinjay Kumar")
                elif userinput2 == "arinjay kumar":
                    print("ChatDNMX -> Your name is same as our founder i.e. Arinjay Kumar")
                elif userinput2 == "Arinjay kumar":
                    print("ChatDNMX -> Your name is same as our founder i.e. Arinjay Kumar")
                elif userinput2 == "arinjay Kumar":
                    print("ChatDNMX -> Your name is same as our founder i.e. Arinjay Kumar")
            except Exception:
                print("ChatDNMX -> Some problem occurred!")
                chat1()
            print("ChatDNMX -> Hello, ", userinput2)
        elif "YEs" in userinput1:
            userinput2 = input("ChatDNMX -> Ok. Please enter your name  :  ")
            try:
                if userinput2 == "Arinjay":
                    print("ChatDNMX -> Your name is same as our founder i.e. Arinjay Kumar")
                elif userinput2 == "":
                    print("ChatDNMX -> Please write your preffered username:")
                elif userinput2 == "arinjay":
                    print("ChatDNMX -> Your name is same as our founder i.e. Arinjay Kumar")
                elif userinput2 == "Arinjay Kumar":
                    print("ChatDNMX -> Your name is same as our founder i.e. Arinjay Kumar")
                elif userinput2 == "arinjay kumar":
                    print("ChatDNMX -> Your name is same as our founder i.e. Arinjay Kumar")
                elif userinput2 == "Arinjay kumar":
                    print("ChatDNMX -> Your name is same as our founder i.e. Arinjay Kumar")
                elif userinput2 == "arinjay Kumar":
                    print("ChatDNMX -> Your name is same as our founder i.e. Arinjay Kumar")
            except Exception:
                print("ChatDNMX -> Some problem occurred!")
                chat1()
            print("ChatDNMX -> Hello, ", userinput2)
        elif "yES" in userinput1:
            userinput2 = input("ChatDNMX -> Ok. Please enter your name  :  ")
            try:
                if userinput2 == "Arinjay":
                    print("ChatDNMX -> Your name is same as our founder i.e. Arinjay Kumar")
                elif userinput2 == "":
                    print("ChatDNMX -> Please write your preffered username:")
                elif userinput2 == "arinjay":
                    print("ChatDNMX -> Your name is same as our founder i.e. Arinjay Kumar")
                elif userinput2 == "Arinjay Kumar":
                    print("ChatDNMX -> Your name is same as our founder i.e. Arinjay Kumar")
                elif userinput2 == "arinjay kumar":
                    print("ChatDNMX -> Your name is same as our founder i.e. Arinjay Kumar")
                elif userinput2 == "Arinjay kumar":
                    print("ChatDNMX -> Your name is same as our founder i.e. Arinjay Kumar")
                elif userinput2 == "arinjay Kumar":
                    print("ChatDNMX -> Your name is same as our founder i.e. Arinjay Kumar")
            except Exception:
                print("ChatDNMX -> Some problem occurred!")
                chat1()
            print("ChatDNMX -> Hello, ", userinput2)
        elif "NO" in userinput1:
            input(
                "ChatDNMX -> Ok. Let's move on then.    *  Press 'ENTER' key on your keyboard to continue  *    "
            )
        elif "no" in userinput1:
            input(
                "ChatDNMX -> Ok. Let's move on then.    *  Press 'ENTER' key on your keyboard to continue  *    "
            )
        elif "No" in userinput1:
            input(
                "ChatDNMX -> Ok. Let's move on then.    *  Press 'ENTER' key on your keyboard to continue  *    "
            )
        elif "nO" in userinput1:
            input(
                "ChatDNMX -> Ok. Let's move on then.    *  Press 'ENTER' key on your keyboard to continue  *    "
            )
        else:
            input(
                "ChatDNMX -> Ok. That's not what I expected. I am assuming that you want to be anonymous.    *  Press "
                "'ENTER' key on your keyboard to continue"
                "*    "
            )
    except Exception:
        print("ChatDNMX -> Some problem occurred!")
        chat1()


chat1()

# Stage  -  2  (*  Important  *)  :-

chat_List = [
    "1. OpenAI's ChatGPT 3.5",
    "2. Google's Gemini 1.5 Pro Experimental",
    "3. Google's Gemma on Groq",
    "4. Meta's Llama 3 on Groq",
    "5. Anthropic's Claude 3 Opus",
    "6. Mistral's Mixtral AI",
    "7. Mistral's Mixtral AI on Groq",
    "8. Stability XL",
    "9. Or continue with ChatDNMX..."
]

print("Please write down the the name of the AI model which you want to use(The name of the AI model should be excatly written(no change to punctuation, capitilization, spaces, etc.))" 
    "or write the number of the option to select that specific AI.")
print(chat_List)

userinput3 = input("You -> ")

def chat_List_Def():
    if userinput3 == "OpenAI's ChatGPT 3.5" or userinput3 == 1:
        chatgpt()
    elif userinput3 == "Google's Gemini 1.5 Pro Experimental" or userinput3 == 2:
        gemini()
    elif userinput3 == "Google's Gemma on Groq" or userinput3 == 3:
        gemma()
    elif userinput3 == "Meta's Llama 3 on Groq" or userinput3 == 4:
        llama()
    elif userinput3 == "Anthropic's Claude 3 Opus" or userinput3 == 5:
        claude()    
    elif userinput3 == "Mistral's Mixtral AI" or userinput3 == 6:
        mixtral()    
    elif userinput3 == "Mistral's Mixtral AI on Groq" or userinput3 == 7:
        mixtral_Groq() 
    elif userinput3 == "Stability XL" or userinput3 == 8:
        stability()
    elif userinput3 == "Or continue with ChatDNMX..." or userinput3 == 9:
        chat2()
    else:
        print("ChatDNMX -> That is not what I expected!")
        print("ChatDNMX -> Please try again by restarting the application.")
        sys.exit()

chat_List_Def()


def chatgpt(): 
    def chat():

        print("Warning: ChatGPT can make mistakes. Check important info.")

        def check_API_Given_In_Past():
            if len("logs/chatgpt.txt") == 0:
                chatgpt_1()
            else:
                chatgpt_2()
        check_API_Given_In_Past()


        def chatgpt_1():
            input = input("Please enter your ChatGPT API Key from https://platform.openai.com/api-keys -> ") 

            location = open("logs/chatgpt.txt", "wb")

            with open("logs/chatgpt.txt", "wb") as file:
                file.write(encrypted_chatgpt)

            load_dotenv()
            save_Api_Key = os.getenv("chatgpt_key")
            user_Message = location.read()
            location.close()

            encrypted_chatgpt = encrypt(user_Message, save_Api_Key)

            load_dotenv()
            OpenAI.api_key = os.getenv("OpenAI.api_key")

            maininput = input("You -> ")

            client = OpenAI()

            # Choose the OpenAI's ChatGPT AI Model
            ai_model = input("Please choose the OpenAI's ChatGPT AI model you want to use(The name of the AI model should be excatly written(no change to punctuation, capitilization, spaces, etc.), from here: https://platform.openai.com/docs/models/overview) -> ")

            # Custom Instructions
            custom_instruction = input("Custom Instructions(Press the 'ENTER' key to skip) -> ")

            completion = client.chat.completions.create(
                model=ai_model,
                messages=[
                    {"role": "system", "content": custom_instruction}
                ],
                temperature=1,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )

            print("ChatGPT -> ", completion.choices[0].message)
        

        def chatgpt_2():
            api_location = open("logs/chatgpt.txt", "r+")

            OpenAI.api_key = api_location

            api_location.close()

            maininput = input("You -> ")

            client = OpenAI()

            completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."}
            ],
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )

            print("ChatGPT -> ", completion.choices[0].message)            


        def loop():
            if chat():
                chat()
                loop()
            else:
                chat()
                loop()


        loop()


def gemini():
    def chat():
            
        def check_API_Given_In_Past():
            if len("logs/gemini.txt") == 0:
                gemini_1()
            else:
                gemini_2()
        check_API_Given_In_Past()

        def gemini_1():
            maininput = input("Please enter your Gemini API Key from https://aistudio.google.com/app/prompts/new_chat -> ")    
            input = input("You -> ")

            print("""
            Gemini:        
            I am still under development, and there are many things that I do not know. If I don't know the answer to a question, I will say so honestly. I will also try to provide some context or resources that may help you find the answer yourself. For example, I might say something like "I'm not sure about that, but I can find out for you. Can you give me more information about what you're looking for?" or "I'm not familiar with that topic, but I can provide you with some links to relevant websites."

            I am always learning new things, and I am committed to providing accurate and helpful information to my users. If you ever notice that I have made a mistake, please feel free to let me know. I appreciate your feedback and will use it to improve my performance.
                    
            """)

            """
            Install the Google AI Python SDK

            At the command line, only need to run once to install the package via pip:
            
            $ pip install google-generativeai

            See the getting started guide for more information:
            https://ai.google.dev/gemini-api/docs/get-started/python
            """

            location = open("logs/gemini.txt", "wb")

            with open("logs/gemini.txt", "wb") as file:
                file.write(encrypted_gemini)

            load_dotenv()
            save_Api_Key = os.getenv("gemini_key")
            user_Message = location.read()
            location.close()

            encrypted_gemini = encrypt(user_Message, save_Api_Key)

            load_dotenv()
            genai.configure(api_key=os.environ[os.getenv("api_key")])

            # Create the model
            # Set up the model
            # See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
            generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
            }
            safety_settings = [
                {
                    "category": "HARM_CATEGORY_HARASSMENT",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
                },
                {
                    "category": "HARM_CATEGORY_HATE_SPEECH",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
                },
                {
                    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
                },
                {
                    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
                },
            ]

            model = genai.GenerativeModel(
                model_name="gemini-1.5-pro-exp-0801",
                safety_settings=safety_settings,
                generation_config=generation_config,
                # safety_settings = Adjust safety settings
                # See https://ai.google.dev/gemini-api/docs/safety-settings
            )

            chat_session = model.start_chat(
                history=[
                ]
            )

            response = chat_session.send_message(input)

            print("Gemini -> ", response.text)
            # print(chat_session.history)

        def gemini_2():  
            input = input("You -> ")

            print("""
                    
            I am still under development, and there are many things that I do not know. If I don't know the answer to a question, I will say so honestly. I will also try to provide some context or resources that may help you find the answer yourself. For example, I might say something like "I'm not sure about that, but I can find out for you. Can you give me more information about what you're looking for?" or "I'm not familiar with that topic, but I can provide you with some links to relevant websites."

            I am always learning new things, and I am committed to providing accurate and helpful information to my users. If you ever notice that I have made a mistake, please feel free to let me know. I appreciate your feedback and will use it to improve my performance.
                    
            """)

            """
            Install the Google AI Python SDK

            At the command line, only need to run once to install the package via pip:
            
            $ pip install google-generativeai

            See the getting started guide for more information:
            https://ai.google.dev/gemini-api/docs/get-started/python
            """

            api_location = open("logs/gemini.txt", "r+")

            genai.configure(api_key=os.environ[api_location])

            api_location.close()

            # Create the model
            # Set up the model
            # See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
            generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
            }
            safety_settings = [
                {
                    "category": "HARM_CATEGORY_HARASSMENT",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
                },
                {
                    "category": "HARM_CATEGORY_HATE_SPEECH",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
                },
                {
                    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
                },
                {
                    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
                },
            ]

            model = genai.GenerativeModel(
                model_name="gemini-1.5-pro-exp-0801",
                safety_settings=safety_settings,
                generation_config=generation_config,
            )

            chat_session = model.start_chat(
                history=[
                ]
            )

            response = chat_session.send_message(input)

            print("Gemini -> ", response.text)
            # print(chat_session.history)
            

    def loop():
        if chat():
            chat()
            loop()
        else:
            chat()
            loop()


    loop()


def gemma():
    def chat():
            
        def check_API_Given_In_Past():
            if len("logs/gemma.txt") == 0:
                gemma_1()
            else:
                gemma_2()
        check_API_Given_In_Past()

        def gemma_1():
            maininput = "Please enter your Groq API Key from https://console.groq.com/keys -> "
            input = input("You -> ")

            location = open("logs/gemma.txt", "wb")

            with open("logs/gemma.txt", "wb") as file:
                file.write(encrypted_gemma)

            load_dotenv()
            save_Api_Key = os.getenv("gemma_key")
            user_Message = location.read()
            location.close()

            encrypted_gemma = encrypt(user_Message, save_Api_Key)

            load_dotenv()
            client = Groq(
                    gemma_api_key=os.environ.get(os.getenv("gemma_api_key")),
                )
            
            chat_completion = client.chat.completions.create(
                model="gemma-7b-it",
                messages=[
                    {
                        "role": "user",
                        "content": input
                    }
                ],
                temperature=1,
                max_tokens=1024,
                top_p=1,
                stream=True,
                stop=None,
            )

            for chunk in chat_completion:
                print("Gemma -> ", chunk.choices[0].delta.content or "", end="")

        def gemma_2():
            input = input("You -> ")

            api_location = open("logs/gemma.txt", "r+")

            client = Groq(
                    gemma_api_key=os.environ.get(api_location),
                )
            
            api_location.close()
            
            chat_completion = client.chat.completions.create(
                model="gemma-7b-it",
                messages=[
                    {
                        "role": "user",
                        "content": input
                    }
                ],
                temperature=1,
                max_tokens=1024,
                top_p=1,
                stream=True,
                stop=None,
            )

            for chunk in chat_completion:
                print("Gemma -> ", chunk.choices[0].delta.content or "", end="")

    def loop():
        if chat():
            chat()
            loop()
        else:
            chat()
            loop()


    loop()


def llama():
    def chat():

        def check_API_Given_In_Past():
            if len("logs/llama.txt") == 0:
                llama_1()
            else:
                llama_2()
        check_API_Given_In_Past()        
            
        def llama_1():    
            maininput = "Please enter your Groq API Key from https://console.groq.com/keys -> "
            input = input("You -> ")  

            location = open("logs/llama.txt", "wb")

            with open("logs/llama.txt", "wb") as file:
                file.write(encrypted_llama)

            load_dotenv()
            save_Api_Key = os.getenv("llama_key")
            user_Message = location.read()
            location.close()

            encrypted_llama = encrypt(user_Message, save_Api_Key)       

            load_dotenv()
            client = Groq(
                    llama_api_key=os.environ.get(os.getenv("llama_api_key")),
                )
            completion = client.chat.completions.create(
                model="llama3-70b-8192",
                messages=[
                    {
                        "role": "user",
                        "content": input
                    }
                ],
                temperature=1,
                max_tokens=1024,
                top_p=1,
                stream=True,
                stop=None,
            )

            for chunk in completion:
                print("Llama -> ", chunk.choices[0].delta.content or "", end="")
        def llama_2():
            input = input("You -> ")  

            api_location = open("logs/llama.txt", "r+")

            client = Groq(
                    llama_api_key=os.environ.get(api_location),
                )
            
            api_location.close()

            completion = client.chat.completions.create(
                model="llama3-70b-8192",
                messages=[
                    {
                        "role": "user",
                        "content": input
                    }
                ],
                temperature=1,
                max_tokens=1024,
                top_p=1,
                stream=True,
                stop=None,
            )

            for chunk in completion:
                print("Llama -> ", chunk.choices[0].delta.content or "", end="")            

    def loop():
        if chat():
            chat()
            loop()
        else:
            chat()
            loop()


    loop()


def claude():
    def chat():

        def check_API_Given_In_Past():
            if len("logs/claude.txt") == 0:
                claude_1()
            else:
                claude_2()
        check_API_Given_In_Past()
            
        def claude_1():
            maininput = input("Please enter your Claude API Key from https://console.anthropic.com/settings/keys -> ")
            
            location = open("logs/claude.txt", "wb")

            with open("logs/claude.txt", "wb") as file:
                file.write(encrypted_claude)

            load_dotenv()
            save_Api_Key = os.getenv("claude_key")
            user_Message = location.read()
            location.close()

            encrypted_claude = encrypt(user_Message, save_Api_Key)

            load_dotenv()
            client = anthropic.Anthropic(
                # defaults to os.environ.get("ANTHROPIC_API_KEY")
                claude_api_key=os.getenv("claude_api_key"),
            )

            message = client.messages.create(
                model="claude-3-opus-20240229",
                max_tokens=1000,
                temperature=0,
                messages=[]
            )
            print("Claude -> ", message.content)
        
        def claude_2():            

            api_location = open("logs/claude.txt", "r+")

            client = anthropic.Anthropic(
                # defaults to os.environ.get("ANTHROPIC_API_KEY")
                claude_api_key=os.getenv("claude_api_key"),
            )

            api_location.close()

            message = client.messages.create(
                model="claude-3-opus-20240229",
                max_tokens=1000,
                temperature=0,
                messages=[]
            )
            print("Claude -> ", message.content)            

    def loop():
        if chat():
            chat()
            loop()
        else:
            chat()
            loop()


    loop()


def mixtral():
    def chat():
            
        def check_API_Given_In_Past():
            if len("logs/gemma.txt") == 0:
                mixtral_1()
            else:
                mixtral_2()
        check_API_Given_In_Past()

        def mixtral_1():
            maininput = input("Please enter your Mistral API Key from https://console.mistral.ai/api-keys/ -> ")
            input = input("You -> ")

            location = open("logs/mixtral.txt", "wb")

            with open("logs/mixtral.txt", "wb") as file:
                file.write(encrypted_mixtral)

            load_dotenv()
            save_Api_Key = os.getenv("mixtral_key")
            user_Message = location.read()
            location.close()

            encrypted_mixtral = encrypt(user_Message, save_Api_Key)

            load_dotenv()
            mixtral_api_key = os.environ[os.getenv("mixtral_api_key")]
            model = "mistral-large-latest"

            client = MistralClient(api_key=mixtral_api_key)

            chat_response = client.chat(
                model=model,
                messages=[ChatMessage(role="user", content=input)]
            )

            print("Mistral AI -> ", chat_response.choices[0].message.content)

        def mixtral_2():
            input = input("You -> ")

            api_location = open("logs/mixtral.txt", "r+")
 
            mixtral_api_key = os.environ[api_location]
            model = "mistral-large-latest"

            api_location.close()

            client = MistralClient(api_key=mixtral_api_key)

            chat_response = client.chat(
                model=model,
                messages=[ChatMessage(role="user", content=input)]
            )

            print("Mistral AI -> ", chat_response.choices[0].message.content)

    def loop():
        if chat():
            chat()
            loop()
        else:
            chat()
            loop()


    loop()


def mixtral_Groq():
    def chat():
            
        def check_API_Given_In_Past():
            if len("logs/mixtral_groq.txt") == 0:
                mixtral_groq_1()
            else:
                mixtral_groq_2()
        check_API_Given_In_Past()

        def mixtral_groq_1():
            maininput = "Please enter your Groq API Key from https://console.groq.com/keys -> "
            input = input("You -> ")

            location = open("logs/mixtral_groq.txt", "wb")

            with open("logs/mixtral_groq.txt", "wb") as file:
                file.write(encrypted_mixtral_groq)

            load_dotenv()
            save_Api_Key = os.getenv("mixtral_groq_key")
            user_Message = location.read()
            location.close()

            encrypted_mixtral_groq = encrypt(user_Message, save_Api_Key)

            load_dotenv()
            client = Groq(
                    mixtral_groq_api_key=os.environ.get(os.getenv("mixtral_groq_api_key")),
                )
            completion = client.chat.completions.create(
                model="mixtral-8x7b-32768",
                messages=[
                    {
                        "role": "user",
                        "content": input
                    }
                ],
                temperature=1,
                max_tokens=1024,
                top_p=1,
                stream=True,
                stop=None,
            )

            for chunk in completion:
                print("Mistral On Groq -> ", chunk.choices[0].delta.content or "", end="")

        def mixtral_groq_2():
            input = input("You -> ")

            api_location = open("logs/mixtral_groq.txt", "r+")

            client = Groq(
                    mixtral_groq_api_key=os.environ.get(api_location),
                )
            
            api_location.close()

            completion = client.chat.completions.create(
                model="mixtral-8x7b-32768",
                messages=[
                    {
                        "role": "user",
                        "content": input
                    }
                ],
                temperature=1,
                max_tokens=1024,
                top_p=1,
                stream=True,
                stop=None,
            )

            for chunk in completion:
                print("Mistral On Groq -> ", chunk.choices[0].delta.content or "", end="")

    def loop():
        if chat():
            chat()
            loop()
        else:
            chat()
            loop()


    loop()


def stability():
    def chat():
            
        def check_API_Given_In_Past():
            if len("logs/stability.txt") == 0:
                stability_1()
            else:
                stability_2()
        check_API_Given_In_Past()

        def stability_1():
            url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"

            maininput = input("Please enter your Stability API Key from https://platform.stability.ai/account/keys -> ")

            input = input("Your prompt -> ")
            input2 = input("How you want it to look like? Separate your options by a comma -> ")

            text_Prompt = input
            prompt_type = input2

            body = {
            "steps": 40,
            "width": 1024,
            "height": 1024,
            "seed": 0,
            "cfg_scale": 5,
            "samples": 1,
            "text_prompts": [
                {
                "text": text_Prompt,
                "weight": 1
                },
                {
                "text": prompt_type,
                "weight": -1
                }
            ],
            }

            location = open("logs/stability.txt", "wb")

            with open("logs/stability.txt", "wb") as file:
                file.write(encrypted_stability)

            load_dotenv()
            save_Api_Key = os.getenv("stability_key")
            user_Message = location.read()
            location.close()

            encrypted_stability = encrypt(user_Message, save_Api_Key)

            load_dotenv()
            headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": os.getenv("Authorization"),
            }

            response = requests.post(
            url,
            headers=headers,
            json=body,
            )

            if response.status_code != 200:
                raise Exception("Non-200 response: " + str(response.text))

            data = response.json()

            # make sure the out directory exists
            if not os.path.exists("./output"):
                os.makedirs("./output")

            for i, image in enumerate(data["artifacts"]):
                with open(f'./output/tti_{image["seed"]}.png', "wb") as f:
                    f.write(base64.b64decode(image["base64"]))

            print("Stability XL -> Finished, check this directory.")

        def stability_2():
            url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"

            input = input("Your prompt -> ")
            input2 = input("How you want it to look like? Separate your options by a comma -> ")

            text_Prompt = input
            prompt_type = input2

            body = {
            "steps": 40,
            "width": 1024,
            "height": 1024,
            "seed": 0,
            "cfg_scale": 5,
            "samples": 1,
            "text_prompts": [
                {
                "text": text_Prompt,
                "weight": 1
                },
                {
                "text": prompt_type,
                "weight": -1
                }
            ],
            }

            api_location = open("logs/stability.txt", "r+")

            headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": api_location,
            }

            api_location.close()

            response = requests.post(
            url,
            headers=headers,
            json=body,
            )

            if response.status_code != 200:
                raise Exception("Non-200 response: " + str(response.text))

            data = response.json()

            # make sure the out directory exists
            if not os.path.exists("./output"):
                os.makedirs("./output")

            for i, image in enumerate(data["artifacts"]):
                with open(f'./output/tti_{image["seed"]}.png', "wb") as f:
                    f.write(base64.b64decode(image["base64"]))

            print("Stability XL -> Finished, check this directory.")  


    def loop():
        if chat():
            chat()
            loop()
        else:
            chat()
            loop()


    loop()


def chat2():
    query = userinput3
    try:
        if "Wikipedia" in query:
            try:
                print("ChatDNMX -> Finding...")
                query = query.replace("Wikipedia", "")
                results = wikipedia.summary(query)
                print("ChatDNMX -> According to Wikipedia : ")
                print(results)
            except Exception:
                print("ChatDNMX -> Sorry, I don't know that.")
        if "wikipedia" in query:
            try:
                print("ChatDNMX -> Finding...")
                query = query.replace("Wikipedia", "")
                results = wikipedia.summary(query)
                print("ChatDNMX -> According to Wikipedia : ")
                print(results)
            except Exception:
                print("ChatDNMX -> Sorry, I don't know that.")
        elif "What" in query:
            try:
                print("ChatDNMX -> Finding...")
                query = query.replace("Wikipedia", "")
                results = wikipedia.summary(query)
                print("ChatDNMX -> According to Wikipedia : ")
                print(results)
            except Exception:
                print("ChatDNMX -> Sorry, I don't know that.")
        elif "what" in query:
            try:
                print("ChatDNMX -> Finding...")
                query = query.replace("Wikipedia", "")
                results = wikipedia.summary(query)
                print("ChatDNMX -> According to Wikipedia : ")
                print(results)
            except Exception:
                print("ChatDNMX -> Sorry, I don't know that.")
        elif "Who" in query:
            try:
                print("ChatDNMX -> Finding...")
                query = query.replace("Wikipedia", "")
                results = wikipedia.summary(query)
                print("ChatDNMX -> According to Wikipedia : ")
                print(results)
            except Exception:
                print("ChatDNMX -> Sorry, I don't know that.")
        elif "who" in query:
            try:
                print("ChatDNMX -> Finding...")
                query = query.replace("Wikipedia", "")
                results = wikipedia.summary(query)
                print("ChatDNMX -> According to Wikipedia : ")
                print(results)
            except Exception:
                print("ChatDNMX -> Sorry, I don't know that.")
        elif "Why" in query:
            try:
                print("ChatDNMX -> Finding...")
                query = query.replace("Wikipedia", "")
                results = wikipedia.summary(query)
                print("ChatDNMX -> According to Wikipedia : ")
                print(results)
            except Exception:
                print("ChatDNMX -> Sorry, I don't know that.")
        elif "why" in query:
            try:
                print("ChatDNMX -> Finding...")
                query = query.replace("Wikipedia", "")
                results = wikipedia.summary(query)
                print("ChatDNMX -> According to Wikipedia : ")
                print(results)
            except Exception:
                print("ChatDNMX -> Sorry, I don't know that.")
        elif "When" in query:
            try:
                print("ChatDNMX -> Finding...")
                query = query.replace("Wikipedia", "")
                results = wikipedia.summary(query)
                print("ChatDNMX -> According to Wikipedia : ")
                print(results)
            except Exception:
                print("ChatDNMX -> Sorry, I don't know that.")
        elif "when" in query:
            try:
                print("ChatDNMX -> Finding...")
                query = query.replace("Wikipedia", "")
                results = wikipedia.summary(query)
                print("ChatDNMX -> According to Wikipedia : ")
                print(results)
            except Exception:
                print("ChatDNMX -> Sorry, I don't know that.")
        elif "How" in query:
            try:
                print("ChatDNMX -> Finding...")
                query = query.replace("Wikipedia", "")
                results = wikipedia.summary(query)
                print("ChatDNMX -> According to Wikipedia : ")
                print(results)
            except Exception:
                print("ChatDNMX -> Sorry, I don't know that.")
        elif "how" in query:
            try:
                print("ChatDNMX -> Finding...")
                query = query.replace("Wikipedia", "")
                results = wikipedia.summary(query)
                print("ChatDNMX -> According to Wikipedia : ")
                print(results)
            except Exception:
                print("ChatDNMX -> Sorry, I don't know that.")
        elif "what is my name" in query:
            try: 
                print("Your name is ", userinput1)
            except Exception:
                print("ChatDNMX -> Sorry, I don't know that.")
        elif "who am i" in query:
            try: 
                print("You are ", userinput1)
            except Exception:
                print("ChatDNMX -> Sorry, I don't know that.")
        elif "whoami" in query:
            try: 
                print("You are ", userinput1)
            except Exception:
                print("ChatDNMX -> Sorry, I don't know that.")

        #  Compliments  :-

        elif "hello" in query:
            print("ChatDNMX -> Hi there, Thanks for your comment, How can I help you?")
        elif "Hello" in query:
            print("ChatDNMX -> Hi there, Thanks for your comment, How can I help you?")
        elif "hallo" in query:
            print("ChatDNMX -> Hi there, Thanks for your comment, How can I help you?")
        elif "Hallo" in query:
            print("ChatDNMX -> Hi there, Thanks for your comment, How can I help you?")
        elif query == "hello":
            print("ChatDNMX -> Hi there, How may I help?")
        elif query == "hi" or query == "hii" or query == "hiiii":
            print("ChatDNMX -> Hi there, What can I do for you?")
        elif query == "how are you":
            print("ChatDNMX -> I am fine! And you?")
        elif query == "fine" or query == "i am good" or query == "i am doing good":
            print("ChatDNMX -> Great! How may I help you?")
        elif query == "thanks" or query == "thank you" or query == "now its my time":
            print("ChatDNMX -> My pleasure !")
        elif query == "what do you sell" or query == "what kinds of items are there" or query == "have you something":
            print("ChatDNMX -> We have coffee and tea here...")
        elif query == "tell me a joke" or query == "tell me something funny" or query == "crack a funny line":
            print(
                "ChatDNMX -> What did the buffalo say when his son left for college?")
            print(
                " Bison! ")

        # Recommendation : Add your custom websites here!

        elif "open youtube" in query:
            print("ChatDNMX -> Opening Youtube...")
            webbrowser.open("https://www.youtube.com")
        elif "open YouTube" in query:
            print("ChatDNMX -> Opening Youtube...")
            webbrowser.open("https://www.youtube.com")
        elif "Open youtube" in query:
            print("ChatDNMX -> Opening Youtube...")
            webbrowser.open("https://www.youtube.com")
        elif "Open YouTube" in query:
            print("ChatDNMX -> Opening Youtube...")
            webbrowser.open("https://www.youtube.com")
        elif "open google" in query:
            print("ChatDNMX -> Opening Google...")
            webbrowser.open("https://www.google.com")
        elif "open Google" in query:
            print("ChatDNMX -> Opening Google...")
            webbrowser.open("https://www.google.com")
        elif "Open google" in query:
            print("ChatDNMX -> Opening Google...")
            webbrowser.open("https://www.google.com")
        elif "Open Google" in query:
            print("ChatDNMX -> Opening Google...")
            webbrowser.open("https://www.google.com")
        elif "open stackoverflow" in query:
            print("ChatDNMX -> Opening Stack Overflow...")
            webbrowser.open("https://www.stackoverflow.com")
        elif "open StackOverflow" in query:
            print("ChatDNMX -> Opening Stack Overflow...")
            webbrowser.open("https://www.stackoverflow.com")
        elif "open stack overflow" in query:
            print("ChatDNMX -> Opening Stack Overflow...")
            webbrowser.open("https://www.stackoverflow.com")
        elif "open Stack Overflow" in query:
            print("ChatDNMX -> Opening Stack Overflow...")
            webbrowser.open("https://www.stackoverflow.com")
        elif "Open stackoverflow" in query:
            print("ChatDNMX -> Opening Stack Overflow...")
            webbrowser.open("https://www.stackoverflow.com")
        elif "Open StackOverflow" in query:
            print("ChatDNMX -> Opening Stack Overflow...")
            webbrowser.open("https://www.stackoverflow.com")
        elif "Open Stack Overflow" in query:
            print("ChatDNMX -> Opening Stack Overflow...")
            webbrowser.open("https://www.stackoverflow.com")
        elif "Open stack overflow" in query:
            print("ChatDNMX -> Opening Stack Overflow...")
            webbrowser.open("https://www.stackoverflow.com")
        elif "open wikipedia" in query:
            print("ChatDNMX -> Opening Wikipedia...")
            webbrowser.open("https://www.wikipedia.com")
        elif "Open wikipedia" in query:
            print("ChatDNMX -> Opening Wikipedia...")
            webbrowser.open("https://www.wikipedia.com")
        elif "open Wikipedia" in query:
            print("ChatDNMX -> Opening Wikipedia...")
            webbrowser.open("https://www.wikipedia.com")
        elif "Open Wikipedia" in query:
            print("ChatDNMX -> Opening Wikipedia...")
            webbrowser.open("https://www.wikipedia.com")

        elif "Open facebook" in query:
            print("ChatDNMX -> Opening Facebook...")
            webbrowser.open("https://www.facebook.com")

        elif "Open Facebook" in query:
            print("ChatDNMX -> Opening Facebook...")
            webbrowser.open("https://www.facebook.com")

        elif "open facebook" in query:
            print("ChatDNMX -> Opening Facebook...")
            webbrowser.open("https://www.facebook.com")

        elif "open Facebook" in query:
            print("ChatDNMX -> Opening Facebook...")
            webbrowser.open("https://www.facebook.com")

        elif "play music" in query:
            input = input("ChatDNMX -> Please write the music directory location to play music -> ")
            print("ChatDNMX -> Opening Music...")
            music_dir = input
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif "open music" in query:
            input = input("ChatDNMX -> Please write the music directory location to play music -> ")
            print("ChatDNMX -> Opening Music...")
            musicPath = (input)
            os.system(f"open {musicPath}")
        elif "what is the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"ChatDNMX -> Sir, the time is : {strTime}")

        elif "open code" or "open visual studio code" or "open vs code" or "open Visual Studio Code" in query:
            input = input("ChatDNMX -> Please write the Visual Studio Code directory location to open Visual Studio Code -> ")
            print("ChatDNMX -> Opening Visual Studio Code...")
            codePath = input
            os.startfile(codePath)
        elif "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            print(f"ChatDNMX -> Sir/Madam, the current time is {hour}:{min}")

        elif "open facetime".lower() in query.lower():
            input = input("ChatDNMX -> Please write the Facetime directory location to open Facetime -> ")
            print("ChatDNMX -> Opening Facetime...")
            os.system(input)

        elif "open pass".lower() in query.lower():
            input = input("ChatDNMX -> Please write the Passkey directory location to open Passkey -> ")
            print("ChatDNMX -> Opening Passkey...")
            os.system(input)
        elif query == "goodbye" or query == "see you later" or query == "see yaa":
            print("ChatDNMX -> Have a nice day!")
        elif "quit" in query:
            try:
                input1 = input("ChatDNMX -> Are you sure you wanna quit?  :  ")
                if input1 == "NO":
                    print("ChatDNMX -> Ok...")
                    chat2()
                if input1 == "no":
                    print("ChatDNMX -> Ok...")
                    chat2()
                if input1 == "No":
                    print("ChatDNMX -> Ok...")
                    chat2()
                if input1 == "nO":
                    print("ChatDNMX -> Ok...")
                    chat2()
            except Exception:
                print("ChatDNMX -> Sorry, I don't know that.")
        elif "exit" in query:
            try:
                input2 = input("ChatDNMX -> Are you sure you wanna quit?  :  ")
                if input2 == "NO":
                    print("ChatDNMX -> Ok...")
                    chat2()
                if input2 == "no":
                    print("ChatDNMX -> Ok...")
                    chat2()
                if input2 == "No":
                    print("ChatDNMX -> Ok...")
                    chat2()
                if input2 == "nO":
                    print("ChatDNMX -> Ok...")
                    chat2()
            except Exception:
                print("ChatDNMX -> Sorry, I don't know that.")
        elif "get out" in query:
            try:
                input3 = input("ChatDNMX -> Are you sure you wanna quit?  :  ")
                if input3 == "NO":
                    print("ChatDNMX -> Ok...")
                    chat2()
                if input3 == "no":
                    print("ChatDNMX -> Ok...")
                    chat2()
                if input3 == "No":
                    print("ChatDNMX -> Ok...")
                    chat2()
                if input3 == "nO":
                    print("ChatDNMX -> Ok...")
                    chat2()
            except Exception:
                print("ChatDNMX -> Sorry, I don't know that.")
        elif "quit" in query:
            try:
                input1 = input("ChatDNMX -> Are you sure you wanna quit?  :  ")
                if input1 == "YES":
                    print("ChatDNMX -> Quitting...    *  Press 'ENTER' key on your keyboard to continue  *    ")

                    def userinput_change():
                        try:
                            with open("logs/exit_log.txt", "w") as f:
                                f.write(datetime.now().strftime('D:/log/logfile_%H_%M_%S_%d_%m_%Y.log'))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print("(Maybe something else)user_name  =  ", userinput1))
                                f.write(print("Log Succesful! User used ChatDNMX."))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print(userinput1))
                                f.write(print("Correct_Usage, Authorised_Usage"))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print(userinput1))
                                f.write(print("Log_ID  =  456123778"))
                                f.write(print('Debugging Succesfull!'))
                        except Exception:
                            print \
                                ("ChatDNMX -> Some problem occurred when trying to save log! (Log_file location  ="
                                "location in which this app is placed.)")
                            userinput_change()

                    userinput_change()
                    exit()
                if input1 == "yes":
                    print("ChatDNMX -> Quitting...    *  Press 'ENTER' key on your keyboard to continue  *    ")

                    def userinput_change():
                        try:
                            with open("logs/exit_log.txt", "w") as f:
                                f.write(datetime.now().strftime('D:/log/logfile_%H_%M_%S_%d_%m_%Y.log'))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print("(Maybe something else)user_name  =  ", userinput1))
                                f.write(print("Log Succesful! User used ChatDNMX."))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print(userinput1))
                                f.write(print("Correct_Usage, Authorised_Usage"))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print(userinput1))
                                f.write(print("Log_ID  =  456123778"))
                                f.write(print('Debugging Succesfull!'))
                        except Exception:
                            print \
                                ("ChatDNMX -> Some problem occurred when trying to save log! (Log_file location  =  location in which this app is placed.)")
                            userinput_change()

                    userinput_change()
                    exit()
                if input1 == "Yes":
                    print("ChatDNMX -> Quitting...    *  Press 'ENTER' key on your keyboard to continue  *    ")

                    def userinput_change():
                        try:
                            with open("logs/exit_log.txt", "w") as f:
                                f.write(datetime.now().strftime('D:/log/logfile_%H_%M_%S_%d_%m_%Y.log'))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print("(Maybe something else)user_name  =  ", userinput1))
                                f.write(print("Log Succesful! User used ChatDNMX."))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print(userinput1))
                                f.write(print("Correct_Usage, Authorised_Usage"))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print(userinput1))
                                f.write(print("Log_ID  =  456123778"))
                                f.write(print('Debugging Succesfull!'))
                        except Exception:
                            print \
                                ("ChatDNMX -> Some problem occurred when trying to save log! (Log_file location  =  location in which this app is placed.)")
                            userinput_change()

                    userinput_change()
                    exit()
                if input1 == "yEs":
                    print("ChatDNMX -> Quitting...    *  Press 'ENTER' key on your keyboard to continue  *    ")

                    def userinput_change():
                        try:
                            with open("logs/exit_log.txt", "w") as f:
                                f.write(datetime.now().strftime('D:/log/logfile_%H_%M_%S_%d_%m_%Y.log'))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print("(Maybe something else)user_name  =  ", userinput1))
                                f.write(print("Log Succesful! User used ChatDNMX."))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print(userinput1))
                                f.write(print("Correct_Usage, Authorised_Usage"))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print(userinput1))
                                f.write(print("Log_ID  =  456123778"))
                                f.write(print('Debugging Succesfull!'))
                        except Exception:
                            print \
                                ("ChatDNMX -> Some problem occurred when trying to save log! (Log_file location  =  location in which this app is placed.)")
                            userinput_change()

                    userinput_change()
                    exit()
                if input1 == "yeS":
                    print("ChatDNMX -> Quitting...    *  Press 'ENTER' key on your keyboard to continue  *    ")

                    def userinput_change():
                        try:
                            with open("logs/exit_log.txt", "w") as f:
                                f.write(datetime.now().strftime('D:/log/logfile_%H_%M_%S_%d_%m_%Y.log'))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print("(Maybe something else)user_name  =  ", userinput1))
                                f.write(print("Log Succesful! User used ChatDNMX."))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print(userinput1))
                                f.write(print("Correct_Usage, Authorised_Usage"))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print(userinput1))
                                f.write(print("Log_ID  =  456123778"))
                                f.write(print('Debugging Succesfull!'))
                        except Exception:
                            print \
                                ("ChatDNMX -> Some problem occurred when trying to save log! (Log_file location  =  location in which this app is placed.)")
                            userinput_change()

                    userinput_change()
                    exit()
                if input1 == "YEs":
                    print("ChatDNMX -> Quitting...    *  Press 'ENTER' key on your keyboard to continue  *    ")

                    def userinput_change():
                        try:
                            with open("logs/exit_log.txt", "w") as f:
                                f.write(datetime.now().strftime('D:/log/logfile_%H_%M_%S_%d_%m_%Y.log'))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print("(Maybe something else)user_name  =  ", userinput1))
                                f.write(print("Log Succesful! User used ChatDNMX."))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print(userinput1))
                                f.write(print("Correct_Usage, Authorised_Usage"))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print(userinput1))
                                f.write(print("Log_ID  =  456123778"))
                                f.write(print('Debugging Succesfull!'))
                        except Exception:
                            print \
                                ("ChatDNMX -> Some problem occurred when trying to save log! (Log_file location  =  location in which this app is placed.)")
                            userinput_change()

                    userinput_change()
                    exit()
                if input1 == "yES":
                    print("ChatDNMX -> Quitting...    *  Press 'ENTER' key on your keyboard to continue  *    ")

                    def userinput_change():
                        try:
                            with open("logs/exit_log.txt", "w") as f:
                                f.write(datetime.now().strftime('D:/log/logfile_%H_%M_%S_%d_%m_%Y.log'))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print("(Maybe something else)user_name  =  ", userinput1))
                                f.write(print("Log Succesful! User used ChatDNMX."))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print(userinput1))
                                f.write(print("Correct_Usage, Authorised_Usage"))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print(userinput1))
                                f.write(print("Log_ID  =  456123778"))
                                f.write(print('Debugging Succesfull!'))
                        except Exception:
                            print \
                                ("ChatDNMX -> Some problem occurred when trying to save log! (Log_file location  =  location in which this app is placed.)")
                            userinput_change()

                    userinput_change()
                    exit()
            except Exception:
                print("ChatDNMX -> Sorry, I don't know that.")
        elif "exit" in query:
            try:
                input2 = input("ChatDNMX -> Are you sure you wanna quit?  :  ")
                if input2 == "YES":
                    print("ChatDNMX -> Quitting...    *  Press 'ENTER' key on your keyboard to continue  *    ")

                    def userinput_change():
                        try:
                            with open("logs/exit_log.txt", "w") as f:
                                f.write(datetime.now().strftime('D:/log/logfile_%H_%M_%S_%d_%m_%Y.log'))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print("(Maybe something else)user_name  =  ", userinput1))
                                f.write(print("Log Succesful! User used ChatDNMX."))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print(userinput1))
                                f.write(print("Correct_Usage, Authorised_Usage"))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print(userinput1))
                                f.write(print("Log_ID  =  456123778"))
                                f.write(print('Debugging Succesfull!'))
                        except Exception:
                            print \
                                ("ChatDNMX -> Some problem occurred when trying to save log! (Log_file location  =  location in which this app is placed.)")
                            userinput_change()

                    userinput_change()
                    exit()
                if input2 == "yes":
                    print("ChatDNMX -> Quitting...    *  Press 'ENTER' key on your keyboard to continue  *    ")

                    def userinput_change():
                        try:
                            with open("logs/exit_log.txt", "w") as f:
                                f.write(datetime.now().strftime('D:/log/logfile_%H_%M_%S_%d_%m_%Y.log'))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print("(Maybe something else)user_name  =  ", userinput1))
                                f.write(print("Log Succesful! User used ChatDNMX."))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print(userinput1))
                                f.write(print("Correct_Usage, Authorised_Usage"))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print(userinput1))
                                f.write(print("Log_ID  =  456123778"))
                                f.write(print('Debugging Succesfull!'))
                        except Exception:
                            print \
                                ("ChatDNMX -> Some problem occurred when trying to save log! (Log_file location  =  location in which this app is placed.)")
                            userinput_change()

                    userinput_change()
                    exit()
                if input2 == "Yes":
                    print("ChatDNMX -> Quitting...    *  Press 'ENTER' key on your keyboard to continue  *    ")

                    def userinput_change():
                        try:
                            with open("logs/exit_log.txt", "w") as f:
                                f.write(datetime.now().strftime('D:/log/logfile_%H_%M_%S_%d_%m_%Y.log'))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print("(Maybe something else)user_name  =  ", userinput1))
                                f.write(print("Log Succesful! User used ChatDNMX."))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print(userinput1))
                                f.write(print("Correct_Usage, Authorised_Usage"))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print(userinput1))
                                f.write(print("Log_ID  =  456123778"))
                                f.write(print('Debugging Succesfull!'))
                        except Exception:
                            print \
                                ("ChatDNMX -> Some problem occurred when trying to save log! (Log_file location  =  location in which this app is placed.)")
                            userinput_change()

                    userinput_change()
                    exit()
                if input2 == "yEs":
                    print("ChatDNMX -> Quitting...    *  Press 'ENTER' key on your keyboard to continue  *    ")

                    def userinput_change():
                        try:
                            with open("logs/exit_log.txt", "w") as f:
                                f.write(datetime.now().strftime('D:/log/logfile_%H_%M_%S_%d_%m_%Y.log'))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print("(Maybe something else)user_name  =  ", userinput1))
                                f.write(print("Log Succesful! User used ChatDNMX."))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print(userinput1))
                                f.write(print("Correct_Usage, Authorised_Usage"))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print(userinput1))
                                f.write(print("Log_ID  =  456123778"))
                                f.write(print('Debugging Succesfull!'))
                        except Exception:
                            print \
                                ("ChatDNMX -> Some problem occurred when trying to save log! (Log_file location  =  location in which this app is placed.)")
                            userinput_change()

                    userinput_change()
                    exit()
                if input2 == "yeS":
                    print("ChatDNMX -> Quitting...    *  Press 'ENTER' key on your keyboard to continue  *    ")

                    def userinput_change():
                        try:
                            with open("logs/exit_log.txt", "w") as f:
                                f.write(datetime.now().strftime('D:/log/logfile_%H_%M_%S_%d_%m_%Y.log'))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print("(Maybe something else)user_name  =  ", userinput1))
                                f.write(print("Log Succesful! User used ChatDNMX."))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print(userinput1))
                                f.write(print("Correct_Usage, Authorised_Usage"))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print(userinput1))
                                f.write(print("Log_ID  =  456123778"))
                                f.write(print('Debugging Succesfull!'))
                        except Exception:
                            print \
                                ("ChatDNMX -> Some problem occurred when trying to save log! (Log_file location  =  location in which this app is placed.)")
                            userinput_change()

                    userinput_change()
                    exit()
                if input2 == "YEs":
                    print("ChatDNMX -> Quitting...    *  Press 'ENTER' key on your keyboard to continue  *    ")

                    def userinput_change():
                        try:
                            with open("logs/exit_log.txt", "w") as f:
                                f.write(datetime.now().strftime('D:/log/logfile_%H_%M_%S_%d_%m_%Y.log'))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print("(Maybe something else)user_name  =  ", userinput1))
                                f.write(print("Log Succesful! User used ChatDNMX."))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print(userinput1))
                                f.write(print("Correct_Usage, Authorised_Usage"))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print(userinput1))
                                f.write(print("Log_ID  =  456123778"))
                                f.write(print('Debugging Succesfull!'))
                        except Exception:
                            print \
                                ("ChatDNMX -> Some problem occurred when trying to save log! (Log_file location  =  location in which this app is placed.)")
                            userinput_change()

                    userinput_change()
                    exit()
                if input2 == "yES":
                    print("ChatDNMX -> Quitting...    *  Press 'ENTER' key on your keyboard to continue  *    ")

                    def userinput_change():
                        try:
                            with open("logs/exit_log.txt", "w") as f:
                                f.write(datetime.now().strftime('D:/log/logfile_%H_%M_%S_%d_%m_%Y.log'))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print("(Maybe something else)user_name  =  ", userinput1))
                                f.write(print("Log Succesful! User used ChatDNMX."))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print(userinput1))
                                f.write(print("Correct_Usage, Authorised_Usage"))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print(userinput1))
                                f.write(print("Log_ID  =  456123778"))
                                f.write(print('Debugging Succesfull!'))
                        except Exception:
                            print \
                                ("ChatDNMX -> Some problem occurred when trying to save log! (Log_file location  =  location in which this app is placed.)")
                            userinput_change()

                    userinput_change()
                    exit()
            except Exception:
                print("ChatDNMX -> Sorry, I don't know that.")
        elif "get out" in query:
            try:
                input3 = input("ChatDNMX -> Are you sure you wanna quit?  :  ")
                if input3 == "YES":
                    print("ChatDNMX -> Quitting...    *  Press 'ENTER' key on your keyboard to continue  *    ")

                    def userinput_change():
                        try:
                            with open("logs/exit_log.txt", "w") as f:
                                f.write(datetime.now().strftime('D:/log/logfile_%H_%M_%S_%d_%m_%Y.log'))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print("(Maybe something else)user_name  =  ", userinput1))
                                f.write(print("Log Succesful! User used ChatDNMX."))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print(userinput1))
                                f.write(print("Correct_Usage, Authorised_Usage"))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print(userinput1))
                                f.write(print("Log_ID  =  456123778"))
                                f.write(print('Debugging Succesfull!'))
                        except Exception:
                            print \
                                ("ChatDNMX -> Some problem occurred when trying to save log! (Log_file location  =  location in which this app is placed.)")
                            userinput_change()

                    userinput_change()
                    exit()
                if input3 == "yes":
                    print("ChatDNMX -> Quitting...    *  Press 'ENTER' key on your keyboard to continue  *    ")

                    def userinput_change():
                        try:
                            with open("logs/exit_log.txt", "w") as f:
                                f.write(datetime.now().strftime('D:/log/logfile_%H_%M_%S_%d_%m_%Y.log'))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print("(Maybe something else)user_name  =  ", userinput1))
                                f.write(print("Log Succesful! User used ChatDNMX."))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print(userinput1))
                                f.write(print("Correct_Usage, Authorised_Usage"))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print(userinput1))
                                f.write(print("Log_ID  =  456123778"))
                                f.write(print('Debugging Succesfull!'))
                        except Exception:
                            print \
                                ("ChatDNMX -> Some problem occurred when trying to save log! (Log_file location  =  location in which this app is placed.)")
                            userinput_change()

                    userinput_change()
                    exit()
                if input3 == "Yes":
                    print("ChatDNMX -> Quitting...    *  Press 'ENTER' key on your keyboard to continue  *    ")

                    def userinput_change():
                        try:
                            with open("logs/exit_log.txt", "w") as f:
                                f.write(datetime.now().strftime('D:/log/logfile_%H_%M_%S_%d_%m_%Y.log'))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print("(Maybe something else)user_name  =  ", userinput1))
                                f.write(print("Log Succesful! User used ChatDNMX."))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print(userinput1))
                                f.write(print("Correct_Usage, Authorised_Usage"))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print(userinput1))
                                f.write(print("Log_ID  =  456123778"))
                                f.write(print('Debugging Succesfull!'))
                        except Exception:
                            print \
                                ("ChatDNMX -> Some problem occurred when trying to save log! (Log_file location  =  location in which this app is placed.)")
                            userinput_change()

                    userinput_change()
                    exit()
                if input3 == "yEs":
                    print("ChatDNMX -> Quitting...    *  Press 'ENTER' key on your keyboard to continue  *    ")

                    def userinput_change():
                        try:
                            with open("logs/exit_log.txt", "w") as f:
                                f.write(datetime.now().strftime('D:/log/logfile_%H_%M_%S_%d_%m_%Y.log'))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print("(Maybe something else)user_name  =  ", userinput1))
                                f.write(print("Log Succesful! User used ChatDNMX."))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print(userinput1))
                                f.write(print("Correct_Usage, Authorised_Usage"))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print(userinput1))
                                f.write(print("Log_ID  =  456123778"))
                                f.write(print('Debugging Succesfull!'))
                        except Exception:
                            print \
                                ("ChatDNMX -> Some problem occurred when trying to save log! (Log_file location  =  location in which this app is placed.)")
                            userinput_change()

                    userinput_change()
                    exit()
                if input3 == "yeS":
                    print("ChatDNMX -> Quitting...    *  Press 'ENTER' key on your keyboard to continue  *    ")

                    def userinput_change():
                        try:
                            with open("logs/exit_log.txt", "w") as f:
                                f.write(datetime.now().strftime('D:/log/logfile_%H_%M_%S_%d_%m_%Y.log'))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print("(Maybe something else)user_name  =  ", userinput1))
                                f.write(print("Log Succesful! User used ChatDNMX."))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print(userinput1))
                                f.write(print("Correct_Usage, Authorised_Usage"))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print(userinput1))
                                f.write(print("Log_ID  =  456123778"))
                                f.write(print('Debugging Succesfull!'))
                        except Exception:
                            print \
                                ("ChatDNMX -> Some problem occurred when trying to save log! (Log_file location  =  location in which this app is placed.)")
                            userinput_change()

                    userinput_change()
                    exit()
                if input3 == "YEs":
                    print("ChatDNMX -> Quitting...    *  Press 'ENTER' key on your keyboard to continue  *    ")

                    def userinput_change():
                        try:
                            with open("logs/exit_log.txt", "w") as f:
                                f.write(datetime.now().strftime('D:/log/logfile_%H_%M_%S_%d_%m_%Y.log'))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print("(Maybe something else)user_name  =  ", userinput1))
                                f.write(print("Log Succesful! User used ChatDNMX."))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print(userinput1))
                                f.write(print("Correct_Usage, Authorised_Usage"))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print(userinput1))
                                f.write(print("Log_ID  =  456123778"))
                                f.write(print('Debugging Succesfull!'))
                        except Exception:
                            print \
                                ("ChatDNMX -> Some problem occurred when trying to save log! (Log_file location  =  location in which this app is placed.)")
                            userinput_change()

                    userinput_change()
                    exit()
                if input3 == "yES":
                    print("ChatDNMX -> Quitting...    *  Press 'ENTER' key on your keyboard to continue  *    ")

                    def userinput_change():
                        try:
                            with open("logs/exit_log.txt", "w") as f:
                                f.write(datetime.now().strftime('D:/log/logfile_%H_%M_%S_%d_%m_%Y.log'))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print("(Maybe something else)user_name  =  ", userinput1))
                                f.write(print("Log Succesful! User used ChatDNMX."))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print(userinput1))
                                f.write(print("Correct_Usage, Authorised_Usage"))
                                f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
                                f.write(print(userinput1))
                                f.write(print("Log_ID  =  456123778"))
                                f.write(print('Debugging Succesfull!'))
                        except Exception:
                            print \
                                ("ChatDNMX -> Some problem occurred when trying to save log! (Log_file location  =  location in which this app is placed.)")
                            userinput_change()

                    userinput_change()
                    exit()
            except Exception:
                print("ChatDNMX -> Sorry, I don't know that.")
    except Exception:
        print("ChatDNMX -> Some problem occurred!")
        chat2()


chat2()

lastinput = input("ChatDNMX -> Quitting...    *  Press 'ENTER' key on your keyboard to continue  *    ")


# The End!
def userinput_change():
    try:
        with open("logs/exit_log.txt", "w+") as f:
            f.write(datetime.now().strftime('D:/log/logfile_%H_%M_%S_%d_%m_%Y.log'))
            f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
            f.write(print("(Maybe something else)user_name  =  ", userinput1))
            f.write(print("Log Succesful! User used ChatDNMX."))
            f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
            f.write(print(userinput1))
            f.write(print("Correct_Usage, Authorised_Usage"))
            f.write(print(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
            f.write(print(userinput1))
            f.write(print("Log_ID  =  456123778"))
            f.write(print('Debugging Succesfull!'))
    except Exception:
        print \
            ("ChatDNMX -> Some problem occurred when trying to save log! (Log_file location  =  location in which this app is placed.)")
        userinput_change()
userinput_change()

# Real Exit 👇
sys.exit
