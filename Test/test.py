from MyPackage import mymodule

def test_top_n():
    '''
    make sure top_n works correctly
    '''

    assert mymodule.top_n([8,3,2,7,4],3) == [8,7,4], 'Incorrect'
    assert mymodule.top_n([7,9,1,0],3) == [9,7,1], 'Incorrect'
    assert mymodule.top_n([11,2,1,30],3) == [30,11,2], 'Incorrect'