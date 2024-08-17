import random
import requests

# Define some responses
responses = {
    "hi": ["Hello!", "Hi there!", "Greetings!"],
    "how are you": ["I'm just a bunch of code, but I'm doing well!", "I'm doing great, thanks!", "All systems are operational!"],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "name": ["I'm your friendly chatbot!", "I don't have a name, but I'm here to chat!", "You can call me ChatBot."],
}

# Function to perform a web search using Bing Search API
def web_search(query):
    api_key = "YOUR_BING_SEARCH_API_KEY"  # Replace with your actual API key
    search_url = "https://api.bing.microsoft.com/v7.0/search"
    headers = {"Ocp-Apim-Subscription-Key": api_key}
    params = {"q": query, "textDecorations": True, "textFormat": "HTML"}

    try:
        response = requests.get(search_url, headers=headers, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        search_results = response.json()

        # Extracting the top result
        if "webPages" in search_results and "value" in search_results["webPages"]:
            top_result = search_results["webPages"]["value"][0]
            return f"Here's what I found: {top_result['name']} - {top_result['snippet']} ({top_result['url']})"
        else:
            return "Sorry, I couldn't find any information on that."

    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except Exception as err:
        return f"An error occurred: {err}"

# Function to get a response
def get_response(user_input):
    # Convert the user input to lowercase to make it case-insensitive
    user_input = user_input.lower()

    # Check if the user's input matches any of the keys in the responses dictionary
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])

    # Check if the user wants to perform a web search
    if "search" in user_input:
        search_query = user_input.replace("search", "").strip()
        if search_query:
            return web_search(search_query)
        else:
            return "What would you like me to search for?"

    # If no match is found, return a default response
    return "I'm not sure how to respond to that."

# Main loop
print("ChatBot: Hello! I'm your chatbot. Type 'bye' to exit.")

while True:
    user_input = input("You: ")

    # Exit the chat if the user types 'bye'
    if "bye" in user_input.lower():
        print("ChatBot: Goodbye!")
        break

    # Get and print the response
    response = get_response(user_input)
    print(f"ChatBot: {response}")
