def find_winner(yundongyuan):
    rounds = [(i, yundongyuan[i]) for i in range(len(yundongyuan))]
    while len(rounds) > 2:
        next_rounds = []
        for i in range(0, len(rounds) - 1, 2):
            if rounds[i][1] == rounds[i + 1][1]:
                next_rounds.append(rounds[i])
            elif rounds[i][1] > rounds[i + 1][1]:
                next_rounds.append(rounds[i + 1])
            else:
                next_rounds.append(rounds[i] if rounds[i][0] < rounds[i + 1][0] else rounds[i + 1])

        if len(rounds) % 2 == 1:
            next_rounds.append(rounds[-1])
        rounds = next_rounds
    
    if rounds[0][1] > rounds[1][1]:
        winner, runnerup = rounds[0], rounds[1]

    elif rounds[0][1] < rounds[1][1]:
        winner, runnerup = rounds[1], rounds[0]
    else:
        winner, runnerup = (rounds[0], rounds[1]) if rounds[0][0] < rounds[1][0] else (rounds[1], rounds[0])
    return winner[0], runnerup[0]

yundongyuan = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
winner, runnerup = find_winner(yundongyuan)
print({winner}, {runnerup})





