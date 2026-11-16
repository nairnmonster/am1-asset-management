from database import get_assets


def test_database_connection():

    assets = get_assets()

    assert assets is not None
