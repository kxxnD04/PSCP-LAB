"""Time To Travel"""
TOWNN = {chr(i):[(i-65)*100+1000, None] for i in range(65, 89)}
BOARD = ["start", 'A', 'B', 'C', 'D', 'E', 'F', 'stop', 'G', 'H', 'I', 'J', 'K', 'L', 'landmark',
'M', 'N', 'O', 'P', 'Q', 'R', 'travel', 'S', 'T', 'U', 'V', 'W', 'X']
def check_winner(p1: dict, p2: dict) -> None:
    """check who win and print the answer"""
    if p1['money'] > p2['money']:
        print('P1')
        print(f"{p1['money']:.2f}")
        if p1['own_town']:
            print(*sorted(p1['own_town'], key=lambda x: TOWNN[x][0])[::-1])
    elif p2['money'] > p1['money']:
        print('P2')
        print(f"{p2['money']:.2f}")
        if p1['own_town']:
            print(*sorted(p2['own_town'], key=lambda x: TOWNN[x][0])[::-1])
    else:
        print("Draw")

def take_action(player: dict, walk:int, starting: int) -> None:
    """take all player action"""
    if player["pos"] + walk >= 28:
        player["money"] += (starting/2)
    player["pos"] = (player["pos"] + walk)%28
    if player['pos'] == 7:
        player["is_stop"] = True
    elif player['pos'] == 14:
        if player["own_town"]:
            choose_lm = input().split()[1]
            TOWNN[choose_lm][0] *= 2
    elif player['pos'] == 21:
        player["is_travel"] = True
    elif player['pos']:
        if TOWNN[BOARD[player['pos']]][1] is None:
            if player['money'] >= 0.7*TOWNN[BOARD[player['pos']]][0]:
                player["own_town"] += [BOARD[player['pos']]]
                TOWNN[BOARD[player['pos']]][1] = player
                player['money'] -= (0.7*TOWNN[BOARD[player['pos']]][0])
        else:
            player['money'] -= (0.7*TOWNN[BOARD[player['pos']]][0])
            TOWNN[BOARD[player['pos']]][1]["money"] += (0.7*TOWNN[BOARD[player['pos']]][0])

def take_stop_action(player:dict, starting: int, action: str) -> None:
    """make a stop action"""
    if action[1].lower() == 'pay':
        player['is_stop'] = False
        player['money'] -= (0.1*player['money'])
        addition_roll = input().strip().split()
        take_action(player, int(addition_roll[1]) + int(addition_roll[2]), starting)
    elif action[1] == action[2]:
        player['is_stop'] = False
        take_action(player, int(action[1])*2, starting)

def main():
    """Time To Travel"""
    starting = int(input())
    turn = int(input())
    p1 = {"pos": 0, "money": starting, "own_town": [], "is_stop": False, "is_travel": False}
    p2 = {"pos": 0, "money": starting, "own_town": [], "is_stop": False, "is_travel": False}
    while p1["money"] > 0 and p2['money'] > 0 and turn:
        end_round = 0
        while end_round != 2:
            action = input().strip().split()
            if action[0] == "P1":
                if p1['is_stop']:
                    take_stop_action(p1, starting, action)
                elif p1['is_travel']:
                    dsc = BOARD.index(action[-1])
                    diff = (dsc - 21) + ((dsc < 21)*28)
                    p1['is_travel'] = False
                    take_action(p1, diff, starting)
                else:
                    take_action(p1, int(action[1]) + int(action[2]), starting)
            else:
                if p2['is_stop']:
                    take_stop_action(p2, starting, action)
                elif p2['is_travel']:
                    dsc = BOARD.index(action[-1])
                    diff = (dsc - 21) + ((dsc < 21)*28)
                    p2['is_travel'] = False
                    take_action(p2, diff, starting)
                else:
                    take_action(p2, int(action[1]) + int(action[2]), starting)
            end_round += 1
        turn -= 1
    check_winner(p1, p2)
main()
