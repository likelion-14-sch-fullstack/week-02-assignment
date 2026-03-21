def valid_input(name): # 입력한 이름이 유효한 이름인지 확인하는 함수
    return name.strip() != "" # 공백을 제거한 문자열이 빈 문자열이 아닌 경우 유효한 입력으로 생각

print("명단 관리 프로그램")
names =[] # 이름을 저장할 리스트 생성

while True: # 무한 루프를 사용하여 사용자가 종료할 때까지 반복 
    input_name = input("이름을 입력하세요(종료 : q, 삭제 : d): ") # 이름을 입력 받음 (q를 입력하면 종료)
    
    if input_name in names: # 이미 등록된 이름인지 확인
        print("이미 등록된 이름입니다. 다른 이름을 입력하세요.") # 중복된 이름에 대한 오류 관리
        continue # 중복된 이름이 입력된 경우 다음 반복으로 넘어감
    
    if input_name.lower() == "q": # 입력이 q인 경우 루프 종료
        break
    
    elif input_name.lower() == "d": # 입력이 d인 경우 리스트에서 이름 제고
        target = input("삭제할 이름을 입력하세요: ") # 삭제할 이름을 입력 받음
        if target in names: # 삭제할 이름이 리스트에 있는지 확인
            names.remove(target) # 리스트에서 이름 제거
            print(f"{target}이(가) 삭제되었습니다.") # 삭제한 이름을 출력하여 사용자에게 알림
    
    if valid_input(input_name): # 입력한 이름이 유효한 경우 리스트에 추가
        if input_name.lower() == "d" or input_name.lower() == "q": # d 또는 q는 이름으로 사용할 수 없도록 처리
            continue # 유효하지 않은 이름이 입력된 경우 다음 반복으로 넘어감
        names.append(input_name.strip()) # 공백을 제거하여 리스트에 추가
        
    
    else:        print("유효한 이름을 입력하세요.") # 유효하지 않은 입력에 대한 오류 관리
    
    print(f"{input_name}이(가) 등록 되었습니다.") # 등록한 이름을 출력하여 사용자에게 알림
    input()
print("\n추가된 명단.")
for i in range(len(names)): # 리스트의 길이만큼 반복문을 돌며 이름을 출력
    print(f"{i+1}. {names[i]}") # 리스트는 0부터 시작하기 때문에 인덱스에 1을 더하여 출력
print(f"\n총 {len(names)}명의 이름이 등록되었습니다.") # 총 등록된 이름의 수를 출력