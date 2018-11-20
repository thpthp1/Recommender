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
API_URL = 'https://api.spotify.com/v1/'
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


def index(request):
    url_args = '&'.join(['{}={}'.format(key, val)
                        for key, val in args_list.items()])
    auth_path = '{}?{}'.format(AUTH_URL, url_args)
    return redirect(auth_path)


def callback(request):
    code = request.GET.get('code')

    data = {
        'grant_type' : 'authorization_code',
        'code' : code,
        'redirect_uri' : redirect_uri
    }

    encoded_client_info = base64.standard_b64encode(
                            '{}:{}'.format(client_ID, client_secret).encode())

    header = {
        'Authorization' : 'Basic {}'.format(encoded_client_info.decode())
    }

    post_request = requests.post(TOKEN_URL, data=data, headers=header)

    response_data = json.loads(post_request.text)

    result = {'result' : json.dumps(response_data)}

    return render(request, 'mainapp/index.html', result)
