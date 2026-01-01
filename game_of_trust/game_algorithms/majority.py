from constant import Move
import Counter


def go_by_majority_optimistic(opponent_steps, ur_steps):
    opponent_steps_dict = Counter(opponent_steps)

    cooperation_by_opponent, cheat_by_opponent = opponent_steps_dict.get(Move.COOPERATE, 0), opponent_steps_dict.get(Move.CHEAT, 0)

    if cooperation_by_opponent >= cheat_by_opponent:
        return Move.COOPERATE

    return Move.Cheat

def go_by_majority_pessimistic(opponent_steps, your_steps):
    opponent_steps_dict = Counter(opponent_steps)

    cooperation_by_opponent, cheat_by_opponent = opponent_steps_dict.get(Move.COOPERATE, 0), opponent_steps_dict.get(Move.CHEAT, 0)

    if cooperation_by_opponent > cheat_by_opponent:
        return Move.COOPERATE

    return Move.Cheat