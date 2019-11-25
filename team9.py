team_name = 'Anders a bonobo'
strategy_name = 'Top 10 anime betrayals'
strategy_description = 'Collude, then when bertraied, betray a crap ton.'

def move(my_history, their_history, my_score, their_score):
 
    if 'b' in their_history:
        return 'b' 
    else:  
        return 'c'
        
'''take the play based on what there history was previous.
    
    history: i will collude utill i am betraied, then i will do nothing but
    betray. The program will choose c untill the oppint does b, then i will do 
    nothing but b for the rest of the program/game. So play nice untill they 
    don't then go off and betray them a lot. 
    Returns 'c' or 'b' for collude or betray.
    '''
    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='b'):
         print('Test passed')
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbb',
              their_history='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b')             