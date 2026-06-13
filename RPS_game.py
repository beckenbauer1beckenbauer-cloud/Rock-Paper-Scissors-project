import random

def play(player1, player2, num_games, verbose=False):
    p1_prev_play = ""
    p2_prev_play = ""
    p1_wins = 0
    p2_wins = 0
    ties = 0

    for _ in range(num_games):
        p1_play = player1(p2_prev_play)
        p2_play = player2(p1_prev_play)

        if p1_play == p2_play:
            ties += 1
            if verbose:
                print( River, p1_play, "vs", p2_play, "TIED" )
        elif (p1_play == "R" and p2_play == "S") or \
             (p1_play == "P" and p2_play == "R") or \
             (p1_play == "S" and p2_play == "P"):
            p1_wins += 1
            if verbose:
                print( "P1", p1_play, "vs", p2_play, "WON" )
        else:
            p2_wins += 1
            if verbose:
                print( "P2", p1_play, "vs", p2_play, "WON" )

        p1_prev_play = p1_play
        p2_prev_play = p2_play

    games_played = p1_wins + p2_wins + ties
    win_rate = (p1_wins / games_played) * 100

    print(f"Final results: Player 1 won: {win_rate:.1f}%, Player 2 won: {((p2_wins / games_played) * 100):.1f}%, Ties: {((ties / games_played) * 100):.1f}%")
    return win_rate

# --------------------------------------------------------------------------------
# THE FOUR OPPONENT BOTS
# --------------------------------------------------------------------------------

def quincy(prev_play, counter=[0]):
    counter[0] += 1
    choices = ["R", "R", "P", "P", "S"]
    return choices[counter[0] % len(choices)]

def mrugesh(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)
    else:
        opponent_history.clear()

    last_ten = opponent_history[-10:]
    if len(last_ten) == 0:
        return "R"
        
    most_frequent = max(set(last_ten), key=last_ten.count)

    if most_frequent == '':
        most_frequent = "R"

    ideal_transition = {'R': 'P', 'P': 'S', 'S': 'R'}
    return ideal_transition[most_frequent]

def kris(prev_play):
    if not prev_play:
        return "R"
    ideal_transition = {'R': 'P', 'P': 'S', 'S': 'R'}
    return ideal_transition[prev_play]

def abbey(prev_play, opponent_history=[], play_order=[{
    "RR": 0, "RP": 0, "RS": 0,
    "PR": 0, "PP": 0, "PS": 0,
    "SR": 0, "SP": 0, "SS": 0,
}]):
    if not prev_play:
        opponent_history.clear()
        # Reset play order counts for a brand new match setup
        play_order[0] = {k: 0 for k in play_order[0]}
        return "R"

    opponent_history.append(prev_play)

    if len(opponent_history) >= 2:
        last_two = "".join(opponent_history[-2:])
        play_order[0][last_two] += 1

    last_play = opponent_history[-1]
    potential_plays = [
        last_play + "R",
        last_play + "P",
        last_play + "S",
    ]

    sub_order = {
        k: play_order[0][k]
        for k in potential_plays
        if k in play_order[0]
    }

    if not sub_order:
        prediction = "R"
    else:
        prediction = max(sub_order, key=sub_order.get)[-1]

    ideal_transition = {'R': 'P', 'P': 'S', 'S': 'R'}
    return ideal_transition[prediction]
