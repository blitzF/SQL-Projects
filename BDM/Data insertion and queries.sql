USE databasee;

CREATE TABLE twitter_data
(Created VARCHAR(7000),UserID VARCHAR(1000),TweetID VARCHAR(1000),Message VARCHAR(8000),ReplyTo VARCHAR(1000),Location VARCHAR(8000),Description_ text,Verified VARCHAR(1000),Followers VARCHAR(1000),Friends VARCHAR(1000),Listed VARCHAR(1000),Faviourites VARCHAR(1000),ProfileCreationDate VARCHAR(1000),Statuses VARCHAR(1000),Language_ VARCHAR(1000),QuotedStatuses text,Retweeted VARCHAR(1000),FaviouriteThis VARCHAR(1000),Hashtag VARCHAR(8000),Urls VARCHAR(8000),UserMentions VARCHAR(8000));

BULK INSERT twitter_data
FROM 'C:\Users\Desktop\final.csv'
WITH(FIRSTROW = 3,FIELDTERMINATOR = ',', ROWTERMINATOR = '\n');

Select count(Message) as TotalTweets
from twitter_data;

Select count(Message) as NumberOfRetweets
From twitter_data
Where Message LIKE '%RT%';

Select count(distinct UserID) as NumberofUniqueUsers
From twitter_data;

Select count(Message) as TweetsWithUrl
from twitter_data
Where Urls is not null;

Select count(Message) as NumberofReplies
From twitter_data 
Where Message LIKE '%@%';

Select UserID, Followers
From twitter_data
Where Followers > 2000000;

Select count(Message) as TweetsContainingBrexit
From twitter_data
Where Message LIKE '%Brexit%';

Select count(Message) as TweetFromEngland
From twitter_data
Where Location LIKE '%england%'
OR Location LIKE '%England%';

Select count(distinct UserID) as NumOfVerifiedAccounts
From twitter_data
Where Verified is not null;

Select count(Message) as HatredTweets
From twitter_data
Where Message LIKE '%dislike%'
OR Message LIKE '%hate%'
OR Message LIKE '%against%'
OR Message LIKE '%disgust%'
OR Message LIKE '%contempt%'
OR Message LIKE '%disrespect%'
OR Message LIKE '%pathetic%';