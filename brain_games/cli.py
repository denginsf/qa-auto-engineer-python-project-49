from prompt import string
def welcome_user() -> str:
    name = string('May I have your name? ')
    return name

if __name__ == '__main__':
    welcome_user()