def longest_word_in_file(file_name):
    file = open(file_name ,'r')
    max_word = ''
    for line in file:
        words = line.split()
        for word in words:
            word_without_punc = remove_puctuation(word)
            if len(word_without_punc) >= len(max_word):
                max_word =  word_without_punc
        return max_word

from string import punctuation
def remove_puctuation(word):
    for punc in punctuation:
        if punc in word:
           word = word.replace(punc,'')
    return word


print(longest_word_in_file('romeo.txt'))
