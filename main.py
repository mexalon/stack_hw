import re


class MyStack:
    def __init__(self):
        self.stack = []

    def __len__(self):
        return len(self.stack)

    def __str__(self):
        return f'{self.stack}'

    def push(self, thing):
        self.stack += [thing]
        return thing

    def pop(self, expect=None):
        try:
            thing = self.stack.pop(-1)
        except IndexError:
            thing = False

        if expect is not None and thing != expect:
            return False

        return thing

    def peek(self):
        try:
            thing = self.stack[-1]
        except IndexError:
            thing = None

        return thing

    def isEmpty(self):
        return len(self) == 0


def balanced(some_string: str):
    clean_list = re.findall("[{\\[()\\]}]", some_string)
    stack = MyStack()

    action = {'(': stack.push,
              '{': stack.push,
              '[': stack.push,
              ')': stack.pop,
              '}': stack.pop,
              ']': stack.pop}

    subst = {'(': '(',
             '{': '{',
             '[': '[',
             ')': '(',
             '}': '{',
             ']': '['}

    res = True
    for b in clean_list:
        if not action[b](subst[b]):
            res = False
            break
    if not stack.isEmpty():
        res = False

    return res


if __name__ == '__main__':
    ss = '[([])((([[[]]])))]{()}'
    if balanced(ss):
        print("Сбалансированно")
    else:
        print("Несбалансированно")
