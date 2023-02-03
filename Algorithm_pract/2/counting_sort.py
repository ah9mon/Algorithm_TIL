def counting_sort(data):
    counts = [0] * (max(data) + 1)
    sort_counts = [0] * len(data)
    
    for i in range(len(data)):
        counts[data[i]] += 1
    
    #print(counts) #[1, 3, 1, 1, 2]
    
    for j in range(1, len(counts)):
        counts[j] += counts[j-1]
    
    #print(counts) #[1, 4, 5, 6, 8]
    
    for index in data:
        counts[index] -= 1
        sort_counts[counts[index]] = index
    
    return sort_counts



data = [0, 4, 1, 3, 1, 2, 4, 1]
print(counting_sort(data)) #[0, 1, 1, 1, 2, 3, 4, 4]