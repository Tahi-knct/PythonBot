word: str = "Python"
List: list = [1, 2, 3]
print(word[1])
print(List[2])
List[2] = 3 ** 3
print(List[2])
List.append(2 ** 2)
print(List[3])
print(List)
List[1:3] = [5, 6, 7]
print(List)
List.clear()
print(List)
print(len(List))
List=[1,2,3,5,4]
List.sort()
print(List)
List2 = List.copy()
print(List2)