from random import randint


def brain_prime_data():
    number_for_task = randint(0, 100) #NOSONAR
    rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    task = f'{number_for_task}'
    root = int(number_for_task ** 0.5)
    if number_for_task < 2:
        correct_answer = 'no'
    else:
        for i in range(2, root + 1):
            if number_for_task % i == 0:
                correct_answer = 'no'
                break
        else:
            correct_answer = 'yes'
    return rule, task, correct_answer


if __name__ == '__main__':
    brain_prime_data()