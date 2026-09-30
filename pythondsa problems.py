stack= []
result = ""
for char in "PYTHON":
    stack.append(char)
while len(stack) > 0:
    result = result + stack.pop()
print(result)