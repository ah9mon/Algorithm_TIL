# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.

def caesar(word, n):
    word_list = list(word) #(apple의 경우)['a', 'p', 'p', 'l', 'e']
    #print(word_list)
                 
    ord_word_list = list(map(ord,word_list)) #(apple의 경우)[97, 112, 112, 108, 101]
    #print(ord_word_list)

    for i in range(len(ord_word_list)): #ord_word_list의 원소개수 만큼 반복

        if chr(ord_word_list[i]).islower(): #i번째 원소가 소문자면  
            
            if (ord_word_list[i] + n) > 122: #i번째 원소의 아스키숫자 + n이 122보다 크면 
                ord_word_list[i] -= 26 #i번째 원소의 아스키숫자에서 - 26

        elif chr(ord_word_list[i]).isupper(): #i번째 원소가 대문자면  

            if (ord_word_list[i] + n) > 90: #i번째 원소의 아스키숫자 + n이 90보다 크면 
                ord_word_list[i] -= 26 #i번째 원소의 아스키숫자에서 - 26

    new_ord_list = list(map(lambda x : x + n, ord_word_list)) #(apple의 경우)[102, 117, 117, 113, 106]
    #print(new_ord_list)
    
    new_word_list = list(map(chr, new_ord_list)) #(apple의 경우)['f', 'u', 'u', 'q', 'j']
    #print(new_word_list)
    new_word = ''.join(new_word_list) # 'fuuqj'
    return new_word
   


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(caesar('apple', 5))      # fuuqj
    print(caesar('ssafy', 1))      # ttbgz
    print(caesar('Python', 10))    # Zidryx
