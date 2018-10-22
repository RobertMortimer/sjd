import random

def score(pl_one, pl_two):
    names = ['Player 1', 'Player 2']
    scores = ['love', '15', '30', '40', 'set']
    ties = ['Play', '15 all', '30 all', 'Duce', 'set']

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
        

#for x in range(10):
#  print( random.randint(0,1))

pl1 = 0
pl2 = 0
print('Game on!')
while score(pl1,pl2)[1] == False:
    print(score (pl1,pl2)[0])
    if random.randint(0,1) == 1:
        pl1 += 1 
    else:
        pl2 += 1
print(score (pl1,pl2)[0])


# print(score (0,0)[0])
# print(score (0,1)[0])
# print(score (0,2)[0])
# print(score (0,3)[0])
# print(score (0,4)[0])
# print(score (5,5)[0])
# print(score (6,5)[0])
# print(score (7,5)[0])
