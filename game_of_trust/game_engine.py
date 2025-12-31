from collections import defaultdict
from game_algorithms.pavlov import pavlov
from game_algorithms.copy_kitten import copy_kitten
from game_algorithms.grudger import grudger
from game_algorithms.tit_for_tat_optimistic import tit_for_tat_optimistic
from game_algorithms.tit_for_tat_pessimistic import tit_for_tat_pessimistic
from constant import SCORING

NUMBER_OF_ROUNDS = 200
STRATEGIES = [
    tit_for_tat_optimistic,
    tit_for_tat_pessimistic,
    grudger,
    pavlov,
    copy_kitten
]

def run_tournament():
    leaderboard = defaultdict(int)

    # I want to make sure both strategies plays against each other twice
    # twice to make sure no one gets the benefit of being the first player
    for strategy_a in STRATEGIES:
        for strategy_b in STRATEGIES:
            score_a, score_b = run_match(strategy_a, strategy_b, NUMBER_OF_ROUNDS)

            leaderboard[strategy_a.__name__] += score_a

    return leaderboard

def run_match(player_a, player_b, num_of_rounds):
    history_a = []
    history_b = []

    score_a, score_b = 0, 0

    for _ in range(num_of_rounds):
        move_a = player_a(history_b, history_a)
        move_b = player_b(history_a, history_b)

        history_a.append(move_a)
        history_b.append(move_b)

        sa, sb = SCORING[(move_a, move_b)]

        score_a += sa
        score_b += sb
    
    return score_a, score_b

leaderboard = run_tournament()

for strategy, score in leaderboard.items():
    print(f"{strategy}: {score}")