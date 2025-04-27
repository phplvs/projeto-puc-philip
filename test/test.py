import asyncio
import pytest
import string
import pytest_asyncio
import random
from unittest.mock import patch

# Definir a versão assíncrona da função gerar_senha
async def gerar_senha_assincrona(TAMANHO=8):
    """Versão assíncrona de gerar_senha"""
    if TAMANHO < 4 or TAMANHO > 64:
        raise ValueError("O tamanho da senha deve ser entre 4 e 64 caracteres.")
    caracteres = string.ascii_letters + string.digits + string.punctuation
    # Simula um processo assíncrono, como uma chamada a uma API ou I/O
    await asyncio.sleep(0.1)  # Simulação de espera assíncrona
    senha = ''.join(random.choice(caracteres) for _ in range(TAMANHO))
    return senha

@pytest.mark.asyncio
async def test_gerar_senha_tamanho_valido():
    """Verifica se a senha gerada tem o tamanho correto"""
    senha = await gerar_senha_assincrona(8)
    assert len(senha) == 8, "A senha gerada deve ter 8 caracteres"

@pytest.mark.asyncio
async def test_gerar_senha_tamanho_minimo():
    """Verifica se o tamanho mínimo de 4 caracteres é respeitado"""
    senha = await gerar_senha_assincrona(4)
    assert len(senha) == 4, "A senha gerada deve ter 4 caracteres"

@pytest.mark.asyncio
async def test_gerar_senha_tamanho_maximo():
    """Verifica se o tamanho máximo de 64 caracteres é respeitado"""
    senha = await gerar_senha_assincrona(64)
    assert len(senha) == 64, "A senha gerada deve ter 64 caracteres"

@pytest.mark.asyncio
async def test_gerar_senha_tamanho_invalido_menor_que_4():
    """Verifica se gera ValueError para senha com tamanho menor que 4"""
    with pytest.raises(ValueError):
        await gerar_senha_assincrona(3)

@pytest.mark.asyncio
async def test_gerar_senha_tamanho_invalido_maior_que_64():
    """Verifica se gera ValueError para senha com tamanho maior que 64"""
    with pytest.raises(ValueError):
        await gerar_senha_assincrona(65)

@pytest.mark.asyncio
async def test_gerar_senha_com_caracteres_permitidos():
    """Verifica se a senha contém apenas caracteres permitidos"""
    senha = await gerar_senha_assincrona(8)
    caracteres_permitidos = string.ascii_letters + string.digits + string.punctuation
    assert all(c in caracteres_permitidos for c in senha), "A senha contém caracteres inválidos"
