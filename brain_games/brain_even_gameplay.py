from random import randint

from prompt import string


def be_question() -> int:
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answer = ''
    counter = 0
    while counter != 3:
        number = randint(0, 100)
        if number % 2 == 0:
            correct_answer = 'yes'
        if number % 2 != 0:
            correct_answer = 'no'
        print(f'Question: {number:}')
        answer = string('Your answer: ')
        if answer.lower() == correct_answer.lower():
            print('Correct!')
            counter = counter + 1
        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was {correct_answer}. "
                f"Let's try again, {name}!"
                )
            exit()
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    be_question()