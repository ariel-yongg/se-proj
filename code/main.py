import requests
import base64
import webbrowser
from urllib.parse import urlencode, urlparse, parse_qs

# Spotify API credentials
CLIENT_ID = "5fcc74a4c3a54d2dbae763db12559fa2"
CLIENT_SECRET = "3ee9835fa7af42df8d6f475a3c1d4396"
REDIRECT_URI = "http://localhost/callback"  # Replace with your redirect URI

# Step 1: Authorize User
def authorize_user():
    """
    Open the Spotify login page to get authorization code.
    """
    auth_url = "https://accounts.spotify.com/authorize"
    params = {
        "client_id": CLIENT_ID,
        "response_type": "code",
        "redirect_uri": REDIRECT_URI,
        "scope": "user-top-read",
    }
    webbrowser.open(f"{auth_url}?{urlencode(params)}")

# Step 2: Exchange Authorization Code for Access Token
def get_access_token(auth_code):
    """
    Exchange authorization code for access token.
    """
    token_url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode(),
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {
        "grant_type": "authorization_code",
        "code": auth_code,
        "redirect_uri": REDIRECT_URI,
    }
    response = requests.post(token_url, headers=headers, data=data)
    response_data = response.json()
    if response.status_code == 200:
        return response_data["access_token"]
    else:
        print("Error obtaining access token:", response_data)
        return None

# Step 3: Fetch User's Top Artists
def get_top_artists(access_token):
    """
    Fetch user's top artists.
    """
    url = "https://api.spotify.com/v1/me/top/artists"
    headers = {
        "Authorization": f"Bearer {access_token}",
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching top artists:", response.json())
        return None

# Main execution
if __name__ == "__main__":
    # Step 1: Authorize User
    print("Opening Spotify login page...")
    authorize_user()
    auth_code = input("Paste the authorization code here: ")

    # Step 2: Get Access Token
    access_token = get_access_token(auth_code)
    if access_token:
        print("Successfully authenticated with Spotify API.")

        # Step 3: Fetch and display user's top artists
        top_artists = get_top_artists(access_token)
        if top_artists:
            print("\nYour Top Artists:")
            for idx, artist in enumerate(top_artists.get("items", []), start=1):
                print(f"{idx}. {artist['name']} (Genres: {', '.join(artist['genres'])})")
    else:
        print("Failed to authenticate with Spotify API.")
