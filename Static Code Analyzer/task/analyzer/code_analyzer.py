fn = input()
with open(fn, 'r') as file:
    for i, line in enumerate(file):
        if len(line) > 79:
            print(f'Line {i + 1}: S001 Too long')

