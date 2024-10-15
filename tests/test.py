import  requests

GOOGLE_TOKEN_VALIDATION_URL = "https://www.googleapis.com/oauth2/v1/tokeninfo"
access_token = 'ya29.a0AcM612xiGa1uo5gGh2Dt5bQsT4ABPB4yiaswkqWCKOCkUq2M6-aFZssO1yPFvU54kb7CoLNzS0qCVvJLiehJyBLnX79Q8Q8MBXwIxQtwYdLhC929qp4lmutT2RM2hf-Naq2XkXqQokUajLOx3jFAuTAIebqi9Eq9aue_8PPgSwaCgYKAfUSARMSFQHGX2MiFzHjJfVm-you1IqiiKUqWw0177'
response = requests.get(f"{GOOGLE_TOKEN_VALIDATION_URL}?access_token={access_token}")
print(response.status_code)
# from datetime import  datetime
#
# print(datetime.now())
# print(datetime.fromtimestamp(1728891148135/1000))

