import requests

url = 'https://github.com/HarshShah03325/AI-for-healthcare/tree/main/Chest%20X-Ray%20Analysis/assets'
response = requests.get(url)

with open('downloaded_image.jpg', 'wb') as file:
    file.write(response.content)

print("Image downloaded successfully.")
