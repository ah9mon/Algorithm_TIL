# encoding graph 만들기
from string import ascii_lowercase
from string import ascii_uppercase

lower_alpha_list = list(ascii_lowercase) # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'index_num1', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_alpha_list = list(ascii_uppercase) # ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
sign_list = ['+','/']

graph = {}
for upper in upper_alpha_list:
    graph[upper] = ord(upper) - 65

for lower in lower_alpha_list:
    graph[lower] = ord(lower) - 71

for num in range(10):
    graph[str(num)] = ord(str(num)) + 4
    

graph['+'] = 62
graph['/'] = 63

# print(graph)
# {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 
#'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25, 'a': 26, 'b': 27, 'c': 28, 'd': 29, 'e': 30, 'f': 31, 'g': 32, 'h': 33, 'index_num1': 34, 'j': 35, 'k': 36, 'l': 37, 'm': 38, 'n': 39, 'o': 40, 
# 'p': 41, 'q': 42, 'r': 43, 's': 44, 't': 45, 'u': 46, 'v': 47, 'w': 48, 'x': 49, 'y': 50, 'z': 51, '0': 52, '1': 53, '2': 54, '3': 55, '4': 56, '5': 57, '6': 58, '7': 59, '8': 60, 
# '9': 61, '+': 62, '/': 63}

# 입력

testcase_num = int(input())

sentence_list = [input() for index_num0 in range(testcase_num)]

# decoding

for index_num1 in range(len(sentence_list)):
    char_list = []
    for char1 in sentence_list[index_num1]: 
        char_list.append(graph.get(char1)) # char1 들을 graph의 숫자들로 바꿔서 char_list에 넣음
        
    char_list = list(map(lambda x : format(x, 'b'),char_list)) #char_list의 항목들을 2진수로 변환 
    for index_num2 in range(len(char_list)):
        if len(char_list[index_num2]) != 6: # 만약 char_list[index_num1] 가 6자리가 아니면 
            char_list[index_num2] = '0' * (6-len(char_list[index_num2])) + char_list[index_num2] # 6-len(char_list[index_num1])만큼 앞에 0을 붙여서 6자리 이진수로 바꿔줌 
    decoding_1 = ''.join(char_list) #char_list를 하나의 string으로 합침
    # print(char_list)
    # print(decoding_1)
    # print(len(decoding_1))

    decoding_list = []    
    for index_num3 in range(int(len(decoding_1)/8)):
        
        decoding_list.append(int('0b' + str(int(decoding_1[8 * index_num3 : 8 * (index_num3 + 1)])),2))
    
    decoding_list = list(map(chr, decoding_list))
    decoding_sentence = ''.join(decoding_list)
    print(f'#{index_num1+1} {decoding_sentence}')

