seq = '((()))'

def examine(seq):
    stack = []
    for ch in seq:
        if ch == '(':
            stack.append(ch)
        else:
            if stack:
                stack.pop()
            else:
                return False
    return True

print(examine(seq))