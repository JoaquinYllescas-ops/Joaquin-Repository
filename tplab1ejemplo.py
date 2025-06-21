ESTADO_FINAL = "ESTADO FINAL"
ESTADO_NO_FINAL = "NO ACEPTADO"
ESTADO_TRAMPA = "EN ESTADO TRAMPA" # La distinción entre estado trampa y no final es porque si bien en ambos casos la cadena 
                                   # actual no es aceptada, estando en un estado final ante el siguiente carácter de entrada el 
                                   # estado puede cambiar, mientras en el trampa no pues es un pozo
TOKENS_POSIBLES = [("TOKEN1", automata_token1),("TOKEN2", automata_token2),...,("ID", automata_id),...,("TOKENJ", automata_tokenj)]

# EJEMPLO DE AFD IMPLEMENTADO POR CODIFICACIÓN DIRECTA
def automata_token1(lexema): # Autómata correspondiente al token 1
    estado = 0 #Variable que contendrá el estado actual del AF
    estados_finales = [1] # Conjunto de estados finales para este autómata
    for caracter in lexema:
        if estado == 0 and caracter==...:
            estado = ...
        elif estado == ... and ...:
            ....
        elif ....
        ....
        ....
        else:
            estado = -1
            break # Si se llega a un estado trampa, finaliza la simulación del autómata

    if estado == -1:
        return ESTADO_TRAMPA
    if estado in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL

....
....
....
# EJEMPLO DE AFD IMPLEMENTADO POR TABLA
def automata_tokenj(lexema): # Autómata correspondiente al token j
    estado = 0 #Variable que contendrá el estado actual del AFD
    estados_finales = [1] # Conjunto de estados finales para este autómata
    delta = {0:{'a1': estadoi,'a2': estadok,...}},...,n:{'a1': estadoi,...,'at': estadok,...}}
    for caracter in lexema:
        if caracter in delta[estado].keys():
            estado = delta[estado][caracter]
        else:
            estado = -1
            break # Si se llega a un estado trampa, finaliza la simulación del autómata

    if estado == -1:
        return ESTADO_TRAMPA
    if estado in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL
    
...
...
...


def lexer(codigo_fuente):
    tokens = [] # listada de tokens que devolverá el lexer correspondiente al código fuente ingresado, se inicializa vacia
    posicion_actual = 0   # carácter actual en el código fuente que se esta procesando
    while posicion_actual < len(codigo_fuente):
        while codigo_fuente[posicion_actual].isspace(): # NO LO VAMOS A HACER ASI
                                                        # CREAR UN TOKEN QUE DETECTE  ' ' \n y \t
             posicion_actual = posicion_actual +1

        comienzo_lexema = posicion_actual # el siguiente lexema comienza en la última posición procesada
        posibles_tokens = [] # categorías de tokens posibles para el lexema actual
        posibles_tokens_con_un_caracter_mas = [] # categorías de tokens posibles para el lexema actual mas el próximo caracter
        lexema = "" # Se inicializa el siguiente lexema
        var_aux_todos_en_estado_trampa = False

        while not var_aux_todos_en_estado_trampa:
            var_aux_todos_en_estado_trampa = True
            lexema = codigo_fuente[comienzo_lexema:posicion_actual + 1]
            posibles_tokens = posibles_tokens_con_un_caracter_mas
            posibles_tokens_con_un_caracter_mas = []

            for (un_tipo_de_token, afd) in TOKENS_POSIBLES:
                simulacion_afd = afd(lexema) # simula la ejecución de cada AFD para el lexema actual agregando un carácter
                if simulacion_afd == ESTADO_FINAL:
                    posibles_tokens_con_un_caracter_mas.append(un_tipo_de_token)
                    var_aux_todos_en_estado_trampa = False
                elif simulacion_afd == ESTADO_NO_FINAL:
                    var_aux_todos_en_estado_trampa = False
            
            posicion_actual = posicion_actual + 1 #Convierte la posición simulada en la actual, ya sea para continuar avanzando en 
                                                  # en el lexema actual, o convertir en la posición inicial del próximo

        if len(posibles_tokens) == 0:
            raise Exception("ERROR:TOKEN DESCONOCIDO" + lexema) # Aquí crear el token de tipo error

        un_tipo_de_token = posibles_tokens[0] # Mientras haya posibilidad de avanzar, ya sea por estar en un estado final o no 
                                              # final el algoritmo avanza, con lo cual siempre devuelve el lexema más largo que 
                                              # coincide con un token; En caso de haber más de uno, devuelve el primero de la lista
                                              # según la precedencia elegida por el creador del lexer en TOKENS_POSIBLES
        token = (un_tipo_de_token, lexema)
        tokens.append(token)

    return tokens

print(lexer("cadena de prueba"))