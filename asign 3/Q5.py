string = "ABCDEFGHIJK"
counter = 1
while (counter < 7):
    print(" "*(counter-1),string[0:11-((counter-1)*2)])
    counter += 1
