import random
import string
import sys


def print_random_password():
    length = random.randint(12, 18)
    characters = string.ascii_letters + string.digits + random.choice('@!#?')
    first_uppercase = random.choice(string.ascii_uppercase)

    required = [random.choice(string.digits), random.choice('@!#?')]
    while(len(required) != length - 1):
        required.append(random.choice(characters))

    random.shuffle(required)
    final_word = ''.join([str(e) for e in required])
    final_word = first_uppercase + final_word
    print(final_word)
    # print(f"Number of ch: {len(final_word)}")

def random_digit_or_special_ch():
    ch = ''
    if (random.randint(0, 1)):
        ch += random.choice('@!#?')
    else:
        ch += random.choice(string.digits)
    return ch

def random_digit_and_special_ch():
    ch = ''
    if (random.randint(0, 1)):
        ch += random.choice('@!#?')
        ch += random.choice(string.digits)
    else:
        ch += random.choice(string.digits)
        ch += random.choice('@!#?')
    return ch

def print_dictionary_password(dictionary_file):
    assembled_password = ''
    first_words = []
    all_words = []
    for i in (open(f"{dictionary_file}", "r").readline().split()):
        if(len(i) > 16):
            continue
        if i[0].isupper():
            first_words.append(i)

        all_words.append(i)

    if(len(first_words) == 0):
        print('Invalid dictionary: Missing uppercase word or the uppercase words are too long')
        return


    copy_of_first_words = first_words
    while(1):
        assembled_password += random.choice(copy_of_first_words)

        if(len(assembled_password) == 16):
            assembled_password += random_digit_and_special_ch()
            break

        other_words = ''
        copy_of_words = all_words

        # Choosing next random words
        while(1):
            if(len(copy_of_words) == 0):
                break

            if(random.randint(0, 1)):
                break

            random_word = random.choice(copy_of_words)
            if(len(random_word) > 16 - len(assembled_password) - len(other_words)):
                copy_of_words.pop(copy_of_words.index(random_word))
            else:
                other_words += random_word


        # If there were no other words picked or they got skipped
        if(len(other_words) == 0):

            # Random for deciding to continue the search for a new pair of upper word with other words
            if (random.randint(0, 1)):
                assembled_password += random_digit_and_special_ch()

                # Checks the required minimal length
                length = len(assembled_password)
                if(length < 12):
                    length = random.randint(12, 18)
                else:
                    # print(f"Length: {length}  Pass: {assembled_password}")
                    length = random.randint(len(assembled_password), 18)

                # Fills the rest of the password with numbers and special characters up to the random length
                while(len(assembled_password) != length):
                    assembled_password += random_digit_or_special_ch()

                break

            else:
                # If there are more then one uppercase words in the list
                if(len(copy_of_first_words) != 1):
                    # Removes the current uppercase word from the list
                    copy_of_first_words.pop(copy_of_first_words.index(assembled_password))

                assembled_password = ''

        # Combines the uppercase word with the other words picked and random digits and special characters
        else:

            # Random for deciding the order for the digits and special characters and the other words
            required = [other_words, random.choice('@!#?'), random.choice(string.digits)]
            random.shuffle(required)
            for i in required:
                assembled_password += i

            # Checks the required minimal length
            length = len(assembled_password)
            if (length < 12):
                length = random.randint(12, 18)
            else:
                length = random.randint(len(assembled_password), 18)

            # Fills the rest of the password with numbers and special characters up to the random length
            while (len(assembled_password) != length):
                assembled_password += random_digit_or_special_ch()
            break


    print(assembled_password)
    # print(f"Number of ch: {len(assembled_password)}")


if __name__ == '__main__':

    if len(sys.argv) == 1:
        print_random_password()
    elif sys.argv[1] == "-use_dict":
        dictionary_file = sys.argv[2]
        print_dictionary_password(dictionary_file)
    else:
        print("Unknown command")
