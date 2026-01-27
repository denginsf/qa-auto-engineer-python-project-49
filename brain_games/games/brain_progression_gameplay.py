from random import randint


def create_progression():
    start = randint(1, 100)
    step = randint(2, 10)
    progression_range = 10
    progression = []
    for n_index in range(progression_range):
        current_element = start + n_index * step
        progression.append(str(current_element))
    return progression


def brain_progression_data():
    rule = 'What number is missing in the progression?'
    start_progression = create_progression()
    which_remove = randint(0, 9)
    correct_answer = start_progression[which_remove]
    start_progression[which_remove] = '..'
    task = ' '.join(start_progression)
    return rule, task, str(correct_answer)


if __name__ == '__main__':
    brain_progression_data()