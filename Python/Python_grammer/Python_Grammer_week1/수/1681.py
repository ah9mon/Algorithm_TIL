word = input()
n = len(word)
#print(n)

if len(word) % 2 == 0 :
    n1= int(n/2 - 1)
    n2= int(n/2 + 1) 
    print(word[n1 : n2])

else : 
    n1 = int((n-1)/2)
    print(word[ n1 ])
