
# MD5 Cracker

# Importando as Bibliotecas
import hashlib
import sys

# Função da MD5
def get_md5_hash(input_string):
    md5_hasher = hashlib.md5()
    md5_hasher.update(input_string.encode('utf-8'))
    hash_string = md5_hasher.hexdigest()
    return hash_string

# Argumentos e Variaáveis para as funções
if len(sys.argv) < 3:
    print('Uso: python3 md5_cracker.py <wordlist> <hash>')
    sys.exit(1)

wordlist_path = sys.argv[1]
target_hash = sys.argv[2]

# Ler o conteúdo da Wordlist
with open(wordlist_path, 'r') as wordlist_file:
    for password in wordlist_file:
        password = password.strip()
        hash_guess = get_md5_hash(password)

        # Validação da senha no Wordlist
        if hash_guess == target_hash:
            print(f'Senha encontrada: {password}')
            break

        else:
            print('A senha não foi encontrada na wordlist.')
