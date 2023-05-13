class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not bool(self.items)

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


def read_file(file_name):
    stack = Stack()
    with open(file_name, 'r') as file:
        for line in file:
            stack.push(line.strip())
    return stack


def write_file(file_name, stack):
    with open(file_name, 'w') as file:
        while not stack.is_empty():
            file.write(stack.pop() + '\n')


def print_stack(stack):
    temp_stack = Stack()
    while not stack.is_empty():
        data = stack.pop()
        print(data)
        temp_stack.push(data)
    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())


def search_stack(stack, query):
    temp_stack = Stack()
    found = False
    while not stack.is_empty():
        data = stack.pop()
        if query in data:
            print(f'Found: {data}')
            found = True
        temp_stack.push(data)
    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())
    if not found:
        print('Not found')


def insert_in_stack(stack, new_data):
    temp_stack = Stack()
    inserted = False
    while not stack.is_empty():
        data = stack.pop()
        if not inserted and new_data > data:
            temp_stack.push(new_data)
            inserted = True
        temp_stack.push(data)
    if not inserted:
        temp_stack.push(new_data)
    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())


def delete_from_stack(stack, query):
    temp_stack = Stack()
    deleted = False
    while not stack.is_empty():
        data = stack.pop()
        if query in data and not deleted:
            deleted = True
            continue
        temp_stack.push(data)
    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())
    if deleted:
        print(f'Deleted: {query}')
    else:
        print('Not found')


file_name = 'bank_accounts.txt'
stack = read_file(file_name)

print('Stack:')
print_stack(stack)

search_query = 'Name10'
print(f'Searching for {search_query}:')
search_stack(stack, search_query)

new_data = 'Surname11;Name11;15056738447;LV439333248951;549466.40;JPY'
print(f'Inserting {new_data}:')
insert_in_stack(stack, new_data)
print('Stack after insertion:')
print_stack(stack)

delete_query = 'Name10'
print(f'Deleting {delete_query}:')
delete_from_stack(stack, delete_query)
print('Stack after deletion:')
print_stack(stack)

write_file(file_name, stack)
