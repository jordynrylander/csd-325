# Jordyn Rylander
# module 9.2
# 5/10/2026

# Imports requests library for API communication
import requests

# Imports json library for formatting JSON data
import json


# Function to format and print JSON data
def format_json(obj):

    # Formats JSON data with indentation
    text = json.dumps(obj, sort_keys=True, indent=4)

    # Prints formatted JSON
    print(text)


# Sends a GET request to the Cat Facts API
response = requests.get("https://catfact.ninja/fact")


# Prints API connection test
print("Cat Facts API Connection Test")

# Prints status code returned from the API
print("Status Code:", response.status_code)


# Prints raw API response
print("\nUnformatted Response")
print(response.json())


# Prints formatted API response
print("\nFormatted Cat Fact")
format_json(response.json())