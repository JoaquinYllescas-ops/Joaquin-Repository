def afd_general(cadena, token_esperado):
    """AFD genérico para cualquier token constante"""
    estado = 0
    for c1, c2 in zip(cadena, token_esperado):
        if c1 != c2:
            return 0
    return 1 if len(cadena) == len(token_esperado) else 0
