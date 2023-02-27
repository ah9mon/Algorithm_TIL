words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

word_dic = {}
for word in words:
    sub_dic = {}
    for char in word:
        if char in sub_dic:
            sub_dic[char] +=1
        else:
            sub_dic[char] = 1
    word_dic[word] = sub_dic
print(word_dic)

anagram = []
for word in words :
    for ana_list in anagram:
        ana_word = ana_list[0]
        if word_dic[word] == word_dic[ana_word]:
            ana_list.append(word)
            break
    else:
        anagram.append([word])
    
print(anagram)

