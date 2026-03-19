def is_valid_input(name): # 이름이 공백이 아니고, 빈 문자열이 아닌지 확인하는 함수
    return name.strip() != ""

print("🦁 아기 사자 명단 관리 프로그램입니다.")

members = [] # 멤버 명단 저장 배열 리스트

while True:
    name = input("아기 사자 이름을 입력하세요 (종료하려면 'exit' 입력 & 삭제하려면 'delete' 입력): ") # 입력 받기
    
    if name == "exit": # 종료
        print("프로그램을 종료합니다.")
        break
    
    if name in members: # 이미 명단에 있는 이름인지 확인 (in 연산자는 리스트에 해당 요소가 있는지 확인하는 연산자)
        print("이미 명단에 있는 이름입니다.")
        continue

    if not is_valid_input(name): # not 연산자는 => !와 같음.
        print("유효한 이름을 입력해주세요.")
        continue
    
    if name == "delete": # 삭제
        delete_name = input("삭제할 아기 사자 이름을 입력하세요: ") # 삭제한 멤버 이름 입력 받기
        if delete_name in members: # 삭제할 이름이 명단에 있는지 확인
            members.remove(delete_name) # remove() 메서드를 이용하여 특정 값 요소를 찾아 삭제
            print(f"{delete_name}이(가) 명단에서 삭제되었습니다.")
        else:
            print("명단에 없는 이름입니다.")
        break
    
    members.append(name) # 입력 받은 이름을 배열에 추가
    print(f"명단에 추가됨: {name}")
    print(f"현재 명단: {len(members)}명 등록됨") # len() 함수는 배열 리스트의 길이 반환

#    
#for 변수 in 반복할것:
#   실행할코드    
#
#range 함수는 배열 아님 -> 배열을 만들어주는 함수
#

    for i in range(len(members)):
        print(f"{i+1}번째 아기 사자, 이름: {members[i]}")