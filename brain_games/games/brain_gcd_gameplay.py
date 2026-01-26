from random import randint


def brain_gcd_data():
    x1 = randint(1, 1000)
    x2 = randint(1, 1000)
    rule = 'Find the greatest common divisor of given numbers.'
    task = f'{x1} {x2}'
    while x2 != 0:
        remainder = x1 % x2
        x1 = x2
        x2 = remainder
    correct_answer = x1
    return rule, task, str(correct_answer)


if __name__ == '__main__':
    brain_gcd_data()