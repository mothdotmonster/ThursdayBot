#!/usr/bin/env python3

from mastodon import Mastodon

url = input("Instance URL: ")

Mastodon.create_app(
    'ThursdayBot',
    api_base_url = url,
    website= 'https://moth.monster/projects/thursday/',
    to_file = 'pytooter_clientcred.secret'
)

mastodon = Mastodon(client_id = 'pytooter_clientcred.secret',)

print(mastodon.auth_request_url())

password = input("Code: ")

mastodon.log_in(
    code = password,
    to_file = 'pytooter_usercred.secret'
 )

print("Sign-in complete. Make sure to keep all .secret files secret!")
