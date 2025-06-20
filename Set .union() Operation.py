english = int(input())
arr = [int(x) for x in input().split()]
french = int(input())
arr2 = [int (x) for x in input().split()]

only_english = set(arr) | set(arr2)
print(len(only_english))