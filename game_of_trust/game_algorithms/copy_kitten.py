from constant import Move, SCORING, POINTS_CONSIDERED_AS_WIN

def copy_kitten(opponent_steps, your_steps):
    if len(opponent_steps) < 2:
        return Move.COOPERATE
    
    if Move.COOPERATE not in opponent_steps[-2:]:
        return Move.CHEAT
    
    return Move.COOPERATE