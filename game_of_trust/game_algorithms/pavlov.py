from constant import Move, SCORING, POINTS_CONSIDERED_AS_WIN


def pavlov(opponent_steps, your_steps):
    if not opponent_steps:
        return Move.COOPERATE
    
    opponent_last_move = opponent_steps[-1]
    your_last_move = your_steps[-1]

    _, your_last_score = SCORING[(opponent_last_move, your_last_move)]

    if your_last_score >= POINTS_CONSIDERED_AS_WIN:
        return your_last_move

    return Move.COOPERATE if your_last_move == Move.CHEAT else Move.CHEAT