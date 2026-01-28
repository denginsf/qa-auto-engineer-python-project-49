from prompt import string


def game_engine(get_data):
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    rule, task, correct_answer = get_data()
    print(rule)
    counter = 0
    while counter != 3:
        _, task, correct_answer = get_data()
        print(f'Question: {task}')
        answer = string('Your answer: ')
        if answer.lower() == correct_answer:
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