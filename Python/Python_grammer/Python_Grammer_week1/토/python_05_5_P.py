words_dict = {'proper' : '적절한',
'possible' : '가능한',
'moral' : '도덕적인',
'patient' : '참을성 있는',
'balance' : '균형',
'perfect' : '완벽한',
'logical' : '논리적인',
'legal' : '합법적인',
'relevant' : '관련 있는',
'responsible' : '책임감 있는',
'regular' : '규칙적인'}


words_list = list(words_dict.keys())
print(words_list)

in_words_list = []
for word in words_list:
    if word[0] == 'b' or 'm' or 'p':
        in_word = 'im'+ word
        in_words_list.append(in_word)
    elif word[0] == 'l' :
        in_word = 'il'+ word
        in_words_list.append(in_word)
    elif word[0] == 'r' :
        in_word = 'ir'+ word
        in_words_list.append(in_word)

in_words_list.sort()            
print(in_words_list)    


