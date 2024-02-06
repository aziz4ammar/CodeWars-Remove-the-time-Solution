def shorten_to_date(long_date):
    index = long_date.index(',')
    return long_date[:index]