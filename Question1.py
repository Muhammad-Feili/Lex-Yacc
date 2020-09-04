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
    VERBS = ['is', 'are', 'study', 'was', 'werer', 'am', 'be', 'been', 'look', 'abide', 'abode', 'abode', 'arise', 'arose', 'arisen', 'awake', 'awoke', 'awoken', 'be', 'was/were', 'been',
             'bear', 'bore', 'born', 'beat', 'beat', 'beaten', 'become', 'became', 'become', 'befall', 'befell', 'befallen', 'beget',
             'begot', 'begotten', 'begin', 'began', 'begun', 'behold', 'beheld', 'beheld', 'bend', 'bent', 'bent', 'bereave', 'bereft',
             'bereft', 'beseech', 'besought', 'besought', 'beset', 'beset', 'beset', 'bespeak', 'bespoke', 'bespoken', 'bestride',
             'bestrode', 'bestridden', 'bet', 'bet', 'bet', 'bid', 'bade/bid', 'bidden/bid', 'bind', 'bound', 'bound', 'bite', 'bit',
             'bitten', 'bleed', 'bled', 'bled', 'blow', 'blew', 'blown', 'break', 'broke', 'broken', 'breed', 'bred', 'bred', 'bring',
             'brought', 'brought', 'broadcast', 'broadcast', 'broadcast', 'build', 'built', 'built', 'burn', 'burnt', 'burnt', 'burst',
             'burst', 'burst', 'buy', 'bought', 'bought', 'can', 'could', 'cast', 'cast', 'cast', 'catch', 'caught', 'caught', 'choose',
             'chose', 'chosen', 'cling', 'clung', 'clung', 'come', 'came', 'come', 'cost', 'cost', 'cost', 'creep', 'crept', 'crept',
             'cut', 'cut', 'cut', 'deal', 'dealt', 'dealt', 'dig', 'dug', 'dug', 'do', 'did', 'done', 'draw', 'drew', 'drawn', 'dream',
             'dreamt', 'dreamt', 'drink', 'drank', 'drunk', 'drive', 'drove', 'driven', 'dwell', 'dwelt', 'dwelt', 'eat', 'ate', 'eaten',
             'interweave', 'interwove', 'interwoven', 'fall', 'fell', 'fallen', 'feed', 'fed', 'fed', 'feel', 'felt', 'felt', 'fight',
             'fought', 'fought', 'find', 'found', 'found', 'flee', 'fled', 'fled', 'fling', 'flung', 'flung', 'fly', 'flew', 'flown',
             'forbid', 'forbad(e)', 'forbidden', 'forecast', 'forecast', 'forecast', 'forget', 'forgot', 'forgotten', 'forgive',
             'forgave', 'forgiven', 'forsake', 'forsook', 'forsaken', 'foresee', 'foresaw', 'foreseen', 'foretell', 'foretold',
             'foretold', 'freeze', 'froze', 'frozen', 'get', 'got', 'got', 'give', 'gave', 'given', 'go', 'went', 'gone', 'grind',
             'ground', 'ground', 'grow', 'grew', 'grown', 'hang', 'hung', 'hung', 'have', 'had', 'had', 'hear', 'heard', 'heard',
             'hide', 'hid', 'hidden', 'hit', 'hit', 'hit', 'hold', 'held', 'held', 'hurt', 'hurt', 'hurt', 'keep', 'kept', 'kept',
             'kneel', 'knelt', 'knelt', 'know', 'knew', 'known', 'lay', 'laid', 'laid', 'lead', 'led', 'led', 'lean', 'leant',
             'leant', 'leap', 'leapt', 'leapt', 'learn', 'learnt', 'learnt', 'leave', 'left', 'left', 'lend', 'lent', 'lent',
             'let', 'let', 'let', 'lie', 'lay', 'lain', 'lose', 'lost', 'lost', 'make', 'made', 'made', 'mean', 'meant', 'meant',
             'meet', 'met', 'met', 'pay', 'paid', 'paid', 'mistake', 'mistook', 'mistaken', 'overhear', 'overheard', 'overheard',
             'oversleep', 'overslept', 'overslept', 'put', 'put', 'put', 'read', 'read', 'read', 'rend', 'rent', 'rent', 'rid',
             'rid', 'rid', 'ride', 'rode', 'ridden', 'ring', 'rang', 'rung', 'rise', 'rose', 'risen', 'run', 'ran', 'run', 'say',
             'said', 'said', 'see', 'saw', 'seen', 'seek', 'sought', 'sought', 'sell', 'sold', 'sold', 'send', 'sent', 'sent',
             'set', 'set', 'set', 'shake', 'shook', 'shaken', 'shed', 'shed', 'shed', 'shine', 'shone', 'shone', 'shit', 'shit/shat',
             'shit/shat', 'shoot', 'shot', 'shot', 'show', 'showed', 'shown', 'shrink', 'shrank', 'shrunk', 'shrive', 'shrove',
             'shriven', 'shut', 'shut', 'shut', 'sing', 'sang', 'sung', 'sink', 'sank', 'sunk', 'sit', 'sat', 'sat', 'slay', 'slew',
             'slain', 'sleep', 'slept', 'slept', 'slide', 'slid', 'slid', 'sling', 'slung', 'slung', 'slink', 'slunk', 'slunk',
             'slit', 'slit', 'slit', 'smell', 'smelt', 'smelt', 'smite', 'smote', 'smitten', 'speak', 'spoke', 'spoken', 'speed',
             'sped', 'sped', 'spend', 'spent', 'spent', 'spin', 'spun', 'spun', 'spit', 'spat', 'spat', 'split', 'split', 'split',
             'spoil', 'spoilt', 'spoilt', 'spread', 'spread', 'spread', 'spring', 'sprang', 'sprung', 'stand', 'stood', 'stood',
             'steal', 'stole', 'stolen', 'stick', 'stuck', 'stuck', 'sting', 'stung', 'stung', 'stink', 'stank', 'stunk', 'stride',
             'strode', 'stridden', 'strike', 'struck', 'struck', 'string', 'strung', 'strung', 'strive', 'strove', 'striven', 'swear',
             'swore', 'sworn', 'sweep', 'swept', 'swept', 'swim', 'swam', 'swum', 'swing', 'swung', 'swung', 'take', 'took', 'taken',
             'teach', 'taught', 'taught', 'tear', 'tore', 'torn', 'tell', 'told', 'told', 'think', 'thought', 'thought', 'throw',
             'threw', 'thrown', 'thrust', 'thrust', 'thrust', 'tread', 'trod', 'trodden', 'understand', 'understood', 'understood',
             'undertake', 'undertook', 'undertaken', 'undo', 'undid', 'undone', 'upset', 'upset', 'upset', 'wake', 'woke', 'woken',
             'wear', 'wore', 'worn', 'weave', 'wove', 'woven', 'weep', 'wept', 'wept', 'win', 'won', 'won', 'wind', 'wound', 'wound',
             'withdraw', 'withdrew', 'withdrawn', 'withstand', 'withstood', 'withstood', 'wring', 'wrung', 'wrung', 'write', 'wrote', 'written']

    CONJUNCTIONS = ['so', 'but', 'and', 'or', 'who', 'whom']

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
            verbs = self.VERBS

        num_verbs = 0
        for word in self.words:
            if word in verbs:
                num_verbs += 1
                if num_verbs == 2:
                    break

        conj = None
        for word in self.words:
            if word in self.CONJUNCTIONS:
                conj = (1, word)

        if num_verbs >= 2:
            print("The Entered Sentence is Compound")
        elif num_verbs == 1:
            if conj and conj[0] == 1:
                print("The Entered Sentence is Compound")
            else:
                print("the Entered Sentence is Simple")


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
