def score(pl_one, pl_two):
    names = ['Player 1', 'Player 2']
    scores = ['love', '15', '30', '40', 'set']
    ties = ['Love all', '15 all', '30 all', 'Duce', 'set']

    # Are we looking for a winner
    if (pl_one < 4)  and (pl_two < 4):
        # are we tied?
        if (pl_one == pl_two):
            return [ties[pl_one], False ]
        else:
            return [scores[pl_one] + ' : ' + scores[pl_two], False ]
    else:
        dif = abs(pl_one - pl_two)
        if dif == 0 :
            return ['Duce', False ]
        elif dif == 1 :
            pos = 'Advantage'
            if pl_one > pl_two:
                return [names[0] + ' ' + pos, False]
            else:
                return [names[1] + ' ' + pos, False]
        else:
            pos = 'Winner'
            if pl_one > pl_two:
                return [names[0] + ' ' + pos, True]
            else:
                return [names[1] + ' ' + pos, True]
        




print(score (0,0)[0])
print(score (0,1)[0])
print(score (0,2)[0])
print(score (0,3)[0])
print(score (0,4)[0])
print(score (5,5)[0])
print(score (6,5)[0])
print(score (7,5)[0])
