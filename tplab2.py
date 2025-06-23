# 4) Desarrollo de automátas
def afd_general(cadena, token_esperado):
    estado = 0
    for c1, c2 in zip(cadena, token_esperado):
        if c1 != c2:
            return 0
    return 1 if len(cadena) == len(token_esperado) else 0

# Palabras reservadas
def afd_program(cadena): return afd_general(cadena, "program")
def afd_var(cadena): return afd_general(cadena, "var")
def afd_int(cadena): return afd_general(cadena, "int")
def afd_bool(cadena): return afd_general(cadena, "bool")
def afd_true(cadena): return afd_general(cadena, "true")
def afd_false(cadena): return afd_general(cadena, "false")
def afd_begin(cadena): return afd_general(cadena, "begin")
def afd_end(cadena): return afd_general(cadena, "end")
def afd_if(cadena): return afd_general(cadena, "if")
def afd_else(cadena): return afd_general(cadena, "else")

# Símbolos básicos de puntuación y asignación
def afd_punto(cadena): return afd_general(cadena, ".")
def afd_punto_coma(cadena): return afd_general(cadena, ";")
def afd_dos_puntos(cadena): return afd_general(cadena, ":")
def afd_asignacion(cadena): return afd_general(cadena, ":=")

# Identificador
def afd_id(cadena):
    if not cadena or not cadena[0].isalpha():
        return 0
    return all(c.isalnum() or c == '_' for c in cadena)
# Numeros, cadena de digitos
def afd_num(cadena):
    return cadena.isdigit()

# 6) 10 Casos de prueba Tiny
codigos = [
    # Ejemplo 1: Declaración simple de variables
    """
    program ejemplo1.
    var x: int;
    var flag: bool;
    begin
    end
    """,

    # Ejemplo 2: Asignación de valores básicos
    """
    program ejemplo2.
    var a: int;
    var b: bool;
    begin
        a := 10;
        b := true;
    end
    """,

    # Ejemplo 3: Estructura if-else básica
    """
    program ejemplo3.
    var condicion: bool;
    begin
        condicion := true;
        if condicion then
            x := 1;
        else
            x := 0;
    end
    """,

    # Ejemplo 4: Variables con nombres válidos
    """
    program ejemplo4.
    var var1: int;
    var _temp: bool;
    var x_y: int;
    begin
        var1 := 100;
        _temp := false;
    end
    """,

    # Ejemplo 5: Números válidos
    """
    program ejemplo5.
    var num1: int;
    var num2: int;
    begin
        num1 := 12345;
        num2 := 0;
    end
    """,

    # Ejemplo 6: Programa vacío válido
    """
    program ejemplo6.
    begin
    end
    """,

    # Ejemplo 7: Múltiples declaraciones
    """
    program ejemplo7.
    var a: int;
    var b: int;
    var c: bool;
    begin
        a := 5;
        b := 10;
        c := false;
    end
    """,

    # Ejemplo 8: If anidado (modificado para evitar operadores)
    """
    program ejemplo8.
    var x: int;
    var y: bool;
    begin
        y := true;
        if y then
            if y then
                x := 1;
            else
                x := 0;
    end
    """,

    # Ejemplo 9: Error léxico por símbolo no válido
    """
    program ejemplo9.
    var a: int;
    begin
        a := 10 @;
    end
    """,

    # Ejemplo 10: Error léxico por palabra mal escrita
    """
    program ejemplo10.
    vaar x: int;
    begin
        x := 5;
    end
    """
]

print("\n--- Resultado del Lexer ejemplos ---\n")
from collections import namedtuple
import re

Token = namedtuple('Token', ['type', 'value'])

# 5) Programa principal TINY que utiliza los autómatas previamente creados
class LexerTINY:
    def __init__(self):
        self.afds = [
            ("PROGRAM", afd_program),
            ("VAR", afd_var),
            ("INT", afd_int),
            ("BOOL", afd_bool),
            ("TRUE", afd_true),
            ("FALSE", afd_false),
            ("BEGIN", afd_begin),
            ("END", afd_end),
            ("IF", afd_if),
            ("ELSE", afd_else),
            ("ASIGNACION", afd_asignacion),
            ("PUNTO", afd_punto),
            ("PUNTO_COMA", afd_punto_coma),
            ("DOS_PUNTOS", afd_dos_puntos),
            ("NUM", afd_num),
            ("ID", afd_id)
        ]
        self.espacios = re.compile(r'\s+')

    def tokenize(self, codigo):
        tokens = []
        i = 0
        n = len(codigo)

        while i < n:
            match_espacios = self.espacios.match(codigo, i)
            if match_espacios:
                i = match_espacios.end()
                continue

            encontrado = False
            for tipo, afd in self.afds:
                max_j = min(i + 10, n)
                for j in range(i + 1, max_j + 1):
                    subcadena = codigo[i:j]
                    if afd(subcadena):
                        if j == n or not ((tipo == "ID" and (codigo[j].isalnum() or codigo[j] == '_')) or
                                         (tipo == "NUM" and codigo[j].isdigit())):
                            tokens.append(Token(tipo, subcadena))
                            i = j
                            encontrado = True
                            break
                if encontrado:
                    break

            if not encontrado:
                print(f"Error léxico: Carácter no reconocido '{codigo[i]}' en posición {i}")
                i += 1
        return tokens

lexer = LexerTINY()

for idx, codigo in enumerate(codigos, start=1):
    print(f"\n>>> Ejemplo {idx} <<<")
    tokens = lexer.tokenize(codigo)
    for token in tokens:
        print(token)
