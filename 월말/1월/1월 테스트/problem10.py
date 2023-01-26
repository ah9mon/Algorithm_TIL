# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.

def is_position_safe(N, M, position):
    x_location = list(range(N)) #[0,1,2]
    y_location = list(range(N)) #[0,1,2]
    M_x_moving = [0, 1] 
    M_y_moving = [2, 3]

    if M in M_x_moving: #M이 M_x_moving에 있다면

        if M == 1: # M이 1이라면
            new_x_position = position[0] + 1

        else: #M이 0이라면
            new_x_position = position[0] - 1
        
        if new_x_position in x_location: #new_x_position가 x_location에 있다면
            return True #True

        else:
            return False #False

    if M in M_y_moving: #M이 M_y_moving에 있다면

        if M == 3: # M이 3이라면
            new_y_position = position[0] + 1

        else: # M이 2라면
            new_y_position = position[0] - 1
        
        if new_y_position in y_location:  #new_y_position가 y_location에 있다면
            return True #True
            
        else:
            return False #False

             
    

# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(is_position_safe(3, 1, (0, 0)))  # True
    print(is_position_safe(3, 0, (0, 0)))  # False
