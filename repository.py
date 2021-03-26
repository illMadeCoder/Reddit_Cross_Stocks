import pymongo
try:
    myclient = pymongo.MongoClient("mongodb://mongoadmin:secret@localhost:27888/?authSource=admin")
    mydb = myclient["reddit_cross_stocks"]    
except pymongo.errors.ServerSelectionTimeoutError as err:
    print(err)
    
