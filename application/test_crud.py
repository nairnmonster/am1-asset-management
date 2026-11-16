from database import (
    add_asset,
    get_assets,
    search_asset,
    update_asset,
    delete_asset
)

# Create
add_asset(
    "Cisco Switch",
    "Network Switch",
    "CS123456",
    "Steve",
    "Active"
)

print("Assets after create:")
print(get_assets())

# Search
print("Search:")
print(search_asset("Cisco Switch"))

# Update
update_asset(4, "Retired")

print("Assets after update:")
print(get_assets())

# Delete
delete_asset(4)

print("Assets after delete:")
print(get_assets())

