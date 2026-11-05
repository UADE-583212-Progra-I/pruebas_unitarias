from src.utils import validar_id_usuario, validar_nombre, validar_email
import pytest

def test_validar_id_usuario():
    # Arrange
    id_usuario = "1"
    # Act
    resultado = validar_id_usuario(id_usuario)
    # Assert
    assert resultado == True

def test_validar_nombre():
    # Arrange
    nombre = ""
    # Act
    resultado = validar_nombre(nombre)
    # Assert
    assert resultado == False


@pytest.mark.parametrize("email, esperado", [
    # Happy path
    ("username@mail.com",     True),
    ("username.lastname@mail.com",   True),
    ("username@mail.com.ar",  True),
    ("usename1@mail.com",       True),
    # Sad path
    ("username.com",     False),
    ("username@mail",     False),
    ("@mail.com",  False),
    ("",        False)
])
def test_validar_email_parametrizado(email, esperado):
    assert validar_email(email) == esperado