testcase_num = int(input())

testcase = [input() for i in range(testcase_num)]
testcase1 = list(map(lambda x : x.split(), testcase))
print(testcase1)   
for i in range(len(testcase1)):
    index_list = list(map(int, testcase1[i]))
    n = index_list[0] // index_list[1]
    m = index_list[0] % index_list[1]
    print(f'#{i+1} {n} {m}') 
        

