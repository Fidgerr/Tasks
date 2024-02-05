def rps_game_winner(array):
    strategy = ['R', 'P', 'S']
    if len(array) != 2:
        raise Exception('WrongNumberOfPlayersError')
    else:
        p1 = array[0]
        p2 = array[1]
        if p1[1] in strategy and p2[1] in strategy:
            a = ''
            if p1[1] == p2[1]:
                a += p1[0] + ' ' + p1[1]
                return a
            else:
                if p1[1] == 'P' and p2[1] == 'R':
                    a += p1[0] + ' ' + p1[1]
                    return a
                elif p1[1] == 'P' and p2[1] == 'S':
                    a += p2[0] + ' ' + p2[1]
                    return a
                elif p1[1] == 'R' and p2[1] == 'S':
                    a += p1[0] + ' ' + p1[1]
                    return a
                elif p1[1] == 'R' and p2[1] == 'P':
                    a += p2[0] + ' ' + p2[1]
                    return a
                elif p1[1] == 'S' and p2[1] == 'P':
                    a += p1[0] + ' ' + p1[1]
                    return a
                elif p1[1] == 'S' and p2[1] == 'R':
                    a += p2[0] + ' ' + p2[1]
                    return a
        else:
            raise Exception('NoSuchStrategyError')
