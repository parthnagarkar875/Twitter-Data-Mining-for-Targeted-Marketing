# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 11:16:16 2019

@author: Parth
"""
'''
import facebook
page_token = "EAAmMobTZBYy8BAC133IUZCB7JpMuEzqcY9sjpA73m4POSnm3lbLbV6UfDyZAe5vMWjPL003OnJsuqwwtz4lNABswt7DhPph65u0n66vZC5yfS8gGvUMDHvLYtuPPm7HTib7J1bHPUJ1fyEcu3TqHJrXKvytOlAUq5fnJqur5cQZDZD"


graph = facebook.GraphAPI(access_token=page_token)
pages_data = graph.get_object(id=1543746042617492)

print(pages_data)

import pyfacebook

api = pyfacebook.Api(long_term_token='EAAmMobTZBYy8BAC133IUZCB7JpMuEzqcY9sjpA73m4POSnm3lbLbV6UfDyZAe5vMWjPL003OnJsuqwwtz4lNABswt7DhPph65u0n66vZC5yfS8gGvUMDHvLYtuPPm7HTib7J1bHPUJ1fyEcu3TqHJrXKvytOlAUq5fnJqur5cQZDZD')
print(api.get_token_info(return_json=True))
'''

from facepy import GraphAPI
access_token = "EAAmMobTZBYy8BAC133IUZCB7JpMuEzqcY9sjpA73m4POSnm3lbLbV6UfDyZAe5vMWjPL003OnJsuqwwtz4lNABswt7DhPph65u0n66vZC5yfS8gGvUMDHvLYtuPPm7HTib7J1bHPUJ1fyEcu3TqHJrXKvytOlAUq5fnJqur5cQZDZD"

graph = GraphAPI(access_token)

# Get my latest posts
graph.get('me/posts')
