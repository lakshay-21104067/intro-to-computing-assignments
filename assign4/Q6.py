def anagram(word):
    if len(word)==1:
        return [word];
    partial_words=anagram(word[1:])
    char=word[0]
    mylist=[]
    for perm in partial_words:
        for i in range(len(perm)+1):
            mylist.append(perm[:i]+char+perm[i:])
    return mylist       


George_word=input("Enter the word by George:")
Possible_words=anagram(George_word)
Barbie_word=input("Enter word by Barbie:")


if Barbie_word in Possible_words:
    print("real friend")
else:
    print("fake friend")
