import random


def generate_number(start_int: int = 0, end_int: int = 100):
    return random.randint(start_int, end_int)


def correct_answer(solution: int, guess: int):
    if solution == guess:
        return True
    return False


def guess_lower_than_sol(solution: int, guess: int):
    return solution > guess  # true if guess is lower than sol
