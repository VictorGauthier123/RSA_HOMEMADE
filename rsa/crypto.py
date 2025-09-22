def encrypt(msg: str, pubkey: tuple[int, int]) -> list[int]:
    """
    Chiffre un message texte caractère par caractère avec la clé publique.
    pubkey = (e, n)
    Retourne une liste d'entiers.
    """
    e, n = pubkey
    return [pow(ord(c), e, n) for c in msg]


def decrypt(cipher: list[int], privkey: tuple[int, int]) -> str:
    """
    Déchiffre une liste d'entiers avec la clé privée.
    privkey = (d, n)
    Retourne le message texte original.
    """
    d, n = privkey
    return ''.join([chr(pow(c, d, n)) for c in cipher])
