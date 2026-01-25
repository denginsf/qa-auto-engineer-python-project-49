from random import choice, randint


def brain_calc_data():
    x1 = randint(0, 100)
    x2 = randint(0, 100)
    expressions = ['+', '-', '*']
    random_expression = choice(expressions)
    rule = 'What is the result of the expression?'
    task = f'{x1} {random_expression} {x2}'
    match random_expression:
        case '+':
            correct_answer = x1 + x2
        case '-':
            correct_answer = x1 - x2
        case '*':
            correct_answer = x1 * x2
    return rule, task, str(correct_answer)


if __name__ == '__main__':
    brain_calc_data()