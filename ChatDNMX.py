#
#
#
#
#  Chat DNMX - A product made for fun.
#
#  Arinjay Kumar Chat DNMX
#
#  Product by Arinjay Kumar
#
#  A part of Zodiac
#
# Dear Programmers and Coders, This is note to you that: Please credit me if you want to share or use this code in
# any type of medium.
#
#  Enjoy!
#
#
#
#

import smtplib  # Import the smtplib module
import bcrypt # pip install bcrypt
import re # pip install bcrypt
import wikipedia  # pip install wikipedia
import datetime  # pip install datetime
import os  # pip install os
import webbrowser  # pip install webbrowser
import logging  # pip install logging
import sys # pip install sys
import os # pip install os
import openai # pip install openai
import google.generativeai as palm # pip install google-generativeai
import base64
import requests


def create_log_files():
    # Directory 
    directory = "logs"
    
    # Parent Directory path 
    parent_dir = "D:/donotopenthisfolder/Arinjay/CONFIDENTIAL/Pending/ChatDNMX/"
    
    # Path 
    path = os.path.join(parent_dir, directory) 
    
    # Create the directory 
    # 'logs' in 
    # 'D:/donotopenthisfolder/Arinjay/CONFIDENTIAL/Pending/ChatDNMX/' 
    try:  
        os.makedirs(path)  
    except OSError as error:  
        print(error)  

    log_files = ["logs/username_log.txt", "logs/password_log.txt", "logs/email_log.txt", "logs/exit_log.txt"]
    for log_file in log_files:
        with open(log_file, "w") as file:
            file.write("")


def hash_password_sha256(password):
    # Hash the password using SHA-256
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password


def validate_email(email):
    # Validate email format using a regular expression
    email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    return bool(email_pattern.match(email))


def validate_username(username):
    # Validate username length and characters
    return 1 <= len(username) <= 64 and username.isalnum()


def validate_password(password):
    # Validate password length and complexity
    return 8 <= len(password) <= 20 and password.isdigit()

def user_sign_up_def():
    try:
        create_log_files()  # Create log files if they don't exist

        username = input("Enter username: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        confirm_password = input("Confirm password: ")

        # Your validation and account creation logic here
        def validation():
            # Validate username
            if not validate_username(username):
                raise ValueError("Invalid username. Username must be 4-20 characters long and alphanumeric.")

            # Validate email
            if not validate_email(email):
                raise ValueError("Invalid email address.")

            # Validate password
            if not validate_password(password):
                raise ValueError(
                    "Invalid password. Password must be 8-20 characters long, contain at least one uppercase letter, "
                    "and one digit.")

            if password != confirm_password:
                raise ValueError("Passwords do not match. Please try again.")

            existing_username = ""
            with open("logs/username_log.txt", "r") as file1:
                existing_username = file1.read().strip()

            if existing_username:
                raise ValueError("Username already exists. Please choose a different username.")

            existing_email = ""
            with open("logs/email_log.txt", "r") as file3:
                existing_email = file3.read().strip()

            if existing_email:
                raise ValueError("Email already exists. Please choose a different email.")

            existing_password = ""
            with open("logs/password_log.txt", "r") as file2:
                existing_password = file2.read().strip()

            if existing_password:
                raise ValueError("Account already exists. Please log in.")

            hashed_password = hash_password_sha256(password)

            with open("logs/username_log.txt", "w") as file1, \
                    open("logs/email_log.txt", "w") as file3, \
                    open("logs/password_log.txt", "w") as file2:
                file1.write(username)
                file3.write(email)
                file2.write(hashed_password.decode('utf-8'))

            print("Success", "Account successfully created. Check your email for confirmation.")
            # Display a message
            print("Account successfully created. Check your email for confirmation.")

        if validation != True:
            sys.exit()

        # Greeting  :-

        I = str(
            input(
                "ChatDNMX -> Hello, {username}    *  Press 'ENTER' key on your keyboard to continue  *    "
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
                "ChatDNMX -> 2.) This chatting session is only one time. You have to restart to ask more questions.    *  Press"
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

        userinput3 = input("You -> ")

        chat_List = [
            "1. OpenAI's ChatGPT 3.5",
            "2. Google's Bard AI",
            "3. Stability XL 1024 1.0",
            "4. Or continue with ChatDNMX..."
        ]


        def chat_List_Def():
            if chat_List.has_key("1. OpenAI's ChatGPT 3.5") or chat_List == 1:
                chatgpt()
            elif chat_List.has_key("2. Google's Bard AI") or chat_List == 2:
                bard()
            elif chat_List.has_key("3. Stability XL 1024 1.0") or chat_List == 3:
                stability()
            elif chat_List.has_key("4. Or continue with ChatDNMX...") or chat_List == 4:
                chat2()
            else:
                print("ChatDNMX -> That is not what I expected!")
                print("ChatDNMX -> Retrying...")
                chat_List_Def()

        chat_List_Def()


        def chatgpt(): 
            def chat():
                openai.api_key = "YOUR_API_KEY"

                userinput = input("You -> ")

                response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=userinput,
                    temperature=0.7,
                    max_tokens=256,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
                )

                print("ChatGPT -> ", response)

                def loop():
                    if chat():
                        chat()
                        loop()
                    else:
                        chat()
                        loop()


                loop()


        def bard():
            def chat():
                prompt = input("""You -> """)

                print("""
                        
                I am still under development, and there are many things that I do not know. If I don't know the answer to a question, I will say so honestly. I will also try to provide some context or resources that may help you find the answer yourself. For example, I might say something like "I'm not sure about that, but I can find out for you. Can you give me more information about what you're looking for?" or "I'm not familiar with that topic, but I can provide you with some links to relevant websites."

                I am always learning new things, and I am committed to providing accurate and helpful information to my users. If you ever notice that I have made a mistake, please feel free to let me know. I appreciate your feedback and will use it to improve my performance.
                        
                """)

                palm.configure(api_key="YOUR_API_KEY")
                models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
                model = models[0].name

                completion = palm.generate_text(
                    model=model,
                    prompt=prompt,
                    temperature=0,
                    # The maximum length of the response
                    max_output_tokens=1000000,
                )

                print("Bard -> ", completion.result)


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
                url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"

                text_Prompt = input("Your prompt -> ")
                prompt_type = input("How you want it to look like? Separate your options by a comma -> ")

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

                headers = {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Authorization": "YOUR_API_KEY",
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

                print("ChatDNMX -> Finished, check this directory.")
                

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

                # Our Recommendation : Add your favourite websites here!

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

                # Our Recommendation : Put your music library/directory/file location 

                elif "play music" in query:
                    print("ChatDNMX -> Opening Music...")
                    music_dir = "Your music library/directory/file location here!"
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir, songs[0]))
                elif "open music" in query:
                    print("ChatDNMX -> Opening Music...")
                    musicPath = (
                        "Your music library/directory/file location here!"
                    )
                    os.system(f"open {musicPath}")
                elif "what is the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    print(f"ChatDNMX -> Sir, the time is : {strTime}")

                # Our Recommendation : Put your Visual Studio Code directory location here! 

                elif "open code" in query:
                    print("ChatDNMX -> Opening Visual Studio Code...")
                    codePath = "Your Visual Studio Code directory location here!"
                    os.startfile(codePath)
                elif "the time" in query:
                    hour = datetime.datetime.now().strftime("%H")
                    min = datetime.datetime.now().strftime("%M")
                    print(f"ChatDNMX -> Sir/Madam, the current time is {hour}:{min}")

                # Our Recommendation : Put your Facetime directory location here!

                elif "open facetime".lower() in query.lower():
                    print("ChatDNMX -> Opening Facetime...")
                    os.system(f"Your Facetime directory location here!")

                # Our Recommendation : Put your Passkey directory location here!

                elif "open pass".lower() in query.lower():
                    print("ChatDNMX -> Opening Passkey...")
                    os.system(f"Your Passkey directory location here!")
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

    except ValueError as ve:
        print("Error", f"Error: {ve}")
    except Exception as e:
        print(f"Error: {str(e)}")
        print("Error", f"Error Code: 404. Some problem occurred! Details: {str(e)}")
    finally:
        sys.exit


if __name__ == "__main__":
    user_sign_up_def()
