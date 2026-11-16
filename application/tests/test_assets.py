from database import get_assets, search_asset


def test_get_assets():

    assets = get_assets()

    assert isinstance(assets, list)


def test_search_asset():

    result = search_asset("Dell Laptop")

    assert result is not None
