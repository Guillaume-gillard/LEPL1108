def toBinary(n):
    """
    Convertit un entier n en un string contenant la séquence sur un octet (ou 8 bits).

    Args:
        n (int): L'entier à convertir en représentation binaire 8 bits.
    Returns:
        str_bin (string): Forme binaire de l'entier en string.
    """
    q = None # quotient 
    r = None # rest 
    div = n # dividend
    str_bin = ""
    while q != 0 :
        r = div % 2
        q = div // 2
        str_bin = str(r) + str_bin
        div = q
    return str_bin

print(toBinary(4545156))

print(int(10))