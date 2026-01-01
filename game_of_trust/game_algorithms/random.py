from constant import Move, SCORING, POINTS_CONSIDERED_AS_WIN
import random

def random(opponent_steps, your_steps):
    return random.choice([Move.COOPERATE, Move.CHEAT])