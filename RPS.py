def player(prev_play, opponent_history=[]):
    # 1. Handle the very first game where prev_play is empty
    if prev_play:
        opponent_history.append(prev_play)
    else:
        opponent_history.clear() # Clear state for a brand new match reset

    # 2. Strategy: Markov Chain / N-gram frequency tracking
    # We look at the last 3 moves to predict the 4th move of the opponent
    n = 3
    
    # Pre-defined ideal counters for each predicted move
    ideal_counter = {'R': 'P', 'P': 'S', 'S': 'R'}
    
    # Default fall-back move if we don't have enough history data yet
    guess = 'R'

    if len(opponent_history) >= n:
        # Get the recent sequence of moves of the opponent
        recent_sequence = "".join(opponent_history[-(n):])
        
        # Look behind at the history to count what usually follows this sequence
        potential_sequences = {
            recent_sequence + 'R': 0,
            recent_sequence + 'P': 0,
            recent_sequence + 'S': 0
        }
        
        # Scan history and populate frequencies
        history_str = "".join(opponent_history)
        for sub_seq in potential_sequences.keys():
            potential_sequences[sub_seq] = history_str.count(sub_seq)
            
        # Predict the opponent's next move based on the highest frequency
        predicted_move = max(potential_sequences, key=potential_sequences.get)[-1]
        
        # Play the winning counter move
        guess = ideal_counter[predicted_move]

    return guess
