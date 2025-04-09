import random
import string
from datetime import datetime

def gerar_senha(tamanho=8):
    caracteres = string.ascii_letters + string.digits
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

if __name__ == "__main__":
    try:
        tamanho = int(input("Dgite o tamanho da senha: "))
    except ValueError:
        print("Entrada inválida. Usando tamanho padrão de 8.")
        tamanho = 8

    senha = gerar_senha(tamanho)
    print("Senha gerada:", senha)

    with open("senha_gerada.txt", "a") as arquivo:
        agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        arquivo.write(f"{agora} - {senha}\n")