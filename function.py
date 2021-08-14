def countWordsFromFile () :
    fileName = input("Enter the file Name : ")
    numberOfWords = 0
    file = open(fileName,"r")

    for line in file :
        words  = line.split()
        numberOfWords = numberOfWords+len(words)

    print("Number of words in the given file are : ")
    print(numberOfWords)

countWordsFromFile()