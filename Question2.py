import ply.lex as lex


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

    # this list is for extracted words from the sentence
    words = list()
    past_participles_irregular = ['abode', 'arisen', 'awoken', 'been', 'born', 'beaten', 'become', 'befallen', 'begotten',
                                  'begun', 'beheld', 'bent', 'bereft', 'besought', 'beset', 'bespoken', 'bestridden', 'bet', 'bidden/bid', 'bound',
                                  'bitten', 'bled', 'blown', 'broken', 'bred', 'brought', 'broadcast', 'built', 'burnt', 'burst', 'bought', 'cast',
                                  'catch', 'choose', 'cling', 'come', 'cost', 'creep', 'cut', 'deal', 'dig', 'do', 'draw', 'dream', 'drink', 'drive',
                                  'dwell', 'eat', 'interweave', 'fall', 'feed', 'feel', 'fight', 'find', 'flee', 'fling', 'fly', 'forbid', 'forecast',
                                  'forget', 'forgive', 'forsake', 'foresee', 'foretell', 'freeze', 'get', 'give', 'go', 'grind', 'grow', 'hang', 'have',
                                  'hear', 'hide', 'hit', 'hold', 'hurt', 'keep', 'kneel', 'know', 'lay', 'lead', 'lean', 'leap', 'learn', 'leave', 'lend',
                                  'let', 'lain', 'lost', 'made', 'meant', 'met', 'paid', 'mistaken', 'overheard', 'overslept', 'put', 'read', 'rent', 'rid',
                                  'ridden', 'rung', 'risen', 'run', 'said', 'seen', 'sought', 'sold', 'sent', 'set', 'shaken', 'shed', 'shone', 'shit/shat',
                                  'shot', 'shown', 'shrunk', 'shriven', 'shut', 'sung', 'sunk', 'sat', 'slain', 'slept', 'slid', 'slung', 'slunk', 'slit', 'smelt',
                                  'smitten', 'spoken', 'sped', 'spent', 'spun', 'spat', 'split', 'spoilt', 'spread', 'sprung', 'stood', 'stolen', 'stuck', 'stung',
                                  'stunk', 'stridden', 'struck', 'strung', 'striven', 'sworn', 'swept', 'swum', 'swung', 'taken', 'taught', 'torn', 'told', 'thought',
                                  'thrown', 'thrust', 'trodden', 'understood', 'undertaken', 'undone', 'upset', 'woken', 'worn', 'woven', 'wept', 'won', 'wound',
                                  'withdrawn', 'withstood', 'wrung', 'written']

    to_be_verbs = ['am', 'is', 'are', 'was', 'were']

    def t_NUMBER(self, token):
        r'\d+'
        token.value = int(token.value)
        return token

    def t_WORD(self, token):
        r'[a-zA-z]+'
        self.words.append(token.value)

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

        if len(verbs) == 0:
            verbs = self.past_participles_irregular

        is_passive = 0
        for i in range(len(self.words)):
            if self.words[i] in self.to_be_verbs:
                for j in range(len(self.words)):
                    # irregular and regluar verbs in english
                    if self.words[j] in verbs or self.words[i][-2:] == "ed":
                        is_passive = 1

        if is_passive == 1:
            print("The Entered Sentence is Passive")
        else:
            print("The Entered Sentence is Perfect")


if __name__ == "__main__":
    lexer = Lexer()
    lexer.build()
    input_data = input("\nEnter the Entry : ")
    if input_data:
        print("\nAnswer : \n")
        lexer.test(input_data)
        print("\nEnd This Example.")
    else:
        print("\n ... \n\nExited The Command")
