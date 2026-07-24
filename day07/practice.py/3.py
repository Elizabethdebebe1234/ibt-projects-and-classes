class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]


names = ["Almaz", "Dawit", "Sara", "Abel"]

stack = Stack()

# Push all names onto the stack
for name in names:
    stack.push(name)

# Pop names to reverse the list
reversed_names = []

while stack.items:
    reversed_names.append(stack.pop())

print("Original List:", names)
print("Reversed List:", reversed_names)