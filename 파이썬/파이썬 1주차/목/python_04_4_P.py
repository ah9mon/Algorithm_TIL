word1 = input('첫 번째 이름을 입력하세요 : ') #apple
word2  = input('두 번째 이름을 입력하세요 : ') # banana

word1_list = list(word1) #['a', 'p', 'p', 'l', 'e']
word2_list = list(word2) #['b','a','n','a','n','a']

for index_num in range(len(word1_list)):
    word1_list[index_num] = ord(word1_list[index_num])  
for index_num in range(len(word2_list)):
    word2_list[index_num] = ord(word2_list[index_num])

# print(word1_list) #[97, 112, 112, 108, 101] 
# print(word2_list) #[98, 97, 110, 97, 110, 97]    
#print(sum(word1_list)) #530
#print(sum(word2_list)) #609

if sum(word1_list) > sum(word2_list): 
    print(word1) #apple
elif sum(word1_list) < sum(word2_list):
    print(word2) #banana
else:
    print('아스키 숫자들의 합이 같습니다')
