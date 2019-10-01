from django.shortcuts import render, redirect
from recommender.secret import client_ID, client_secret
import requests
import json
import urllib
import base64

# Create your views here.
PORT = 8000

# URL end-point
AUTH_URL = "https://accounts.spotify.com/authorize"
API_URL = 'https://api.spotify.com/v1'
TOKEN_URL = 'https://accounts.spotify.com/api/token'
CALLBACK_URL = 'callback/q'
redirect_uri = 'http://127.0.0.1:' + '{}/{}'.format(PORT, CALLBACK_URL)

# scopes
scopes = [
    'user-read-private',
]

args_list = {
    'response_type' : 'code',
    'client_id' : client_ID,
    'scope' : ' '.join(scopes),
    'redirect_uri' : redirect_uri,
}

# Auth token
auth_token = None


def signin(request):
    url_args = '&'.join(['{}={}'.format(key, val)
                        for key, val in args_list.items()])
    auth_path = '{}?{}'.format(AUTH_URL, url_args)
    return redirect(auth_path)

def index(request):
    user_data = request.session['user_data']
    if user_data != None:
        user_data = json.loads(user_data)
        return render(request, 'mainapp/index.html', context={"data" : sorted(user_data.items())})
    else:
        return render(request, 'mainapp/index.html')

def callback(request):

    # getting the auth code
    code = request.GET.get('code')
    data = {
        'grant_type' : 'authorization_code',
        'code' : code,
        'redirect_uri' : redirect_uri
    }

    encoded_client_info = base64.standard_b64encode(
                            '{}:{}'.format(client_ID, client_secret).encode())

    auth_header = {
        'Authorization' : 'Basic {}'.format(encoded_client_info.decode())
    }

    post_request = requests.post(TOKEN_URL, data=data, headers=auth_header)

    # Get response data
    response_data = json.loads(post_request.text)

    auth_token = response_data['access_token']
    token_type = response_data['token_type']
    expires_in = response_data['expires_in']
    refresh_token = response_data['refresh_token']

    auth_dict = {
        'auth_token' : auth_token,
        'token_type' : token_type,
        'expires_in' : expires_in,
        'refresh_token' : refresh_token
    }

    # Send in the authorization for user's info
    API_ENDPOINT = "{}/me".format(API_URL)

    user_header = {
        "Authorization" : "Bearer {}".format(auth_token)
    }

    get_request = requests.get(API_ENDPOINT, headers=user_header)
    user_data = json.loads(get_request.text)
    request.session['user_data'] = get_request.text
    return redirect(index)
