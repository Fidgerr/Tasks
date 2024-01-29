def rps_game_winner(array):
    strategy = ['R', 'P', 'S']
    if len(array) != 2:
        print('WrongNumberOfPlayersError')
    else:
        p1 = array[0]
        p2 = array[1]
        if p1[1] in strategy and p2[1] in strategy:
            if p1[1] == p2[1]:
                print("'", *p1, "'")
            else:
                if p1[1] == 'P' and p2[1] == 'R':
                    print("'", *p1, "'")
                elif p1[1] == 'P' and p2[1] == 'S':
                    print("'", *p2, "'")
                elif p1[1] == 'R' and p2[1] == 'S':
                    print("'", *p1, "'")
                elif p1[1] == 'R' and p2[1] == 'P':
                    print("'", *p2, "'")
                elif p1[1] == 'S' and p2[1] == 'P':
                    print("'", *p1, "'")
                elif p1[1] == 'S' and p2[1] == 'R':
                    print("'", *p2, "'")
        else:
            print('NoSuchStrategyError')


rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']])
rps_game_winner([['player1', 'P'], ['player2', 'A']])
rps_game_winner([['player1', 'P'], ['player2', 'S']])
rps_game_winner([['player1', 'P'], ['player2', 'P']])
