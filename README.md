# RSA-CLI

A small Python project that implements a **homemade RSA** with an
**interactive command line interface**.\
Great for understanding how RSA works and for showcasing Python skills
on GitHub.

------------------------------------------------------------------------

## Features

-   Generate RSA keys `(e, n)` and `(d, n)`\
-   Encrypt a text message character by character\
-   Decrypt an encrypted message\
-   Interactive terminal interface (chat-like)

------------------------------------------------------------------------

## Project Structure

    rsa-cli/
    ├── rsa/
    │   ├── __init__.py
    │   ├── math_utils.py   # math utilities (primality, modular inverse…)
    │   ├── keygen.py       # RSA key generation
    │   ├── crypto.py       # encryption / decryption
    │   └── cli.py          # interactive interface
    ├── main.py             # entry point
    ├── README.md           # this file
    └── requirements.txt    # empty (standard library only)

------------------------------------------------------------------------

## Installation

Clone the repository and run Python:

``` bash
git clone https://github.com/VictorGauthier123/RSA_HOMEMADE.git
cd rsa_homemade
python main.py
```

*(Project compatible with Python ≥ 3.10, no external dependencies)*

------------------------------------------------------------------------

## Usage

Simply run:

``` bash
python main.py
```

Example session:

    === RSA CLI ===

    What do you want to do?
    1 - Generate keys
    2 - Encrypt a message
    3 - Decrypt a message
    4 - Quit
    > 1
    Prime number size (default 8) : 8
    Public key : (65537, 253)
    Private key: (153, 253)

    > 2
    Enter the message to encrypt: hello
    Public key (e,n): 65537,253
    Encrypted message: 68 147 221 147 205 19 115

    > 3
    Enter the encrypted message (numbers separated by spaces): 68 147 221 147 205 19 115
    Private key (d,n): 153,253
    Decrypted message: hello

------------------------------------------------------------------------

## Notes

-   This RSA implementation is **simplified**: small prime numbers
    (8--12 bits) → not secure.\
-   The goal is **to illustrate the algorithm** rather than provide
    real-world security.\


