import random
import string
import time


def gerar_senha(tamanho=8):
    """
    Gera uma senha aleatória com letras, dígitos e pontuação.
    """
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha


if __name__ == "__main__":
    try:
        tamanho = int(input("Digite o tamanho da senha: "))
    except ValueError:
        print("Entrada inválida. Usando tamanho padrão de 8.")
        tamanho = 8

    # Efeito visual de carregando...
    print("Gerando senha", end="", flush=True)
    for _ in range(3):
        time.sleep(1)
        print(".", end="", flush=True)
    print("\n")

    senha_gerada = gerar_senha(tamanho)
    print("Senha gerada:", senha_gerada)
    print("Senha salva com sucesso. Até logo!")

    print("⚠️ Atenção: o arquivo será sobrescrito!")
    with open("senha.txt", "w", encoding="utf-8") as arquivo_senha:
        arquivo_senha.write(senha_gerada + "\n")
