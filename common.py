import enchant

d = enchant.Dict("en_US")
f = open("thousand-most-common-english-words.txt", "r")

def process_word(word):
    word = word.upper().strip()
    if len(word) == 4:
        index = open('realwords.txt', 'r').read().find(word)
        if index > 0:
            with open('commonwords.txt', 'a') as the_file:
                the_file.write(" "+word+"\n")

for x in f:
    process_word(x)
