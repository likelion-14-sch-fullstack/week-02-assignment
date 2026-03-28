lions = []

print("🦁 아기 사자 명단 관리 프로그램입니다.")

while True:
    print("\n" + "="*30)
    name = input("✏ 아기 사자 이름을 입력하세요 (종료: q / 삭제: d): ")

    # 1. 종료 기능 (q 입력 시)
    if name == 'q':
        break

    # 2. 삭제 기능 추가 (d 입력 시)
    elif name == 'd':
        target = input("🗑️ 삭제할 이름: ")
        if target in lions:
            lions.remove(target)
            print(f"✅ {target} 학생이 명단에서 삭제되었습니다.")
        else:
            print("⚠️ 명단에 없는 이름입니다.")
        continue

    # 3. 중복 이름 방지 (in 연산자 사용)
    if name in lions:
        print("❌ 이미 등록된 이름입니다!")
        continue
    
    # 이름 추가
    lions.append(name)
    print(f"✨ {name} 학생이 추가되었습니다.")

# 반복문 종료 후 출력 영역
print("\n📋 현재 아기 사자 명단입니다.")
if not lions:
    print("현재 등록된 인원이 없습니다.")
else:
    for i in range(len(lions)):
        print(f"🦁 {i + 1}. {lions[i]}")

# 4. 총 인원 수 출력
print(f"\n✨ 총 {len(lions)}명이 등록되었습니다.")
print("프로그램을 종료합니다.")