# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 11:16:16 2019

@author: Parth
"""
import facebook
page_token = "EAAmMobTZBYy8BAC133IUZCB7JpMuEzqcY9sjpA73m4POSnm3lbLbV6UfDyZAe5vMWjPL003OnJsuqwwtz4lNABswt7DhPph65u0n66vZC5yfS8gGvUMDHvLYtuPPm7HTib7J1bHPUJ1fyEcu3TqHJrXKvytOlAUq5fnJqur5cQZDZD"
app_token= "2687900944589615|KZYqSAv6zwtCe0Jim_6VxKpODsA"

graph = facebook.GraphAPI(access_token=app_token, version = "5.0")
pages_data = graph.get_object("leomessi")
print(pages_data)
'''
import pyfacebook

api = pyfacebook.Api(long_term_token='EAAmMobTZBYy8BAC133IUZCB7JpMuEzqcY9sjpA73m4POSnm3lbLbV6UfDyZAe5vMWjPL003OnJsuqwwtz4lNABswt7DhPph65u0n66vZC5yfS8gGvUMDHvLYtuPPm7HTib7J1bHPUJ1fyEcu3TqHJrXKvytOlAUq5fnJqur5cQZDZD')
print(api.get_token_info(return_json=True))

from facepy import GraphAPI
access_token = "EAAmMobTZBYy8BAC133IUZCB7JpMuEzqcY9sjpA73m4POSnm3lbLbV6UfDyZAe5vMWjPL003OnJsuqwwtz4lNABswt7DhPph65u0n66vZC5yfS8gGvUMDHvLYtuPPm7HTib7J1bHPUJ1fyEcu3TqHJrXKvytOlAUq5fnJqur5cQZDZD"

graph = GraphAPI(access_token)

# Get my latest posts
t=graph.search('Mumbai Property Market',type='group')
'''