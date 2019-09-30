# Skrifið forrit sem skrifar út hversu oft
# tiltekinn stafur kemur fyrir í tiltekinni skrá
# og í hversu mörgum orðum stafurinn kemur fyrir.
# Ekki skal gerður greinarmunur á há- og lágstöfum.
# Bæði stafurinn og skráarnafnið eru slegin inn af notanda.

# 1. Lesa skráarnafn frá notanda
# 2. Lesa staf frá notanda
# 3. Opna skrá
# 4. Meðhöndla skrá
# 5. Prenta út upplýsingar

def read_filename():
    name = input("Enter a filename: ")
    return name

def read_char():
    ch = input("Enter a single character: ")
    return ch

def open_file(filename):
    file_object = open(filename, 'r')
    return file_object #hér í þessu falli gætum við notað try except dótið

def count_ch_in_word(user_ch, word):
    counter = 0
    for ch in word:
        if ch == user_ch:
            counter += 1
    return counter

def process_file(file_object, ch):
    # Lesa skrá línu fyrir línu
    # Brjóta línu upp í einstök orð
    # Telja hversu oft stafur kemur fyrir í orðum
    # Telja hversu oft stafur kemur fyrir í skránni í heild sinni
    ch_count = 0
    word_count = 0
    for line in file_object:
        word_list = line.split()
        for word in word_list:
            count_in_word = count_ch_in_word(ch, word)
            ch_count += count_in_word
            if count_in_word > 0:
                word_count +=1
    return ch_count, word_count
def print_results(ch, ch_count, word_count):
    print('The letter {} appears {} times'.format(ch, ch_count))
    print('The letter {} appears in {} words'.format(ch, word_count))
def main():
    filename = read_filename()

    ch = read_char()

    file_object = open_file(filename)

    ch_count, word_count = process_file(file_object, ch)

    print_results(ch, ch_count, word_count)

main()