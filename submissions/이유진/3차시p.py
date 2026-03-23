name=[]
tmp="" #입력값 잠시 저장할 임시 변수 생성

#입출력 각각 별도 함수 사용
def Input() : 
    while(True):
        tmp=input("이름을 입력하세요:") 
        if tmp.strip()=="": #빈 문자열 입력 방지
            print("빈 문자열입니다. 이름을 입력해주세요.")
        elif tmp=='q':
            print()
            Output()
            break
        elif tmp=='d': 
            tmp=input("목록에서 삭제할 이름을 입력하시오: ")
            if tmp in name: name.remove(tmp) #입력받은 이름이 리스트에 있다면 삭제
            else: print("목록에 등록되지 않은 이름입니다.") 
        elif tmp in name: #이름 중복 입력 방지
            print(f"'{tmp}', 이미 등록된 이름입니다.") 
        else: 
            name.append(tmp) #리스트에 입력받은 이름 추가

def Output() : 
    for i in range(len(name)):
        print(f"{i+1}.{name[i]}") #이름 명단 출력
    print(f"총 {len(name)}명이 등록되었습니다.")

print("<아기 사자 명단 관리 프로그램>")
print("(q):명단 출력 후 프로그램 종료")
print("(d):명단에서 삭제할 이름 선택")
Input()