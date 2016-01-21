from django.shortcuts import render
import json
from django.http import HttpResponse

from .fun.work_fun import ( 
	get_all_posts_dict, 
	string_to_dict,
	sort_posts_dict_by_likes,
	remove_dicts_from_list_based_on_key,
	get_most_likers,
	liker_ids_tornado
)


def fb_login(request):
	if request.method == 'POST':

		all_posts_dict = get_all_posts_dict(request.POST['user_posts'])
		all_posts_dict['data'] = remove_dicts_from_list_based_on_key(all_posts_dict, 'likes')

		my_most_liked_post = sort_posts_dict_by_likes(all_posts_dict)[0]
		print my_most_liked_post

		like_ids_list = liker_ids_tornado(all_posts_dict)
		my_biggest_fans = get_most_likers(like_ids_list)
		print my_biggest_fans

	return render(request, 'talentur/fb_login.html')
