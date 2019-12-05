import re
from functools import reduce

def compile_glsl_to_python(glsl_code):
    lines = re.split('(;|{)', glsl_code)
    lines = reduce(lambda acc, el: acc[:-1] + [acc[-1] + el] if ';' in el or '{' in el else acc + [el], lines, [])

    new_lines = []
    tab_count = 0
    for line in lines:
        new_line = re.sub(r'float', '', line)
        new_line = re.sub(r'(vec\d)\s+(\w+)\s*=\s*(\w+(?!.*(?:\.|\(|\d)))', r'\1 \2 = \1(\3)', new_line)

        new_line = re.sub(r'(vec\d)(?=.*[\=\{])', '', new_line)
        new_line = re.sub(r';|\{|\}', '', new_line)
        new_line = re.sub('\s', '', new_line)
        new_line = re.sub('return', 'return ', new_line)

        for i in range(0, tab_count):
            new_line = '    ' + new_line

        if '{' in line:
            tab_count += 1
            if 'if' not in line:
                new_line = 'def ' + new_line + ':'
            else:
                new_line = new_line + ':'

        new_lines.append(new_line)

    return '\n'.join(new_lines)
