"""Módulo para gerar uma senha aleatória e salvar em arquivo."""

from fastapi import FastAPI
import random
import string
import time

app = FastAPI()

def gerar_senha(TAMANHO=8):
    # Validação de tamanho
    if TAMANHO < 4 or TAMANHO > 64:
        raise ValueError("O tamanho da senha deve ser entre 4 e 64 caracteres.")
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(TAMANHO))
    return senha

if __name__ == "__main__":
    try:
        tamanho = int(input("Digite o tamanho da senha: "))  # pylint: disable=invalid-name
    except ValueError:
        print("Entrada inválida. Usando tamanho padrão de 8.")
        tamanho = 8

    # Efeito visual de carregando...
    print("Gerando senha", end="", flush=True)
    for _ in range(3):
        time.sleep(1)
        print(".", end="", flush=True)
    print("\n")

    senha_gerada = gerar_senha(tamanho)  # pylint: disable=invalid-name
    print("Senha gerada:", senha_gerada)
    print("Senha salva com sucesso. Até logo!")

    print("⚠️ Atenção: o arquivo será sobrescrito!")
    with open("senha.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(senha_gerada + "\n")

        print("Senha salva no arquivo 'senha.txt'.")
        with open("senha.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write(senha_gerada + "\n")
