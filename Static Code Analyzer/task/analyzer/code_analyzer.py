import os.path
import re
import sys


def s001(fn, num, line):
    if len(line) > 79:
        print(f'{fn}: Line {num}: S001 Too long')


def s002(fn, num, line):
    if (len(line) - len(line.lstrip())) % 4 != 0:
        print(f'{fn}: Line {num}: S002 Indentation is not a multiple of four')


def s003(fn, num, line):
    if ';' in line:
        exp = '[\'\"].*;.*[\'\"]'
        is_str = re.search(exp, line)
        if not is_str and ('#' not in line or line.index(';') < line.index('#')):
            print(f'{fn}: Line {num}: S003 Unnecessary semicolon after a statement')


def s004(fn, num, line):
    if '#' in line:
        k = line.index('#')
        if k > 2 and line[k - 2: k] != '  ':
            print(f'{fn}: Line {num}: S004 Less than two spaces before inline comments')


def s005(fn, num, line):
    if '#' in line and 'todo' in line.lower():
        print(f'{fn}: Line {num}: S005 TODO found')


def s006(fn, num, line):
    if cnt_blank > 2:
        print(f'{fn}: Line {num}: S006 More than two blank lines')


def s007(fn, num, line):
    exp1 = '(def|class)'
    exp2 = '(def  |class  )'
    if re.search(exp1, line) and re.search(exp2, line):
        print(f'{fn}: Line {num}: S007 Too many spaces after def')


def s008(fn, num, line):
    exp = 'class\s+[A-Z][a-z]*[A-Z]?[a-z]*(\([A-Z][a-z]*[A-Z]?[a-z]*\))?:$'
    if 'class' in line and not re.search(exp, line):
        print(f'{fn}: Line {num}: S008 Class name should be written in CamelCase')


def s009(fn, num, line):
    exp = 'def\s+[a-z0-9_]+\('
    if 'def ' in line and not re.search(exp, line):
        print(f'{fn}: Line {num}: S009 Function name should be written in snake_case')


def chk_file(fn):
    with open(fn, 'r') as file:
        global cnt_blank
        for i, line in enumerate(file):
            if line.strip():
                for n in range(9):
                    s = f's00{n + 1}(fn, {i + 1}, line)'
                    eval(s)
                cnt_blank = 0
            else:
                cnt_blank += 1


args = sys.argv
path = args[1]
is_file = os.path.isfile(path)
base = os.path.dirname(path) if is_file else path
files = [os.path.split(path)[1]] if is_file else os.listdir(base)

cnt_blank = 0

for file in files:
    fn = base + os.sep + file
    chk_file(fn)
