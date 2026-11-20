from unittest.mock import patch
from database import get_assets


@patch("database.get_connection")
def test_mock_database_connection(mock_connection):

    mock_cursor = mock_connection.return_value.cursor.return_value

    mock_cursor.fetchall.return_value = [
        (1, "Test Laptop", "Laptop", "ABC123", "Steve", "In Use")
    ]

    assets = get_assets()

    assert assets[0][1] == "Test Laptop"
