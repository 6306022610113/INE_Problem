"""
Test.assert_equals(chess_board('a1'), 'black')
Test.assert_equals(chess_board('e5'), 'black')
Test.assert_equals(chess_board('d1'), 'white')
Test.assert_equals(chess_board('c7'), 'black')
Test.assert_equals(chess_board('h5'), 'white')
Test.assert_equals(chess_board('g2'), 'white')
Test.assert_equals(chess_board('b3'), 'white')
Test.assert_equals(chess_board('f6'), 'black')
Test.assert_equals(chess_board('g5'), 'black')
"""

def chess_board(index):
    index_board =['a','b','c','d','e','f','g','h'] 
    c = index_board.index(index[0]) + int(index[1])
    if c % 2 == 0:
        return 'white'
    else:
        return  'black'




print(chess_board('a1'))
print(chess_board('e5'))
print(chess_board('d1'))


