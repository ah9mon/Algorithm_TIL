words = ["round" , "dream", "magnet" , "tweet" , "tweet", "trick", "kiwi"]

for index_number in range(len(words)-1): # len(words) = 7
    if words[index_number][-1] == words[index_number + 1][0]: #words리스트의 index_number번째의 원소의 마지막 글자와 (index_number +1) 번째 첫번쨰 글자가 같다면 
        if words[index_number] == words[index_number + 1]: #words리스트의 index_number번째 원소(단어)와 (index_number + 1)번쨰 원소(단어)가 같다면
            print(f'{index_number + 2}번째 사람 탈락 (같은 단어 사용)') # (index_number + 2)번쨰 사람탈락 출력
        else:
            pass
    else:
        print(f'{index_number + 2}번째 사람 탈락(시작 문자 다름)') # (index_number + 2)번째 사람 탈락 출력   
