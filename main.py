import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    parameters = sys.argv

    if len(parameters)<2:
        print("No prompt provided")
        sys.exit(1)

    verbose = False
    if len(parameters)==3 and parameters[2]=="--verbose":
        verbose = True
        
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = parameters[1]
    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)]),]

    response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)
    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count

    if verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")
    print(response.text)


if __name__ == "__main__":
    main()
