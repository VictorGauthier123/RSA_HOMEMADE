import math
from .math_utils import generate_prime, modinv

def generate_keys(bits: int = 8):
    """
    Génère une paire de clés RSA (publique, privée).
    bits : taille en bits des nombres premiers.
    Retourne (pub, priv) où
      pub = (e, n)
      priv = (d, n)
    """
    # Choisir deux nombres premiers
    p = generate_prime(bits)
    q = generate_prime(bits)
    while q == p:
        q = generate_prime(bits)

    n = p * q
    phi = (p - 1) * (q - 1)

    # Exposant public
    e = 65537
    if math.gcd(e, phi) != 1:
        e = 3
        while math.gcd(e, phi) != 1:
            e += 2

    # Exposant privé
    d = modinv(e, phi)

    return (e, n), (d, n)
