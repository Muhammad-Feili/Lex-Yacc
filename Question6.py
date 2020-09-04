import ply.lex as lex


class Lexer(object):
    tokens = (
        'NUMBER',
        'WORD',
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

    code_line = ""
    code_context = []

    def t_NUMBER(self, token):
        r'\d+'
        self.code += token.value
        token.value = int(token.value)

    def t_WORD(self, token):
        r'.+'
        self.code_line += token.value

    def t_NEWLINE(self, token):
        r'\n+'
        token.lexer.lineno += len(token.value)
        self.code_context.append(self.code_line)
        self.code_line = ""

    def t_error(self, token):
        print('Illegal character "%s"' % token.value[0])
        token.lexer.skip(1)

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    def line_indents(self, line):
        j = 0
        space = 0
        while line[j] == ' ':
            space += 1
            j += 1

        return space

    def rec_indenting(self, i, whole_indent):
        if i == len(self.code_context)-1:
            if whole_indent > 0:
                while whole_indent > 1:
                    whole_indent -= 1
                    self.code_context[len(self.code_context)-1] += "}\n"
            return

        if self.code_context[i][-1] == ":":
            whole_indent += 1
            next_tabs = self.line_indents(self.code_context[i+1])

            self.code_context[i] += "\n"+" "*next_tabs+"{\n"
            return self.rec_indenting(i+1, whole_indent)

        else:
            next_tabs = self.line_indents(self.code_context[i])
            if self.line_indents(self.code_context[i]) > self.line_indents(self.code_context[i+1]):
                whole_indent -= 1
                self.code_context[i] = self.code_context[i]+" "*next_tabs+"}\n"
                return self.rec_indenting(i+1, whole_indent)
            else:
                return self.rec_indenting(i+1, whole_indent)

    def test(self, input_data):
        self.lexer.input(input_data)
        token = self.lexer.token()
        while True:
            if not token:
                break
            print(token)

        for i in range(len(self.code_context)):
            if self.code_context[i][-1] == ":":
                continue
            else:
                self.code_context[i] += ";\n"
        self.rec_indenting(0, 1)
        code = """"""
        print("*************************************")
        for i in self.code_context:
            code += i
        print(code)


if __name__ == "__main__":
    lexer = Lexer()
    lexer.build()
    code = """def test(self, input_data):
    self.lexer.input(input_data)
    while True:
        token = self.lexer.token()
        if not token:
            break
        print(token)

    for i in range(len(self.code_context)):
        if self.code_context[i][-1] == ":":
            continue
    """
    lexer.test(code)
