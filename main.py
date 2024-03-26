import re

#abri o aruqivo de leitura
file = open("read.py")

#vetores 
operadores_python = {
    '=': 'Assignment operator',
    '+': 'Addition operator',
    '-': 'Subtraction operator',
    '/': 'Division operator',
    '*': 'Multiplication operator',
    '<': 'Less than operator',
    '>': 'Greater than operator',
    '==': 'Equality operator',
    '!=': 'Inequality operator',
    '<=': 'Less than or equal to operator',
    '>=': 'Greater than or equal to operator',
    'and': 'Logical AND operator',
    'or': 'Logical OR operator',
    'not': 'Logical NOT operator',
    'in': 'Membership operator (checks if a value exists in a sequence)',
    'not in': 'Membership negation operator ',
    'is': 'Identity operator (checks if two variables refer to the same object)',
    'is not': 'Identity negation operator '
}
operadores_python_key = operadores_python.keys()

palavras_chave = {
    'int': 'Integer type', 
    'float': 'Floating point', 
    'char': 'Character type', 
    'boolean': 'Boolean type', 
    'def': 'Function', 
    'input': 'Accepts input from the user',
    'for': 'Loop through iterable objects',
    'if': 'Conditional statement',
    'print': 'Outputs text or variables to the console',
    'while': 'Loop while a condition is true',
    'else': 'Executes when the if condition is false',
    'main': 'Entry point of the program',
    'return': 'Returns a value from a function',
    'void': 'Indicates that a function does not return any value'
}
palavras_chave_key= palavras_chave.keys()

simbolos_especiais = {
    '(': 'Parêntese de abertura',
    ')': 'Parêntese de fechamento',
    '[': 'Colchete de abertura',
    ']': 'Colchete de fechamento',
    '{': 'Chave de abertura',
    '}': 'Chave de fechamento',
    ',': 'Vírgula',
    ';': 'Ponto e vírgula',
    ' ': 'Espaço',
    '.': 'Ponto'
}
simbolos_especiais_key = palavras_chave.keys()

comentarios = {
  '//':'Comentário de linha'
}
comentarios_key = comentarios.keys()

identificadores = {
    'ID': 'Identificador'
}
identificadores_key = identificadores.keys()

letras = {
    'a': 'Letra "a"',
    'á': 'Letra "á"',
    'à': 'Letra "à"',
    'â': 'Letra "â"',
    'ã': 'Letra "ã"',
    'ä': 'Letra "ä"',
    'b': 'Letra "b"',
    'c': 'Letra "c"',
    'ç': 'Letra "ç"',
    'd': 'Letra "d"',
    'e': 'Letra "e"',
    'é': 'Letra "é"',
    'ê': 'Letra "ê"',
    'ë': 'Letra "ë"',
    'f': 'Letra "f"',
    'g': 'Letra "g"',
    'h': 'Letra "h"',
    'i': 'Letra "i"',
    'í': 'Letra "í"',
    'î': 'Letra "î"',
    'ï': 'Letra "ï"',
    'j': 'Letra "j"',
    'k': 'Letra "k"',
    'l': 'Letra "l"',
    'm': 'Letra "m"',
    'n': 'Letra "n"',
    'o': 'Letra "o"',
    'ó': 'Letra "ó"',
    'ô': 'Letra "ô"',
    'õ': 'Letra "õ"',
    'ö': 'Letra "ö"',
    'p': 'Letra "p"',
    'q': 'Letra "q"',
    'r': 'Letra "r"',
    's': 'Letra "s"',
    't': 'Letra "t"',
    'u': 'Letra "u"',
    'ú': 'Letra "ú"',
    'û': 'Letra "û"',
    'ü': 'Letra "ü"',
    'v': 'Letra "v"',
    'w': 'Letra "w"',
    'x': 'Letra "x"',
    'y': 'Letra "y"',
    'z': 'Letra "z"'
}

numeros = {
    '0': 'Número zero',
    '1': 'Número um',
    '2': 'Número dois',
    '3': 'Número três',
    '4': 'Número quatro',
    '5': 'Número cinco',
    '6': 'Número seis',
    '7': 'Número sete',
    '8': 'Número oito',
    '9': 'Número nove',
}
numeros_key = numeros.keys()

padrao_numero_inteiro = r'\b\d+\b'
padrao_numero_decimal = r'\b\d+\.\d+\b'
padrao_comentario = r'//.*'
padrao_identificador = r'[a-zA-Z_][a-zA-Z0-9_]*'
padrao_referencia = r'\([a-zA-Z_][a-zA-Z0-9_]\)'

constantes_texto = {
    'TEXTO': 'Constante de texto '
}
constantes_texto_key = constantes_texto.keys()

a = file.read()

programa = a.split("\n")
contagem = 0
# Itera sobre cada linha do programa
for num_linha, linha in enumerate(programa, start=1):
    print("Linha #", num_linha, "\n", linha)
    tokens = linha.split()
    print("Tokens:", tokens)
    print("Propriedades:\n")
    for token in tokens:
        if token in operadores_python:
            print("Operador:", operadores_python[token])
        elif token in palavras_chave:
            print("Palavra-chave:", palavras_chave[token])
        elif token in simbolos_especiais:
            print("Símbolo especial:", simbolos_especiais[token])
        elif re.match(padrao_comentario, token):
            print("Comentário:", token)
        elif re.match(padrao_identificador, token):
            print("Identificador:", token)
        elif re.match(padrao_numero_decimal, token):
            print("Número decimal:", token)
        elif re.match(padrao_numero_inteiro, token):
            print("Número inteiro:", token)
        else:
            print("Error")
        

