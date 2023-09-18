mport requests

url = "https://httpbin.org/put"

payload = "<file contents here>"
headers = {
  'Name': 'Sankalp Swarup',
  'Email': 'sankalp.swarup2020@vitbhopal.ac.in',
  'College': 'VIT Bhopal',
  'StudentId': '20BCY10114',
  'FileName': 'main.py',
  'Content-Type': 'application/octet-stream'
}

response = requests.request("PUT", url, headers=headers, data=payload)

if response.status_code == 200:
    print("Details submitted successfully!")
else:
    print(f"Failed to submit details. Error: {response.text}")