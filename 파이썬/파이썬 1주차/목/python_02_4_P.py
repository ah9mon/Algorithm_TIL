# 출력 결과 예시
# 스테이크   50,000
# + VAT     7,500
# 총계 ₩    57,500
menu = {'스테이크' : 5 }
dish = input('음식을 주문하세요 : ')
VAT = menu[dish]*0.15
print(f'{menu[dish]}0,000원 입니다.')
print('VAT 미포함 가격입니다. 결제하시겠습니까?')
ans = input('yes or no : ')
if ans == 'yes' :
    print('영수증')
    print(f'{dish}   {menu[dish]*10000}')
    print(f'+ VAT      {5*0.15*10000}')
    print(f'총계 ₩    {(VAT + menu[dish])*10000 }')