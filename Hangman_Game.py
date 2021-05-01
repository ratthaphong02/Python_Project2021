from random_word import RandomWords
rw = RandomWords()
c = str(rw.get_random_word(hasDictionaryDef="true", includePartOfSpeech="noun",  minDictionaryCount=1, maxDictionaryCount=2, minLength=2, maxLength=4))
print("This word has : ", len(c), "Char")
print(c)
for i in range(6):
    char = input("Guess Your Character : ")
    if char in c:
        print("Right", i)
        # for R in range(len(c)):
        #     if R == len(c) - 1:
        #         break
    else:
        print("Wrong", i)
print(c)

