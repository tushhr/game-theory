from constant import Move

def grudger(opponent_steps, your_steps):
    if len(opponent_steps) == 0:
        return Move.COOPERATE
    
    if Move.CHEAT in opponent_steps:
        return Move.CHEAT
    
    return Move.COOPERATE