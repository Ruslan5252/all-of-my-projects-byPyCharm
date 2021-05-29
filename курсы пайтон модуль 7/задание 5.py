def word_in_str(str='',word=''):
    count = 0
    word=word.lower()
    for i in str.lower():
        if i == word:
            count +=1
    return count
print(word_in_str("Java",'a'))



