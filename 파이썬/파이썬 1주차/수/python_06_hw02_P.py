# A.    입력 예시 
# ['eat','tea','tan','ate','nat','bat']

# B.    출력 예시 
# [ ['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat'] ] 


# set()가 같은 것 끼리 묶기 
# 일단 set dict 만들고
# value가 같은 것끼리 리스트화  

str_list = input('입력 : ')
str_list = str_list.strip("[""]")
str_list = str_list.replace(",", ' ')
str_list = str_list.replace("'", ' ')
str_list = str_list.split()
words = str_list
    
def group_anagrams():

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
    return anagram

print(group_anagrams())


