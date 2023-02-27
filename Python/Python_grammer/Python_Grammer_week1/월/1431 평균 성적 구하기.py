score = {
    'python': 80,
    'django': 89,
    'web': 83
}

score['algorithm'] = 90 #{'python': 80, 'django': 89, 'web': 83, 'algorithm': 90}
score['python'] = 85 #{'python': 85, 'django': 89, 'web': 83, 'algorithm': 90}
score_sum = sum(score.values()) #score_sum = 347 (values 합)
score_average = score_sum / len(score) #score_average = value 전체 합 / value 개수 

print(score_average) #86.75
