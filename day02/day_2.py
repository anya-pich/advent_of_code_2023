with open('day_2.txt') as f:
    lines = f.readlines()
    # A X for Rock, defeats scissors and scores 1
    # B Y for Paper, defeats rock and scores 2
    # C Z for Scissors, defeats paper and scores 3
    # theirs = ['a', 'b', 'c']
    # mine = ['x', 'y', 'z']
    # my_total_score = 0
    # for line in lines:
    #     their_letter, my_letter = line.lower().strip().split(' ')
    #     they = theirs.index(their_letter)
    #     me = mine.index(my_letter)
    #     my_score = me + 1
    #     if they == me:
    #         my_score += 3
    #     if me - 1 == they or (me == 0 and they==2):
    #         my_score += 6
    #     my_total_score += my_score
    # print(my_total_score)

    shapes = ['a', 'b', 'c'] # rock, paper, scissors
    outcomes = ['x', 'y', 'z'] # lose, draw, win
    my_total_score = 0
    for line in lines:
        their_letter, outcome_letter = line.lower().strip().split(' ')
        they = shapes.index(their_letter)
        outcome = outcomes.index(outcome_letter) - 1
        me = (they + outcome)%3
        my_score = 6 if outcome == 1 else 3 if outcome == 0 else 0
        my_score += me + 1
        my_total_score += my_score
    print(my_total_score)