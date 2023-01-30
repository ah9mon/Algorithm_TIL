
import random

class ClassHelper:

    def __init__(self, list1):
        self.list = list1
        
    def pick(self, n):
        return random.sample(self.list, n)
        

    def match_pair(self):
        random.shuffle(self.list)
        if len(self.list) % 2 == 0 :
            teams = []
            for num1 in range(len(self.list) // 2):
                teams.append(self.list[num1 * 2 : (num1 + 1) * 2])

            return teams
            
        else :
            teams = []
            for num1 in range(len(self.list) // 2 - 1):
                teams.append(self.list[num1 * 2 : (num1 + 1) * 2])
            
            teams.append(self.list[-3:])

            return teams


ch = ClassHelper(['김해피', '이해킹', '조민지', '박영수', '정민수'])

print(ch.pick(1))
print(ch.pick(1))
print(ch.pick(2))
print(ch.pick(3))
print(ch.pick(4))

print(ch.match_pair())
