scopes = ["user:read"]
user_scopes = ["user:read","user:write","group:read","group:write"]

print(any([scope in scopes for scope in user_scopes]))


import requests

GOOGLE_TOKEN_VALIDATION_URL = "https://www.googleapis.com/oauth2/v1/tokeninfo"

def validate_access_token(token:str):
    response = requests.get(f"{GOOGLE_TOKEN_VALIDATION_URL}?access_token={token}")
    return response.json()

token = "ya29.a0AcM612yQZqipJYUeZrK1fnDdGgwKlaKKPlCYr-pkpeUvd8aYm1neWWJio6p2JynoHzvM7SD1khCozNYZq8I6M2YU6a5B3M2KUG7qKDxVygKE85lcbAXnChPt73F47FL244NMASXqgCKGe-_00HXJO0XGuK_715H3mXFNd337WAaCgYKATQSARMSFQHGX2MilGm9NhwKxvYPhe-lSYQE8A0177"
print(validate_access_token(token))