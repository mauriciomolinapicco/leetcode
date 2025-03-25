#SORTING ARRAY BASED ON STR SIZE
arr = ["alice", "james","john","doe"]

arr.sort(key=lambda x: len(x))
print(arr)