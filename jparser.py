#!/usr/bin/env python3
import re
import json
import time
from datetime import datetime, date

def total_like_of(jsonstr):
	total_like_str = re.search('"edge_hashtag_to_media":{"count":(\d+)', jsonstr).group(0) #
	total_like_count : int = int(total_like_str.split(':')[2]) # Milestone
	print('\n\tTotal likes: \t' + str(total_like_count) + '\n') 
	return total_like_count
	

def create_top9infolist(jsonstr):	
	toppost_str = re.search('"edge_hashtag_to_top_posts":.*},"edge_hashtag_to_content_advisory', jsonstr).group(0)[28 : -34] # shameful hard coded # print(toppost_str)
	toppost_dicts = json.loads(toppost_str)
	with open('raw_top.json', 'w', encoding='utf-8') as jsonfile:
		json.dump(toppost_dicts, jsonfile, indent=4, ensure_ascii=False) 
		
	# print(toppost_dicts["edges"][0]["node"])
		
	
#	returndict = {
#		"postId" : postId, 
#		"numLike": numLike,
#		"numComment": numComment,
#		"date": date,
#		"TAG?"
#	}
	
	newdict = {}
	returndictlist = []
	
	print("PostID\t\tLikes\tComments\tDate")
	for jdict in toppost_dicts["edges"]:
		
		postId = jdict["node"]["shortcode"]
		numLike = str(jdict["node"]["edge_liked_by"]["count"])
		numComment = str(jdict["node"]["edge_media_to_comment"]["count"])
		date = datetime.utcfromtimestamp(jdict["node"]["taken_at_timestamp"]).strftime('%Y-%m-%d')
		
		newdict["postId"] = postId
		newdict["numLike"] = numLike
		newdict["numComment"] = numComment
		newdict["date"] = date
		
		returndictlist.append(newdict)
				
		print(postId + '\t' 
			+ numLike + '\t'
			+ numComment + '\t\t'
			+ date
		) # for display only 
		
	return returndictlist