# -*- coding: utf-8 -*-
####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Chimera'
strategy_name = 'Luar'
strategy_description = ''' Betrayed by the words they said. The bot will scan the opponenets previuos three actions and 
determine its next action based off what they opponent has done recently'''
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history of this player.
    Returns 'c' or 'b' for collude or betray.
    '''
    '''
    if 'b' in their_history:
        return 'b'
    else:
        return 'c'
    '''
    
    if len(their_history) >= 3:
        opponents_recent_moves = [their_history[-1],their_history[-2],their_history[-3] ]
    b_count = 0
    if len(their_history) < 3:
        return 'b'
    else:
        for moves in opponents_recent_moves:
            if 'b' in opponents_recent_moves:
                b_count += 1
                if b_count >= 2:
                    return 'b'
                else:
                    return 'c'     
    
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
              result= 'b' )