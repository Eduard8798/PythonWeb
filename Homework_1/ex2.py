#Translate

word = "English"
translation = "Franch"
print('This is  dictionary')
dictionary = [
    {
    "word":word,
    "translation":translation
    }
]

def wordTranslate(dictionary):
    for i in dictionary:
        print(i)

def addWord(dictionary):
    word = input("Enter a word English: ")
    translation = input("Enter a translation Franch: ")
    dictionary.append({"word": word, "translation": translation})
    wordTranslate(dictionary)

def deleteWord(dictionary):
    word = input("Enter a word English: ")
    for i in dictionary:
        if i["word"] == word:
            i.remove({"word": word, "translation": translation})
    wordTranslate(dictionary)

def searchWord(dictionary):
    for i in dictionary:
        if i["word"] == word:
            print(i["translation"])

def editWord(dictionary):
    word = input("Enter a word English: ")

    for i in dictionary:
        if i["word"] == word:
            new_word = input("Enter a word English change: ")
            new_transl = input("Enter a translation Franch change: ")
            i["word"]=new_word
            i["translation"]=new_transl
            print(f"The word '{word}' has been updated.")
            wordTranslate(dictionary)
            return


addWord(dictionary)

editWord(dictionary)