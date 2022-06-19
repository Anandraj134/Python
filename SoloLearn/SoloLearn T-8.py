def main():
    phrase = input()
    wordcount = 0
    lettercount = 0
    for word in phrase.split():
        lettercount = lettercount + len(word)
        wordcount = wordcount + 1

    print(lettercount/wordcount)

main()