# Jordyn Rylander
# module 9.2
# 5/10/2026

# Imports the requests library so Python can connect
import requests
# Imports json so responses can be formatted and easier to read
import json

# Function used to print formatted JSON data
def jprint(obj):
    # Converts JSON into a formatted string
    text = json.dumps(obj, sort_keys=True, indent=4)
    # Prints formatted text
    print(text)

# Sends a GET request to the Dog API
response = requests.get("https://dog.ceo/api/breeds/image/random")

# Prints API connection test information
print("Dog API Connection Test")
# Prints the status code returned from the API
print("Status Code:", response.status_code)

# Prints the raw unformatted response
print("\nUnformatted Response")
print(response.json())

# Prints the formatted response
print("\nFormatted Response")
jprint(response.json())