import os
import psycopg2


def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        database=os.getenv("DB_NAME", "asset_management"),
        user=os.getenv("DB_USER", "assetadmin"),
        password=os.getenv("DB_PASSWORD")
    )

def add_asset(asset_name, asset_type, serial_number, assigned_user, status):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO assets
        (asset_name, asset_type, serial_number, assigned_user, status)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (asset_name, asset_type, serial_number, assigned_user, status)
    )

    conn.commit()
    cur.close()
    conn.close()


def get_assets():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM assets")

    assets = cur.fetchall()

    cur.close()
    conn.close()

    return assets

def search_asset(asset_name):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM assets WHERE asset_name = %s",
        (asset_name,)
    )

    asset = cur.fetchall()

    cur.close()
    conn.close()

    return asset
    
def get_asset_by_id(asset_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM assets WHERE asset_id = %s",
        (asset_id,)
    )

    asset = cur.fetchone()

    cur.close()
    conn.close()

    return asset


def update_asset(asset_id, status):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        UPDATE assets
        SET status = %s
        WHERE asset_id = %s
        """,
        (status, asset_id)
    )

    conn.commit()

    cur.close()
    conn.close()


def delete_asset(asset_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM assets WHERE asset_id = %s",
        (asset_id,)
    )

    conn.commit()

    cur.close()
    conn.close()
