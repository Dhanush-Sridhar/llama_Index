from llama_index.llms.google_genai import GoogleGenAI

import os
import dotenv
import sys

dotenv.load_dotenv()



def get_llm():
    return GoogleGenAI(
        model="gemini-2.0-flash",
        api_key=os.getenv("GOOGLE_API_KEY")
    )


# multiline comment
'''''
llm = get_llm()

# command line argument
if len(sys.argv) > 1:   
    user_input = sys.argv[1]
else:
    user_input = input("Enter a prompt: ")

response = llm.complete(user_input)

print(response)
'''''