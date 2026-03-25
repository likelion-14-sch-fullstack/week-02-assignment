# 명단 입력값이 올바른지 검사하는 함수
def is_valid_input(name):
    # strip()으로 앞뒤 공백을 제거한 뒤
    # 빈 문자열이 아니면 True를 반환
    return name.strip() != ""


# 현재 저장된 명단을 출력하는 함수
def print_lions(lions):
    print("\n📋 현재 등록된 명단입니다.")

    # 명단이 비어 있으면 안내 메시지 출력
    if len(lions) == 0:
        print("아직 등록된 사람이 없습니다.")
        return

    # 번호를 붙여서 명단 출력
    for i in range(len(lions)):
        print(f"🦁 {i + 1}. {lions[i]}")


# 프로그램의 전체 동작을 담당하는 함수
def run_program():
    # 이름들을 저장할 빈 리스트 생성
    lions = []

    # 프로그램 시작 안내 문구 출력
    print("🚀 멋사 14기 명단 관리 프로그램입니다.")
    print("이름을 입력하면 등록됩니다.")
    print("종료하려면 q, 삭제하려면 d를 입력하세요.")

    # 사용자가 직접 종료할 때까지 반복
    while True:
        # 사용자에게 이름 입력 받기
        name = input("\n📝 이름을 입력하세요 (q: 종료, d: 삭제): ")

        # q를 입력하면 반복문 종료
        if name == "q":
            print("\n✅ 이름 입력을 종료합니다.")
            break

        # d를 입력하면 삭제 기능 실행
        elif name == "d":
            target = input("❌ 삭제할 이름을 입력하세요: ")

            # 삭제할 이름이 리스트에 있으면 삭제
            if target in lions:
                lions.remove(target)
                print(f"'{target}' 이름이 삭제되었습니다.")
            else:
                print("해당 이름은 명단에 없습니다.")

            # 삭제 처리 후 다시 입력 단계로 이동
            continue

        # 공백 입력 방지
        if not is_valid_input(name):
            print("⚠ 이름이 비어 있습니다. 다시 입력해주세요.")
            continue

        # 중복 이름 방지 기능
        if name in lions:
            print("⚠ 이미 등록된 이름입니다. 다른 이름을 입력해주세요.")
            continue

        # 유효한 이름이면 리스트에 추가
        lions.append(name)
        print(f"✅ '{name}' 이(가) 등록되었습니다.")

    # 반복문 종료 후 최종 명단 출력
    print_lions(lions)

    # 총 인원 수 출력
    print(f"\n총 {len(lions)}명이 등록되었습니다.")


# 이 파일을 직접 실행했을 때만 프로그램 시작
if __name__ == "__main__":
    run_program()