def valid_input(name): # 입력한 이름이 유효한 이름인지 확인하는 함수
    return name.strip() != "" # 공백을 제거한 문자열이 빈 문자열이 아닌 경우 유효한 입력으로 생각

print("명단 관리 프로그램")
names =[] # 이름을 저장할 리스트 생성

while True: # 무한 루프를 사용하여 사용자가 종료할 때까지 반복 
    input_name = input("이름을 입력하세요(종료 : q): ") # 이름을 입력 받음 (q를 입력하면 종료)
    if input_name.lower() == "q": # 입력이 q인 경우 루프 종료
        break
    if valid_input(input_name): # 입력한 이름이 유효한 경우 리스트에 추가
        names.append(input_name.strip()) # 공백을 제거하여 리스트에 추가
    else:        print("유효한 이름을 입력하세요.") # 유효하지 않은 입력에 대한 오류 관리
    
    print(f"{input_name}이(가) 등록 되었습니다.") # 등록한 이름을 출력하여 사용자에게 알림
print("\n추가된 명단.")
for i in range(len(names)): # 리스트의 길이만큼 반복문을 돌며 이름을 출력
    print(f"{i+1}. {names[i]}") # 리스트는 0부터 시작하기 때문에 인덱스에 1을 더하여 출력
