def top_n (items, n):
    ''' return top n iteam in an array in desc order.

    Args:
        items (array): list or array-like object.
        n (int): number of items to return.

    return : 
        array top n items in desc order

    Egs: 
        >>> top_n([8,7,2,3,5], 3)
        [8.7,5]

    '''

    for i in range(n) : #keep sorting til we have top n items
        for j in range(len(items)-1-i) : 

            if items[j] > items[j+1]: #if item is larger than next item..
                items[j], items[j+1] = items[j+1], items[j] # swap for two!
    
    #get last 2 items
    top_n = items[-n:]

    # return in desc order..
    return top_n[::-1]
