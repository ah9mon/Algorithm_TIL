import random as rd

def making_card_list() -> list:
	card_list = []

	for shape in ["spade", "heart", "diamond", "clover"]:

		for number in ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]:

			card_list.append((shape, number))

	return card_list


trump_card_list = making_card_list()
#print(trump_card_list)

player1_win = 0
player2_win = 0
Alpha_dict = {'J' : 11 , 'Q' : 12 , 'K' : 13, 'A' : 14 }
#print(Alpha_dict.keys())
Shape_dict = {'clover' : 1 , 'heart' : 2 , 'diamond' : 3 , 'spade' : 4 } 
while True:
    
    player1 = rd.choice(trump_card_list) # player1에 trump_card_list 원소 한가지 랜덤으로 할당
    trump_card_list.remove(player1) # player1에 할당된 원소 삭제
    player1 = list(player1)
    
    player2 = rd.choice(trump_card_list) # player2에 trump_card_list 원소 한가지 랜덤으로 할당
    trump_card_list.remove(player2) # player2에 할당된 원소 삭제 
    player2 = list(player2)
    
    if player1[1] in Alpha_dict.keys():# 만약 player1[1] in Alpha_dict.keys()에 있다면
        player1[1] = Alpha_dict[player1[1]] # 알파벳을 수치 비교를 위해 수로 바꿈
        if player1[0] in Shape_dict.keys(): # 만약 player1[1] in Shape_dict.keys()에 있다면
           player1[0] = Shape_dict[player1[0]] # 문양을 수치 비교를 위해 수로 바꿈 
       
    if player2[1] in Alpha_dict.keys(): # 만약 player2[1] in Alpha_dict.keys()에 있다면
        player2[1] = Alpha_dict[player2[1]] # 알파벳을 수치 비교를 위해 수로 바꿈
        if player2[0] in Shape_dict.keys(): # 만약 player2[1] in Shape_dict.keys()에 있다면
           player2[0] = Shape_dict[player2[0]] # 문양을 수치 비교를 위해 수로 바꿈
              
    
    
    if player1[1] > player2[1]:# 만약 player1의 숫자가 player2보다 크다면 
        player1_win += 1# player1 승
    elif player1[1] < player2[1]:# 만약 player1의 숫자가 player2보다 작다면 
        player2_win += 1# player2 승
    else: # 만약 player1의 숫자가 player2와 같다면 문양 가치 비교
        if player1[0] > player2[0]:# 만약 player1의 숫자가 player2보다 크다면 
            player1_win += 1# player1_win에 승리 횟수 추가
        elif player1[0] < player2[0]:# 만약 player1의 숫자가 player2보다 작다면 
            player2_win += 1# player2_win에 승리 횟수 추가  
    
    if player1_win == 6: # player1이 6번 승리하면
        print(f'player1이 {player1_win}번 승리')
        break
    elif player2_win == 6 : # player2가 6번 승리하면
        print(f'player2가 {player2_win}번 승리')     
        break
        
    
    
    

