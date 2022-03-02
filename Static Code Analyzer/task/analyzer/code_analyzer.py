import re


def s001(num, line):
    if len(line) > 79:
        print(f'Line {num}: S001 Too long')


def s002(num, line):
    if (len(line) - len(line.lstrip())) % 4 != 0:
        print(f'Line {num}: S002 Indentation is not a multiple of four')


def s003(num, line):
    if ';' in line:
        exp = '[\'\"].*;.*[\'\"]'
        is_str = re.search(exp, line)
        if not is_str and ('#' not in line or line.index(';') < line.index('#')):
            print(f'Line {num}: S003 Unnecessary semicolon after a statement')


def s004(num, line):
    if '#' in line:
        k = line.index('#')
        if k > 2 and line[k - 2: k] != '  ':
            print(f'Line {num}: S004 Less than two spaces before inline comments')


def s005(num, line):
    if '#' in line and 'todo' in line.lower():
        print(f'Line {num}: S005 TODO found')


def s006(num, line):
    if cnt_blank > 2:
        print(f'Line {num}: S006 More than two blank lines')


# fn = 'tst.py'
fn = input()
with open(fn, 'r') as file:
    cnt_blank = 0
    for i, line in enumerate(file):
        if line.strip():
            for n in range(6):
                s = f's00{n + 1}({i + 1}, line)'
                eval(s)
            cnt_blank = 0
        else:
            cnt_blank += 1
