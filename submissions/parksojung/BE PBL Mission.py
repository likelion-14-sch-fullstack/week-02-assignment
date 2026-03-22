def is_valid_input(name):   #유효성 검사 함수
    return name.strip() != ""    #빈 문자열인지 검사

print("🦁 아기 사자 명단 관리 프로그램입니다.")
lions = [] # 빈 리스트-> 무한 루프로 이름을 계속 받아 저장

while True: 
    name = input("✏아기 사자 이름을 입력하세요(종료하려면 'q' 입력): ")

    if name == "q":     #종료 조건
        print("\n 이름 입력을 종료합니다.")   
        break

    elif name == "d":
        target = input("삭제할 이름: ")
        if target in lions:
            lions.remove(target)
            print(f"'{target}' 삭제되었습니다.")
        else:
            print("해당 이름이 존재하지 않습니다.")
        continue

    if not is_valid_input(name):   #빈 입력 방어
        print("이름이 비어있습니다. 다시 입력해주세요.")
        continue

    if name in lions:     #중복 방어
        print("이미 등록된 이름입니다!")
        continue

    lions.append(name)    # 리스트에 추가
    print(f"'{name}' 이(가) 등록되었습니다.⭐️")

print("\n 현재 아기 사자 명단입니다.오늘도 수고하셨습니다🌙")    # 출력
for i in range(len(lions)):
        print(f" {i + 1}. {lions[i]}")