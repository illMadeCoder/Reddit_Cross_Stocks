import repository
import finnhub

finnhub_client = finnhub.Client(api_key="sandbox_c19r0kv48v6tl8v9nl8g")

# will test if repo contains stock info otherwise it will hit api and cache repo for next time
# currently has no means of updating after the initial cache
def all_stock_symbols():
    repository.mycol = repository.mydb["stocks"]
    db_symbols = list(repository.mycol.find({},{"displaySymbol":1}))

    if len(db_symbols) > 0: # previously cached
        return list(map(lambda x : x["displaySymbol"], db_symbols))
        print("stocks previously cached")
    else: # not yet cached
        print("stocks not cached, hitting api")
        api_symbols = list(map(lambda x : x["displaySymbol"], finnhub_client.stock_symbols("US")))
        # cache for next time
        repository.mycol.insert_many(list(map(lambda x : {"displaySymbol":x}, api_symbols)))
        return api_symbols
