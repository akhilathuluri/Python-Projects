import requests
import json

print("Mobile Number validation")
print("API Used Is Abstract-Api: https://www.abstractapi.com/")
num = input("Enter The Mobile Number With Including Country Code Remove +")
response = requests.get(f"https://phonevalidation.abstractapi.com/v1/?api_key=<YOUR_API_KEY>&phone={num}")
print(response.status_code)

data = json.loads(response.content)
for key, value in data.items():
    if key in ['format', 'country']:
        print(f"{key}:")
        for sub_key, sub_value in value.items():
            if sub_key == ['international','code']:
                print(f"  {sub_key}: {sub_value}")
            else:
                print(f"  {sub_key}: {sub_value}")
    else:
        print(f"{key}: {value}")