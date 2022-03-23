from requests import get


url = 'http://127.0.0.1:8000/bills/api/kredyts/'

print(url)

with get(url) as content:
    for row in content.json():
        print(row)
