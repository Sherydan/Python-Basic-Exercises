word = input('Give me a word: ')
word_list = list(word)
word_list.reverse()

str1 = ''.join(word_list)

if str1 == word:
    print(f'your word {word} is a palindrome')