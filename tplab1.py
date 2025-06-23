def afd_general(cadena, token_esperado):
    """AFD genérico para cualquier token constante"""
    estado = 0
    longitud = len(token_esperado)
    
    for caracter in cadena:
        if estado < longitud and caracter == token_esperado[estado]:
            estado += 1
        else:
            return 0
    
    return 1 if estado == longitud else 0
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
def afd_not(cadena): return afd_general(cadena, "not")
def afd_and(cadena): return afd_general(cadena, "and")
def afd_or(cadena): return afd_general(cadena, "or")
def afd_goto(cadena): return afd_general(cadena, "goto")

# Símbolos simples
def afd_punto(cadena): return afd_general(cadena, ".")
def afd_punto_coma(cadena): return afd_general(cadena, ";")
def afd_igual(cadena): return afd_general(cadena, "=")
def afd_asignacion(cadena): return afd_general(cadena, ":=")
def afd_dos_puntos(cadena): return afd_general(cadena, ":")
def afd_parentesis_izq(cadena): return afd_general(cadena, "(")
def afd_parentesis_der(cadena): return afd_general(cadena, ")")
def afd_suma(cadena): return afd_general(cadena, "+")
def afd_resta(cadena): return afd_general(cadena, "-")
def afd_multiplicacion(cadena): return afd_general(cadena, "*")
def afd_igualdad(cadena): return afd_general(cadena, "==")
def afd_distinto(cadena): return afd_general(cadena, "<>")
def afd_menor(cadena): return afd_general(cadena, "<")
def afd_mayor(cadena): return afd_general(cadena, ">")
def afd_menor_igual(cadena): return afd_general(cadena, "<=")
def afd_mayor_igual(cadena): return afd_general(cadena, ">=")   


def afd_id(cadena):
    """AFD para identificadores (comienzan con letra, seguido de letras, números o _)"""
    if not cadena: return 0
    
    estado = 0
    for c in cadena:
        if estado == 0:
            if c.isalpha():
                estado = 1
            else:
                return 0
        elif estado == 1:
            if not (c.isalnum() or c == '_'):
                return 0
    return 1

def afd_num(cadena):
    """AFD para números enteros (secuencia de dígitos)"""
    if not cadena: return 0
    
    for c in cadena:
        if not c.isdigit():
            return 0
    return 1 

# def probar_afds():
#     tests = [
#         ("program", afd_program),
#         ("var", afd_var),
#         ("123", afd_num),
#         ("abc123", afd_id),
#         (":=", afd_asignacion),
#         ("<>", afd_distinto),
#         ("true", afd_true),
#         ("iff", afd_if)  # Debería fallar
#     ]
    
#     for cadena, afd in tests:
#         resultado = afd(cadena)
#         print(f"'{cadena}': {resultado}")    
# probar_afds() 
import re
from collections import namedtuple

# Definición de la estructura de un token
Token = namedtuple('Token', ['type', 'value'])

class LexerTINY:
    def __init__(self):
        # Lista de todos los AFDs en orden de prioridad
        self.afds = [
            # Palabras reservadas
            ("PROGRAM", self.afd_program),
            ("VAR", self.afd_var),
            ("INT", self.afd_int),
            ("BOOL", self.afd_bool),
            ("TRUE", self.afd_true),
            ("FALSE", self.afd_false),
            ("BEGIN", self.afd_begin),
            ("END", self.afd_end),
            ("IF", self.afd_if),
            ("ELSE", self.afd_else),
            ("NOT", self.afd_not),
            ("AND", self.afd_and),
            ("OR", self.afd_or),
            ("GOTO", self.afd_goto),
            
            # Operadores y símbolos (los de más caracteres primero)
            ("ASIGNACION", self.afd_asignacion),
            ("IGUALDAD", self.afd_igualdad),
            ("MENOR_IGUAL", self.afd_menor_igual),
            ("MAYOR_IGUAL", self.afd_mayor_igual),
            ("DISTINTO", self.afd_distinto),
            ("PUNTO", self.afd_punto),
            ("PUNTO_COMA", self.afd_punto_coma),
            ("IGUAL", self.afd_igual),
            ("DOS_PUNTOS", self.afd_dos_puntos),
            ("PARENTESIS_IZQ", self.afd_parentesis_izq),
            ("PARENTESIS_DER", self.afd_parentesis_der),
            ("SUMA", self.afd_suma),
            ("RESTA", self.afd_resta),
            ("MULTIPLICACION", self.afd_multiplicacion),
            ("MENOR", self.afd_menor),
            ("MAYOR", self.afd_mayor),
            
            # Identificadores y números
            ("NUM", self.afd_num),
            ("ID", self.afd_id)
        ]
        
        # Expresión regular para saltar espacios y comentarios
        self.espacios = re.compile(r'\s+')
        self.comentarios = re.compile(r'\{.*?\}')

    # Implementación de todos los AFDs (los mismos que definimos antes)
    def afd_general(self, cadena, token_esperado):
        estado = 0
        longitud = len(token_esperado)
        
        for caracter in cadena:
            if estado < longitud and caracter == token_esperado[estado]:
                estado += 1
            else:
                return 0
        
        return 1 if estado == longitud else 0

    def afd_program(self, cadena): return self.afd_general(cadena, "program")
    def afd_var(self, cadena): return self.afd_general(cadena, "var")
    def afd_int(self, cadena): return self.afd_general(cadena, "int")
    def afd_bool(self, cadena): return self.afd_general(cadena, "bool")
    def afd_true(self, cadena): return self.afd_general(cadena, "true")
    def afd_false(self, cadena): return self.afd_general(cadena, "false")
    def afd_begin(self, cadena): return self.afd_general(cadena, "begin")
    def afd_end(self, cadena): return self.afd_general(cadena, "end")
    def afd_if(self, cadena): return self.afd_general(cadena, "if")
    def afd_else(self, cadena): return self.afd_general(cadena, "else")
    def afd_not(self, cadena): return self.afd_general(cadena, "not")
    def afd_and(self, cadena): return self.afd_general(cadena, "and")
    def afd_or(self, cadena): return self.afd_general(cadena, "or")
    def afd_goto(self, cadena): return self.afd_general(cadena, "goto")
    def afd_punto(self, cadena): return self.afd_general(cadena, ".")
    def afd_punto_coma(self, cadena): return self.afd_general(cadena, ";")
    def afd_igual(self, cadena): return self.afd_general(cadena, "=")
    def afd_asignacion(self, cadena): return self.afd_general(cadena, ":=")
    def afd_dos_puntos(self, cadena): return self.afd_general(cadena, ":")
    def afd_parentesis_izq(self, cadena): return self.afd_general(cadena, "(")
    def afd_parentesis_der(self, cadena): return self.afd_general(cadena, ")")
    def afd_suma(self, cadena): return self.afd_general(cadena, "+")
    def afd_resta(self, cadena): return self.afd_general(cadena, "-")
    def afd_multiplicacion(self, cadena): return self.afd_general(cadena, "*")
    def afd_igualdad(self, cadena): return self.afd_general(cadena, "==")
    def afd_distinto(self, cadena): return self.afd_general(cadena, "<>")
    def afd_menor(self, cadena): return self.afd_general(cadena, "<")
    def afd_mayor(self, cadena): return self.afd_general(cadena, ">")
    def afd_menor_igual(self, cadena): return self.afd_general(cadena, "<=")
    def afd_mayor_igual(self, cadena): return self.afd_general(cadena, ">=")

    def afd_id(self, cadena):
        if not cadena: return 0
        estado = 0
        for c in cadena:
            if estado == 0:
                if c.isalpha():
                    estado = 1
                else:
                    return 0
            elif estado == 1:
                if not (c.isalnum() or c == '_'):
                    return 0
        return 1

    def afd_num(self, cadena):
        if not cadena: return 0
        for c in cadena:
            if not c.isdigit():
                return 0
        return 1

    def tokenize(self, codigo):
        tokens = []
        i = 0
        n = len(codigo)
        
        while i < n:
            # Saltar espacios en blanco
            match_espacios = self.espacios.match(codigo, i)
            if match_espacios:
                i = match_espacios.end()
                continue
                
            # Saltar comentarios
            match_comentarios = self.comentarios.match(codigo, i)
            if match_comentarios:
                i = match_comentarios.end()
                continue
            
            # Probar cada AFD
            encontrado = False
            for tipo, afd in self.afds:
                # Buscar la subcadena más larga que coincida
                max_j = min(i + 10, n)  # Acoto el maximo de i para evitar sobrepasar el final del codigo fuente
                for j in range(i + 1, max_j + 1):
                    subcadena = codigo[i:j]
                    if afd(subcadena):
                        # Verificar si es la coincidencia más larga posible
                        if j == n or not ((tipo == "ID" and (codigo[j].isalnum() or codigo[j] == '_')) or 
                                         (tipo == "NUM" and codigo[j].isdigit())):
                            tokens.append(Token(tipo, subcadena))
                            i = j
                            encontrado = True
                            break
                if encontrado:
                    break
                    
            if not encontrado:
                # Carácter no reconocido
                print(f"Error léxico: Carácter no reconocido '{codigo[i]}' en posición {i}")
                i += 1
                
        return tokens     
# 6) Código de prueba en TINY
codigo_ejemplo = """
program 1.
var x: int = 10;
var flag: bool = true;
begin
    x := x + 5;
end
"""

# Crear y ejecutar el lexer
lexer = LexerTINY()
tokens = lexer.tokenize(codigo_ejemplo)

# 7) Imprimir los tokens encontrados
for token in tokens:
    print(f"Token(tipo='{token.type}', valor='{token.value}')")


codigo_ejemplo = """
program 2.
begin
    let a = 5 * (3 + 2) - 8 / 2;
    let b = a % 3;  // Error: % no es operador válido
end
"""

lexer = LexerTINY()
tokens = lexer.tokenize(codigo_ejemplo)

# 7) Imprimir los tokens encontrados
for token in tokens:
    print(f"Token(tipo='{token.type}', valor='{token.value}')")

codigo_ejemplo = """
program 3.
var n: int = 5;
begin
    if n > 0 goto positivo;
    negativo:
    n := 0;
    goto fin;
    positivo:
    n := n * 2;
    fin:
end
"""

lexer = LexerTINY()
tokens = lexer.tokenize(codigo_ejemplo)

# 7) Imprimir los tokens encontrados
for token in tokens:
    print(f"Token(tipo='{token.type}', valor='{token.value}')")

codigo_ejemplo = """
program 4.
var a: bool = true;
var b: bool = false;
begin
    let c = a and b;
    let d = not c or a;
end
"""

lexer = LexerTINY()
tokens = lexer.tokenize(codigo_ejemplo)

# 7) Imprimir los tokens encontrados
for token in tokens:
    print(f"Token(tipo='{token.type}', valor='{token.value}')")    

codigo_ejemplo = """
program 5.
var x: int = 10;
var y: int = 20;
begin
    if x >= y then goto mayor;
    if x <> y then goto diferente;
    mayor:
    diferente:
end
"""

lexer = LexerTINY()
tokens = lexer.tokenize(codigo_ejemplo)

# 7) Imprimir los tokens encontrados
for token in tokens:
    print(f"Token(tipo='{token.type}', valor='{token.value}')")  

codigo_ejemplo = """
program 6.
var 1x: int = 5;  
var @y: bool;     
begin
    x := x * 2#;  
end
"""

lexer = LexerTINY()
tokens = lexer.tokenize(codigo_ejemplo)

# 7) Imprimir los tokens encontrados
for token in tokens:
    print(f"Token(tipo='{token.type}', valor='{token.value}')") 

codigo_ejemplo = """
program 7.
var i: int = 0;
begin
    inicio:
    if i < 10 then
        if i % 2 == 0 then  
            i := i + 1;
        goto inicio;
end
"""

lexer = LexerTINY()
tokens = lexer.tokenize(codigo_ejemplo)

# 7) Imprimir los tokens encontrados
for token in tokens:
    print(f"Token(tipo='{token.type}', valor='{token.value}')")   

codigo_ejemplo = """
program 8.
begin
end
"""

lexer = LexerTINY()
tokens = lexer.tokenize(codigo_ejemplo)

# 7) Imprimir los tokens encontrados
for token in tokens:
    print(f"Token(tipo='{token.type}', valor='{token.value}')")          

codigo_ejemplo = """
program 9.
{ Este es un programa de ejemplo }
var x: int = 123;  { Valor inicial }

begin
    { Operación simple }
    x := x + 1;
end
"""

lexer = LexerTINY()
tokens = lexer.tokenize(codigo_ejemplo)

# 7) Imprimir los tokens encontrados
for token in tokens:
    print(f"Token(tipo='{token.type}', valor='{token.value}')")          

codigo_ejemplo = """
program 10.
var _var: int = 999999999;
var x_y_z: bool = false;
begin
    if _var <= 1000000000 and x_y_z == false then
        goto etiqueta_123;
    etiqueta_123:
    let z = _var * _var;
end
"""

lexer = LexerTINY()
tokens = lexer.tokenize(codigo_ejemplo)

# 7) Imprimir los tokens encontrados
for token in tokens:
    print(f"Token(tipo='{token.type}', valor='{token.value}')")          


