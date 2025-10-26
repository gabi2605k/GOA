def index_of_max(lst):
    if not lst:  
        return None
    max_num = max(lst)
    return lst.index(max_num)