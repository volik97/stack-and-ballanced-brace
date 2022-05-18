class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def pop(self):
        if len(self.stack) == 0:
            return None
        removed = self.stack.pop()
        return removed

    def push(self, item):
        self.stack.append(item)

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

def balance_check(brace_list):
    if len(brace_list) % 2 == 1:
        return False

    openings = set('({[')
    matches = set([('{', '}'), ('(', ')'), ('[', ']')])

    for brace in brace_list:
        if brace in openings:
            stack.push(brace)
        else:
            if stack.size() == 0:
                return False
            last_open = stack.pop()
            if (last_open, brace) not in matches:
                return False

    return stack.size() == 0


if __name__ == '__main__':
    stack = Stack()
    print(balance_check('[([])((([[[]]])))]{()}'))