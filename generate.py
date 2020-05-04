wheel1 = ["R","S","T","L","N","B","D","M","J","P"]
wheel2 = ["R","T","L","H","A","E","I","O","U","Y"]
wheel3 = ["R","S","T","L","N","A","C","D","E","O"]
wheel4 = ["R","S","T","L","N","E","D","H","K","Y"]

for x in wheel1:
    for y in wheel2:
        for z in wheel3:
            for a in wheel4:
                with open('combinations.txt', 'a') as the_file:
                    the_file.write(x+y+z+a+"\n")
