from unittest.mock import patch
from src import services

def test_crear_usuario():

    # Arrange
    usuarios = [
        {"id_usuario": 1, "nombre": "Elon", "email": "elon@tesla.com"},
        {"id_usuario": 2, "nombre": "Jeff", "email": "jeff@aws.com"},
        {"id_usuario": 3, "nombre": "Bill", "email": "Bill@microsoft.com"},
        {"id_usuario": 4, "nombre": "Mark", "email": "Mark@meta.com"}
    ]

    nuevo_usuario = {
        "nombre": "Lisa",
        "email": "Lisa@amd.com"
    }

    with patch("src.services.storage.read_data") as mock_read, \
         patch("src.services.storage.write_data") as mock_write:

        mock_read.return_value = usuarios.copy()
        mock_write.return_value = True

        # Act
        resultado = services.crear_usuario(nuevo_usuario)
        mock_write.assert_called_once()
        ruta, usuarios_guardados = mock_write.call_args.args

        # Assert
        assert resultado is True
        assert len(usuarios_guardados) == 5
        # Verificar el último usuario
        assert usuarios_guardados[-1] == {
            "id_usuario": 5,
            "nombre": "Lisa",
            "email": "Lisa@amd.com"
        }