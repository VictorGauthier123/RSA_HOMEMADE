from .keygen import generate_keys
from .crypto import encrypt, decrypt

def run_cli():
    print("=== RSA maison ===")
    while True:
        print("\nQue voulez-vous faire ?")
        print("1 - Générer des clés")
        print("2 - Chiffrer un message")
        print("3 - Déchiffrer un message")
        print("4 - Quitter")

        choice = input("> ").strip()

        if choice == "1":
            bits = input("Taille des nombres premiers (par défaut 8) : ").strip()
            bits = int(bits) if bits.isdigit() else 8
            pub, priv = generate_keys(bits=bits)
            print("Clé publique :", pub)
            print("Clé privée  :", priv)

        elif choice == "2":
            msg = input("Entrez le message à chiffrer : ")
            pub = input("Clé publique (e,n) : ")
            try:
                e, n = map(int, pub.split(","))
                cipher = encrypt(msg, (e, n))
                print("Message chiffré :", " ".join(map(str, cipher)))
            except Exception as err:
                print("Erreur :", err)

        elif choice == "3":
            cipher = input("Entrez le message chiffré (nombres séparés par des espaces) : ")
            priv = input("Clé privée (d,n) : ")
            try:
                cipher = list(map(int, cipher.split()))
                d, n = map(int, priv.split(","))
                msg = decrypt(cipher, (d, n))
                print("Message déchiffré :", msg)
            except Exception as err:
                print("Erreur :", err)

        elif choice == "4":
            print("Au revoir !")
            break

        else:
            print("Choix invalide. Réessayez.")
