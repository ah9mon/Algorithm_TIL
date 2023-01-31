from collections import Counter

participants =  [3, 7, 100, 21, 13, 6, 5, 7, 5, 6, 3, 13, 21]
#

same_count = sorted( Counter(participants).items() , key = lambda x : x[1]) #[(100, 1), (3, 2), (7, 2), (21, 2), (13, 2), (6, 2), (5, 2)]
print(same_count[0][0]) # 100
