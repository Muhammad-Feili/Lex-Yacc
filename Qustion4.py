import ply.lex as lex

OPERATORS = set(['+', '-', '*', '/', '(', ')'])
PRIORITY = {'+': 1, '-': 1, '*': 2, '/': 2}


def infix_to_prefix(formula):
    op_stack = []
    exp_stack = []
    for ch in formula:
        if not ch in OPERATORS:
            exp_stack.append(ch)
        elif ch == '(':
            op_stack.append(ch)
        elif ch == ')':
            while op_stack[-1] != '(':
                op = op_stack.pop()
                a = exp_stack.pop()
                b = exp_stack.pop()
                exp_stack.append(op+b+a)
            op_stack.pop()  # pop '('
        else:
            while op_stack and op_stack[-1] != '(' and PRIORITY[ch] <= PRIORITY[op_stack[-1]]:
                op = op_stack.pop()
                a = exp_stack.pop()
                b = exp_stack.pop()
                exp_stack.append(op+b+a)
            op_stack.append(ch)

    # leftover
    while op_stack:
        op = op_stack.pop()
        a = exp_stack.pop()
        b = exp_stack.pop()
        exp_stack.append(op+b+a)
    print(exp_stack[-1])
    return exp_stack[-1]


class Lexer(object):
    tokens = (
        'NUMBER',
        'PLUS',
        'MINUS',
        'TIMES',
        'DIVIDE',
        'LPAREN',
        'RPAREN',
    )

    t_PLUS = r'\+'
    t_MINUS = r'\-'
    t_TIMES = r'\*'
    t_DIVIDE = r'/'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_ignore = ' \t'

    expression = ""

    def t_NUMBER(self, token):
        r'\d+'
        self.expression += token.value
        token.value = int(token.value)
        return token

    def t_EXPRESSION(self, token):
        r'[^ \t\n]+'
        self.expression += token.value

    def t_newline(self, token):
        r'\n+'
        token.lexer.lineno += len(token.value)

    def t_error(self, token):
        print('Illegal character "%s"' % token.value[0])
        token.lexer.skip(1)

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    def test(self, input_data, verbs=[]):
        self.lexer.input(input_data)
        while True:
            token = self.lexer.token()
            if not token:
                break

        print(self.expression)
        print(input_data)
        prefix = infix_to_prefix(self.expression)
        print("the prefix expr of :", input_data, "is", prefix)


if __name__ == "__main__":
    lexer = Lexer()
    lexer.build()
    input_data = input("\nEnter the Entry : ")
    if input_data:
        print("\nAnswer : \n")
        print("♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪")
        lexer.test(input_data)
        print("♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪\n")
        print("\nEnd This Example.")
    else:
        print("\n ... \n\nExited The Command")
