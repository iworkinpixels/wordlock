f = open("realwords.txt", "r")

def process_word(word):
    word = word.upper().strip()
    if len(word) == 4:
        index = open('thousand-most-common-english-words.txt', 'r').read().find(word)
        if index < 0:
            with open('uncommonwords.txt', 'a') as the_file:
                the_file.write(" "+word+"\n")

for x in f:
    process_word(x)
