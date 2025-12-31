from constant import Move

def tit_for_tat_pessimistic(opponent_steps, your_steps):
    return Move.CHEAT if (len(opponent_steps) == 0) else opponent_steps[-1]