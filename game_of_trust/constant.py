from enum import IntEnum

class Move(IntEnum):
    CHEAT = 0
    COOPERATE = 1

POINTS_CONSIDERED_AS_WIN = 3

SCORING = {
    (Move.COOPERATE, Move.COOPERATE): (3, 3),
    (Move.CHEAT, Move.COOPERATE): (5, -1),
    (Move.COOPERATE, Move.CHEAT): (-1, 5),
    (Move.CHEAT, Move.CHEAT): (1, 1)
}