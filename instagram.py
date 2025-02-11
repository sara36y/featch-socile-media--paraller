import requests

instagram_business_account_id = "17841470995138639"  # ID الخاص بحساب Instagram Business
access_token = "IGQWRQV3JhdjFYbHlHaXB6T0RnWGVzQktxZAlFDYWxYU3ZA3UEJjMVBQMDBqTDFSaFYwSDVnRjBVc2ZAFTHFkSTBIMXdyTExKSndJQThPazIyWG5FMTV0ZAUdGY1Q0d2JDTG9YNEVCelI2eHVxSE1Obk1vbmFvYjBGNUUZD"  # استبدل بـ Access Token

url = f"https://graph.instagram.com/{instagram_business_account_id}/media"
params = {
    "fields": "id,caption,media_type,media_url,thumbnail_url,timestamp",  # حدد الحقول اللي عايز تجيبها
    "access_token": access_token
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}, {response.json()}")
