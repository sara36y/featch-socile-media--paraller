import requests

# استبدل بـ Access Token و Page ID
access_token = "EAAR1hZAsKzzQBO1Ia2iM5tBqZB90sLDDyo8twUwSzhDJW5GI1p692YfJFl2eABARYZAemefVSQsWjEAXLhYfTDypDcJnepKKaRchFDGiWxbQJ20AuLLdQpaQK2hqIpkQfOmUEyffr6tM41BSXRaqtAGkFuV9PVWE70nh1jtb7La1ZAyofdc7MLRTDyhWTRSBhWPTGY41MNGn6U7ciKRNN22QnomJcLqD8AZDZD"
page_id = "100012886029734"  # استبدل بـ Page ID الخاص بك

url = f"https://graph.facebook.com/100012886029734/posts"
params = {
    "access_token": access_token,
    "fields": "message,created_time,attachments"
}

response = requests.get(url, params=params)

# تحقق من الاستجابة
if response.status_code == 200:
    print(response.json())  # طباعة البيانات المسترجعة
else:
    print(f"Error: {response.status_code}")
    print(response.json())  # طباعة تفاصيل الخطأ إذا حدث




