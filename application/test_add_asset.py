from database import add_asset, get_assets

add_asset(
    "Dell Laptop",
    "Laptop",
    "DL123456",
    "Steve",
    "Active"
)

assets = get_assets()

print(assets)
