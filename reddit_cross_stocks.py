import reddit_service
import stock_service
import parsing_service
import functools
import graph_service

# get list of all stock symbols
stock_symbols = stock_service.all_stock_symbols()
# filter out ignore list
stock_ignore_list = ['DD' # Due Diligence
                     ,'LOL' # Laugh Out Loud
                     ,'RH' # Robbinhood
                     ,'FOR' # ???
                     ,'IT'
                     ,'MJ' # michael jordan
                     ]
stock_symbols = list(filter(lambda x : x not in stock_ignore_list, stock_symbols))
#print(stock_symbols)
# get subreddit
subreddit = "wallstreetbets"

# get subreddit hot submissions
hot_submissions = reddit_service.hot_submissions(subreddit)

# # get post's titles
# submissions_titles = reddit_service.get_titles(hot_submissions)

# get post's comments
# (of the form [[string]] or a list of comments per submission
submissions_comments = reddit_service.get_comment_bodys(hot_submissions)

# # get title comment pairs
# title_comments = zip(submissions_titles, submissions_comments)

# text crawl each comment seeking stock symbols and count
# of the form [[[stock symbol string]]]

# raw indicates here that we have not yet tested if they're true stock symbols just yet
submissions_comments_stock_symbols_raw = list(
    map(lambda comments : list(
        map(lambda comment :
            parsing_service.findall_stock_symbols(comment)
            , comments))
        , submissions_comments))

submissions_stock_symbols_raw = functools.reduce(lambda acc, x : acc + x, submissions_comments_stock_symbols_raw)

subreddit_stock_symbols_raw = functools.reduce(lambda acc, x : acc + x, submissions_stock_symbols_raw)

stock_symbol_counts = {}
for raw_stock_symbol in subreddit_stock_symbols_raw:
    if raw_stock_symbol in stock_symbols:
        if raw_stock_symbol in stock_symbol_counts:
            stock_symbol_counts[raw_stock_symbol] += 1
        else:
            stock_symbol_counts[raw_stock_symbol] = 1

graph_service.bar(stock_symbol_counts)
