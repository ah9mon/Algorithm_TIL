import os 

if not os.path.exists('[첨부파일 참고]'): #현재 디렉토리에 [첨부파일 참고]라는 폴더나 확장자가 없는 파일이 없다면
    os.mkdir('[첨부파일 참고]') # [첨부파일 참고] 라는 폴더 생성

file_name = os.listdir() # 해당 경로에 있는 모든 파일 및 폴더의 파일명/확장자 리스트를 할당
# print(file_name) 
for filename in file_name :
    if os.path.splitext(filename)[0] == '[첨부파일 참고]' : #file_name 리스트에 폴더(파일)명이 [첨부파일 참고]인 폴더(파일)가 있다면
        print(filename) # 파일명과 확장자를 출력 (폴더는 확장자가 없으므로 파일명만 출력됨)




