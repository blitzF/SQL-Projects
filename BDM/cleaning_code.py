import pandas as pd
import os
import csv
from datetime import datetime as dt
import numpy as np

with open("data.csv") as infile, open("out.csv", "w") as outfile:
    for line in infile:
        outfile.write(line.replace(",", " "))

data = []
data_txtanalysis = []
with open("out.csv") as infile:
	for line in infile:
		deletelist = ['{','+','"','0000']
		for word in deletelist:
			line = line.replace(word,'')

		created = line[line.find("created_at")+11:line.find("id:")]
		index = line.index(created)
		line = line[index : :]

		tweetID = line[line.find("id:")+3:line.find("id_str")]
		index = line.index(tweetID)
		line = line[index : :]

		userID = line[line.find("user:")+5:line.find("user:")+100]
		userID = userID[userID.find(":")+1:userID.find("id_str")]

		text = line[line.find("text:")+5:line.find("source:")]
		index = line.index(text)
		line = line[index : :]
		data_txtanalysis.append(text)


		reply_to = line[line.find("in_reply_to_screen_name:")+24:line.find("user:")]
		extra = 'in_reply_to_user_id_str:'
		index = line.index(reply_to)
		line = line[index+24 : :]

		location = line[line.find("location:")+9:line.find("url:")]
		index = line.index(location)
		line = line[index : :]

		description = line[line.find("description:")+12:line.find("protected:")]
		index = line.index(description)
		line = line[index : :]

		verified = line[line.find("verified:")+9:line.find("followers_count:")]
		index = line.index(verified)
		line = line[index : :]

		followers = line[line.find("followers_count:")+16:line.find("friends_count:")]
		index = line.index(followers)
		line = line[index : :]
		friends = line[line.find("friends_count:")+14:line.find("listed_count:")]
		index = line.index(friends)
		line = line[index : :]
		listed = line[line.find("listed_count:")+13:line.find("favourites_count:")]
		index = line.index(listed)
		line = line[index : :]


		favorites_all = line[line.find("favourites_count:")+17:line.find("statuses_count:")]
		index = line.index(favorites_all)
		line = line[index : :]


		statuses = line[line.find("statuses_count:")+15:line.find("created_at:")]
		index = line.index(statuses)
		line = line[index : :]


		profile_creation_date = line[line.find("created_at:")+11:line.find("utc_offset:")]
		index = line.index(profile_creation_date)
		line = line[index : :]

		language = line[line.find("lang:")+5:line.find("contributors_enabled")]
		index = line.index(language)
		line = line[index : :]

		quoted_status = line[line.find("text:")+5:line.find("source:")]
		if len(quoted_status) > 160:
			quoted_status = 'NULL'
		else:
			quoted_status = quoted_status
		

		retweeted = line[line.find("retweet_count:")+14:line.find("favorite_count")]
		index = line.index(retweeted)
		line = line[index : :]

		favorites_this= line[line.find("favorite_count:")+15:line.find("entities:")]
		index = line.index(favorites_this)
		line = line[index : :]


		hashtags = line[line.find("hashtags:")+9:line.find("urls:")]
		if hashtags == '[]':
			hashtags = "NULL"
		else:
			hashtags = hashtags
		index = line.index(hashtags)
		line = line[index : :]

		urls = line[line.find("urls:")+5:line.find("user_mentions:")]
		if urls == '[]':
			urls = "NULL"
		else:
			urls = urls
		index = line.index(urls)
		line = line[index : :]


		user_mentions = line[line.find("user_mentions:")+14:line.find("symbols:")]
		if user_mentions == '[]':
			user_mentions = "NULL"
		else:
			user_mentions = user_mentions
		index = line.index(user_mentions)
		line = line[index : :]



		data.append([created,userID,tweetID,text,reply_to,location,description,
			verified,followers,friends,listed,favorites_all,
			profile_creation_date,statuses,language,quoted_status,
			retweeted,favorites_this,hashtags,urls,user_mentions])
		

df = pd.DataFrame(data, columns= ['created','UserID','TweetID','Message','reply_to','location',
	'description','verified','followers','friends','listed','favorites_all'
	,'profile_creation_date','statuses','language','quoted_status',
	'retweeted','favorites_this','hashtags','urls','user_mentions'])




df.to_csv('clean_data.csv', index=False, sep=',' , line_terminator='\n')

with open('texts.txt', 'w') as f:
    for item in data_txtanalysis:
        f.write("%s\n" % item)

with open('texts.csv', 'w') as f:
    for item in data_txtanalysis:
        f.write("%s\n" % item)

with open("clean_data.csv") as in_file:
	with open("out_fnam.csv", 'w') as out_file:
		writer = csv.writer(out_file)
		for row in csv.reader(in_file):
			if any(field.strip() for field in row):
				writer.writerow(row)

with open("out_fnam.csv") as inn_file:
	with open("final.csv", 'w') as outt_file:
		writer = csv.writer(outt_file)
		for row in csv.reader(inn_file):
			if any(field.strip() for field in row):
				writer.writerow(row)
os.remove('out.csv')
os.remove('clean_data.csv')
os.remove('out_fnam.csv')


