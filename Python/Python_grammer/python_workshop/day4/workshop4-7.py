#강한 이름

def get_strong_word(word1, word2):
    word1_list = list(map(ord,word1))
    word2_list = list(map(ord,word2))
    if sum(word1_list) > sum(word2_list):
        return word1
    elif sum(word1_list) < sum(word2_list):
        return word2
    else:
        return None
    
print(get_strong_word('delilah', 'dixon'))