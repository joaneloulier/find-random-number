import random

def generate_number(start_int: int = 0, end_int: int = 100):
    return random.randint(start_int, end_int)

def correct_answer(solution: int, guess: int):
    if solution == guess:
        return True
    return False

def higher_or_lower(solution: int, guess: int):
    if solution > guess:
        return 'guess_lower_than_sol'
    else:
        return 'guess_higher_than_sol'