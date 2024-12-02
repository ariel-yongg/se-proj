import requests
import base64

# Spotify API credentials 
CLIENT_ID = ''
CLIENT_SECRET = ''

def get_access_token():
    """
    This function obtains an access token using Client Credentials flow.
    Returns the access token as a string.
    """
    # Encode client credentials
    credentials = f"{CLIENT_ID}:{CLIENT_SECRET}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()

    # Spotify API endpoint for token
    auth_url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": f"Basic {encoded_credentials}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials"
    }

    # Request token
    response = requests.post(auth_url, headers=headers, data=data)
    response_data = response.json()

    # Check if token is successfully received
    if response.status_code == 200:
        return response_data["access_token"]
    else:
        print("Error obtaining access token:", response_data)
        return None
        
    # Test the authentication
    access_token = get_access_token()
    if access_token:
        print("Successfully authenticated with Spotify API.")
    else:
        print("Authentication failed. Check your credentials.")