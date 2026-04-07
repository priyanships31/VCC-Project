import requests

# Replace with YOUR VM external IP
url = "http://35.222.188.129:5000/detect"

# Send image file
files = {"image": open("test.png", "rb")}

response = requests.post(url, files=files)

print("Response from server:")
print(response.json())