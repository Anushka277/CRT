def Student_Grade_System(name: str, n1: int, n2: int, n3: int) -> str:
    average = round((n1 + n2 + n3) / 3, 2)
    status = "Pass" if average >= 40 else "Fail"
    return f"Average grade: {average}, Status: {status}"



if __name__ == '__main__':
    name = input().strip()
    n1, n2, n3 = map(int, input().split())
    print(Student_Grade_System(name, n1, n2, n3))