from os import linesep

WORDS = []

def load_data():
    print('Loading...')
    try:
        with open('words_bank.txt', 'r') as f:
            big_text = f.read()
            lines = big_text.split('\n')
            print(lines)

            for i in range(0, len(lines), 2):
                WORDS.append({'english':lines[i], 'persian':lines[i+1]})
    except(FileNotFoundError):
        print("words_bank not found")
        exit()
    print('Loaded!')


def check_exist(txt):
    for word in WORDS:
        if txt == word:
            return True
            break;
    else:
        return False;


def add_word(en, fa):
    if check_exist(en) == True:
        print('word is already exist')
        return False
    with open('words_bank.txt', 'a') as f:
        f.write('\n' + en + '\n' + fa)


def split_dot(input_text):
    return input_text.split('. ')
    

def translate_en2fa(input_text):
    sentens = split_dot(input_text)
    output_text = ""
    for line in sentens:
        user_words = line.split(' ')
        for user_word in user_words:
            for WORD in WORDS:
                if user_word == WORD['english']:
                    output_text += WORD['persian'] + " "
                    break
            else:
                output_text += user_word + " "
    return output_text


def translate_fa2en(input_text):
    sentens = split_dot(input_text)
    output_text = ""
    for line in sentens:
        user_words = line.split(' ')
        for user_word in user_words:
            for WORD in WORDS:
                if user_word == WORD['persian']:
                    output_text += WORD['english'] + " "
                    break
            else:
                output_text += user_word + " "
    return output_text


def show_menu():
    print('Welcom to translator')
    print('1- Add Word')
    print('2- Translation english2persian')
    print('3- Translation persian2english')
    print('4- Exit')


load_data()
while True:
    show_menu()
    choice = int(input('Enter your choice: '))

    if choice == 1:
        en = input('en word: ')
        fa = input('fa word: ')
        add_word(en, fa)
    elif choice == 2:
        user_text = input('please write your en text: ')
        output_text = translate_en2fa(user_text)
        print(output_text)
    elif choice == 3:
        user_text = input('please write your fa text: ')
        output_text = translate_fa2en(user_text)
        print(output_text)
    elif choice == 4:
        exit()
