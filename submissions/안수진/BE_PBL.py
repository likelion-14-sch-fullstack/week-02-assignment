def is_valid_input(name):
    return name.strip() != ""

print("*낯선 곳에 도착했다.")
print("*오래된 명부가 놓여 있다.")
print("*펜이 스스로 움직이길 기다리는 것 같다.")
print()
print("[ 몬스터 명부 ]")


lions = [] # 이름 저장 리스트

while True:
    print()
    name = input("*이름을 적는다... (포기하려면 q / 지우려면 d) : ")

    if name == "q":  # 종료 조건
        print()
        print("*포기하지마 {name}! 의지를 가지렴...")
        break

    elif name == "d":  # 삭제 기능
        target = input("*지우고 싶은 이름은? : ")
        if target in lions:
            lions.remove(target)
            print(f"*당신은 '{target}' 의 이름이 천천히 흐려졌다.")
            print(f"*이상하게 조용하다.")
        else:    
            print(f"*당신은 '{target}' 의 이름을 찾을 수 없었다.")
            print("*이곳에 있어도 될지 모르겠다는 기분이... 당신을 의지로 채워준다.")

    elif not is_valid_input(name):    # 빈 입력 방어
        print("*펜이 멈췄다.")
        print("*이름 없이는 기록될 수 없다.")

    elif name in lions:    # 중복 방지
        print(f"*당신은 '{name}' 의 이름을 이미 새겼다.")
        print("*방이 조용하다. 이 정적이 당신을 의지로 채워준다.")

    else:
        lions.append(name)
        print(f"*당신은 '{name}' 이라고 적었다.")
        print("*당신이 이곳에 도달했음이 당신을 의지로 채워준다.")

# 명단 출력
print()
print("*당신은 명부를 펼쳐 보았다.") 
for i in range(len(lions)):
    print(f"  {i + 1}.  {lions[i]}")

# 총 인원 수 출력
print()
print(f"*총 {len(lions)} 명의 이름이 새겨져 있다.")
print("*요리 냄새가 당신을 의지로 채워준다.")
