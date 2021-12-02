import random
import string


def print_random_password():
    length = random.randint(12, 18)
    characters = string.ascii_letters + string.digits + random.choice('@!#?')
    first_uppercase = random.choice(string.ascii_uppercase)
    random_symbol_pos = random.randint(0, 15)
    rest_of_the_word = ''

    for i in range(length - 2):
        rest_of_the_word = rest_of_the_word + random.choice(characters)

    final_rest_of_the_word = rest_of_the_word[:random_symbol_pos] + random.choice('@!#?') + rest_of_the_word[
                                                                                            random_symbol_pos:]
    final_word = first_uppercase + final_rest_of_the_word

    print(final_word)


def print_dictionary_password():
    length = random.randint(12, 18)
    password_length = 0
    assembled_password = ''
    is_first_word_valid = False
    while not is_first_word_valid:
        random_first_word = random.choice(open("dictionar.txt", "r").readline().split())
        if random_first_word[0].isupper():
            is_first_word_valid = True

    while password_length <= length - len(random_first_word):

        random_word = random.choice(open("dictionar.txt", "r").readline().split())
        assembled_password = assembled_password + random.choice(open("dictionar.txt", "r").readline().split()) + ' '
        password_length = len(assembled_password.replace(' ', ''))
        print('length', length)
        print('firstword', len(random_first_word))
        print(password_length)
        if password_length > length - len(random_first_word):
            for i in range(length - len(random_first_word)):
                if assembled_password[i] == ' ':
                    assembled_password_symbol = assembled_password[:i] + random.choice('@!#?') + assembled_password[i:]
            final_assembled_password = (assembled_password_symbol.removesuffix(random_word)).replace(' ', '')

    final_final_password = random_first_word + final_assembled_password
    print(final_final_password)


if __name__ == '__main__':
    print_random_password()
    print_dictionary_password()
