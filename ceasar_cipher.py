import time

eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

def ceasar(text, step, eng, cipher):
    s = ''
    if eng:
        if cipher:
            for i in range(len(text)):
                if text[i].isalpha() and text[i].isupper():
                    s += eng_upper_alphabet[(eng_upper_alphabet.find(text[i]) + step)%26]
                elif text[i].isalpha() and text[i].islower():
                    s += eng_lower_alphabet[(eng_lower_alphabet.find(text[i]) + step)%26]
                else:
                    s += text[i]
        else:
            for i in range(len(text)):
                if text[i].isalpha() and text[i].isupper():
                    s += eng_upper_alphabet[(eng_upper_alphabet.find(text[i]) - step)%26]
                elif text[i].isalpha() and text[i].islower():
                    s += eng_lower_alphabet[(eng_lower_alphabet.find(text[i]) - step)%26]
                else:
                    s += text[i]
    else:
        if cipher:
            for i in range(len(text)):
                if text[i].isalpha() and text[i].isupper():
                    s += rus_upper_alphabet[(rus_upper_alphabet.find(text[i]) + step)%32]
                elif text[i].isalpha() and text[i].islower():
                    s += rus_lower_alphabet[(rus_lower_alphabet.find(text[i]) + step)%32]
                else:
                    s += text[i]
        else:
            for i in range(len(text)):
                if text[i].isalpha() and text[i].isupper():
                    s += rus_upper_alphabet[(rus_upper_alphabet.find(text[i]) - step)%32]
                elif text[i].isalpha() and text[i].islower():
                    s += rus_lower_alphabet[(rus_lower_alphabet.find(text[i]) - step)%32]
                else:
                    s += text[i]
    return s

def user_interact():
    print("Enter 'yes' if you want to cipher text, 'no' if decipher:")
    a = input().lower()
    while not (a.startswith('y') or a.startswith('n')):
        print('Invalid response')
        a = input().lower()
    
    if a.startswith('y'):
        cipher = True
    else:
        cipher = False
    
    print("What language? Enter 'en' or 'ru':")
    a = input().lower()
    while not (a.startswith('en') or a.startswith('ru')):
        print('Invalid response')
        a = input().lower()
    
    if a.startswith('en'):
        eng = True
    else:
        eng = False
        
    print("Enter the text:")
    text = input()
    
    if cipher:
        print("Enter the step of ciphering:")
    else:
        print("Enter the step of deciphering:")
    st = input()
    while st.isdigit()==False:
        print("Enter a number!")
        st = input()
    st = int(st)
    
    time.sleep(0.5)
    for _ in range(3):
        if cipher:
            print('Ciphering...')
        else:
            print('Deciphering...')
        time.sleep(1)
    
    print(ceasar(text, st, eng, cipher))
    
    print('Do you want to continue ciphering? (yes/no):')
    a = input().lower()
    while not a.startswith('y') and not a.startswith('n'):
        print('Invalid response')
        a = input().lower()
    if a.startswith('y'):
        return True
    else:
        return False

while user_interact()==True:
    user_interact()