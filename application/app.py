from flask import Flask, request, redirect

from database import (
    get_assets,
    add_asset,
    search_asset,
    delete_asset,
    update_asset,
    get_asset_by_id
)

app = Flask(__name__)


@app.route("/")
def home():

    assets = get_assets()

    page = """
    <h1>Asset Management System - Deployment Test</h1>

    <p>
        <a href="/add">Add Asset</a> |
        <a href="/search">Search Asset</a>
    </p>

    <h2>Current Assets</h2>

    <table border="1" cellpadding="5">
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Type</th>
            <th>User</th>
            <th>Status</th>
            <th>Actions</th>
        </tr>
    """

    for asset in assets:
        page += f"""
        <tr>
            <td>{asset[0]}</td>
            <td>{asset[1]}</td>
            <td>{asset[2]}</td>
            <td>{asset[4]}</td>
            <td>{asset[5]}</td>
            <td>
                <a href="/edit/{asset[0]}">Edit</a> |
                <a href="/delete/{asset[0]}">Delete</a>
            </td>
        </tr>
        """

    page += "</table>"

    return page


@app.route("/add", methods=["GET", "POST"])
def add():

    if request.method == "POST":

        add_asset(
            request.form["asset_name"],
            request.form["asset_type"],
            request.form["serial_number"],
            request.form["assigned_user"],
            request.form["status"]
        )

        return redirect("/")

    return """
    <h1>Add Asset</h1>

    <form method="post">

        Asset Name:<br>
        <input name="asset_name"><br><br>

        Asset Type:<br>
        <input name="asset_type"><br><br>

        Serial Number:<br>
        <input name="serial_number"><br><br>

        Assigned User:<br>
        <input name="assigned_user"><br><br>

        Status:<br>
        <input name="status"><br><br>

        <input type="submit" value="Add Asset">

    </form>

    <br>

    <a href="/">Home</a>
    """


@app.route("/search", methods=["GET", "POST"])
def search():

    results = []

    if request.method == "POST":

        results = search_asset(
            request.form["asset_name"]
        )

    page = """
    <h1>Search Asset</h1>

    <form method="post">
        Asset Name:
        <input name="asset_name">
        <input type="submit" value="Search">
    </form>

    <br>

    <a href="/">Home</a>

    <hr>
    """

    for asset in results:
        page += f"""
        <p>
            ID: {asset[0]} |
            Name: {asset[1]} |
            Status: {asset[5]}
        </p>
        """

    return page


@app.route("/edit/<int:asset_id>", methods=["GET", "POST"])
def edit(asset_id):

    asset = get_asset_by_id(asset_id)

    if request.method == "POST":

        update_asset(
            asset_id,
            request.form["status"]
        )

        return redirect("/")

    return f"""
    <h1>Edit Asset</h1>

    <p>Asset: {asset[1]}</p>

    <form method="post">

        Status:<br>
        <input name="status" value="{asset[5]}"><br><br>

        <input type="submit" value="Update">

    </form>

    <br>

    <a href="/">Home</a>
    """


@app.route("/delete/<int:asset_id>")
def delete(asset_id):

    delete_asset(asset_id)

    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
