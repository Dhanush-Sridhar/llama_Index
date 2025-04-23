#####################################################################
#                                                                     #
#                       LLM Definition Module                         #
#                                                                     #
#   This module provides functionality to initialize and configure    #
#   the Google Gemini LLM model for text generation tasks.           #
#                                                                     #
#   Author: DHANUSH                                                   #
#   Date: 23/04/2025                                                 #
#                                                                     #
#####################################################################




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