import math
import random

def is_prime(n: int) -> bool:
    """Teste si un nombre est premier (méthode simple)."""
    if n < 2:
        return False
    if n % 2 == 0 and n != 2:
        return False
    for i in range(3, int(math.isqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def generate_prime(bits: int = 8) -> int:
    """Génère un nombre premier aléatoire de 'bits' bits (par défaut 8)."""
    while True:
        p = random.getrandbits(bits)
        if is_prime(p):
            return p


def egcd(a: int, b: int):
    """Algorithme d’Euclide étendu. Retourne (pgcd, x, y) tel que ax + by = pgcd."""
    if a == 0:
        return b, 0, 1
    g, y, x = egcd(b % a, a)
    return g, x - (b // a) * y, y


def modinv(a: int, m: int) -> int:
    """Inverse modulaire de a modulo m."""
    g, x, _ = egcd(a, m)
    if g != 1:
        raise Exception("Pas d'inverse modulaire")
    return x % m
