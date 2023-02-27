fruits = input()
fruits = fruits.lower()
# print(fruit)
fruits1 = fruits.split(',')
# print(fruit1)

for n in range(len(fruits1)):
    if 'rotten' in fruits1[n]:
        fruits1[n] = fruits1[n].replace('rotten','')
        print(fruits1[n])
        

print(fruits1)
