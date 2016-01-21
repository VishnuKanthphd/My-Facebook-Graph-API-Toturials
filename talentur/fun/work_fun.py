import json
import requests
from collections import Counter

def liker_ids_tornado(response, like_ids_list = None):
	like_ids_list = [] if like_ids_list is None else like_ids_list
	data_list = response['data']

	for post_message_story in data_list:
		if 'likes' in post_message_story:
			for liker in post_message_story['likes']['data']:
				like_ids_list.append((liker['id'], liker['name']))
	if 'paging' in response and 'next' in response['paging']:
		r = requests.get(response['paging']['next']).json()
		liker_ids_tornado(r, like_ids_list)
	return like_ids_list

def get_most_likers(like_ids_list):
	id_results_dict = Counter(like_ids_list)
	return id_results_dict

def string_to_dict(json_string):
    return json.loads(json_string)

def tornado_all_posts_dict(response_dict, master_posts = None ):
	master_posts = {'data':[]} if master_posts is None else master_posts
	posts = response_dict['data']
	master_posts['data'] = master_posts['data'] + posts
	if 'paging' in response_dict and 'next' in response_dict['paging']:
		r = requests.get(response_dict['paging']['next']).json()
		tornado_all_posts_dict(r, master_posts)
	return master_posts

def remove_dicts_from_list_based_on_key(response_dict, key):
	the_list = response_dict['data']
	return [dicti for dicti in the_list if key in dicti]

def sort_posts_dict_by_likes(response_dict):
	list_of_user_post_objects = response_dict['data']
	list_of_user_post_objects = sorted(list_of_user_post_objects, key=lambda k: -k['likes']['summary']['total_count']) 
	return list_of_user_post_objects

def get_all_posts_dict(response):
	return tornado_all_posts_dict(string_to_dict(response))