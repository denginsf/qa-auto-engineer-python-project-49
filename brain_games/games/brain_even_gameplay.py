from random import randint


def brain_even_data():
    rule = 'Answer "yes" if the number is even, otherwise answer "no".'
    task = randint(1, 100)   # NOSONAR
    if task % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return rule, task, correct_answer


if __name__ == '__main__':
    brain_even_data()