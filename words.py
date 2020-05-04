import enchant

d = enchant.Dict("en_US")
f = open("combinations.txt", "r")

def process_word(word):
    if d.check(word.strip().upper()):
        with open('realwords.txt', 'a') as the_file:
            the_file.write(" "+word)
for x in f:
    process_word(x)
