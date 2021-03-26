import re

# stock symbols are indicated by a word with at least two
# uppercase letters (there are one letter stocks but for the
# sake of perfomance we ignore those for now) and are optionally
# followed by or lead by a $
re_stock_symbol = r'\b\$?[A-Z]{2}[A-Z]?\$?\b'

def findall_stock_symbols(s):
    return re.findall(re_stock_symbol, s)
