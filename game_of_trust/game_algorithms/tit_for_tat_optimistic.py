from constant import Move

def tit_for_tat_optimistic(opponent_steps, your_steps):
    return Move.COOPERATE if (len(opponent_steps) == 0) else opponent_steps[-1]