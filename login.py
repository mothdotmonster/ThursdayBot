#!/usr/bin/env python3

from mastodon import Mastodon

url = input("Instance URL: ")
username = input("Username: ")
password = input("Password: ")

Mastodon.create_app(
    'ThursdayBot',
    api_base_url = url,
    website= 'https://moth.monster/projects/thursday/',
    to_file = 'pytooter_clientcred.secret'
)

mastodon = Mastodon(client_id = 'pytooter_clientcred.secret',)
mastodon.log_in(
    username,
    password,
    to_file = 'pytooter_usercred.secret'
)

print("Sign-in complete. Make sure to keep all .secret files secret!")