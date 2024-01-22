import google.generativeai as palm


def chat():
    prompt = input("""You: """)

    print("""
            
    I am still under development, and there are many things that I do not know. If I don't know the answer to a question, I will say so honestly. I will also try to provide some context or resources that may help you find the answer yourself. For example, I might say something like "I'm not sure about that, but I can find out for you. Can you give me more information about what you're looking for?" or "I'm not familiar with that topic, but I can provide you with some links to relevant websites."

    I am always learning new things, and I am committed to providing accurate and helpful information to my users. If you ever notice that I have made a mistake, please feel free to let me know. I appreciate your feedback and will use it to improve my performance.
            
    """)

    palm.configure(api_key='AIzaSyDy9KlkJM9AZkJ6aQ-kpADRRUxlGbGN6vQ')
    models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
    model = models[0].name

    completion = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=0,
        # The maximum length of the response
        max_output_tokens=1000000,
    )

    print("Bard: ", completion.result)


def loop():
    if chat():
        chat()
        loop()
    else:
        chat()
        loop()


loop()
