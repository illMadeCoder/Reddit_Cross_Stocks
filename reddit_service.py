import praw

reddit = praw.Reddit(
    client_id="uVt13TRTymSChw",
    client_secret="8qW4ZmcR3p35CH6ksOdqhrstt6k_Mw",
    user_agent="reddit_times_stock",
)

# submissions = reddit.subreddit("learnpython").hot(limit=10)
# l = list(map(lambda x : x.comments, submissions))
# list(map(lambda x : x.author,l[0]))

def hot_submissions(subreddit_name):
    return reddit.subreddit(subreddit_name).hot(limit=10)

def get_titles(subreddit):
    pass

def get_comment_bodys(submissions):    
    return list(map(lambda x : list(map(lambda y: y.body, x.comments.replace_more(limit=0) and x.comments)), submissions))
