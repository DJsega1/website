from website import __init__


@app.route("/test_view")
def test_view():
    return "Hello, world"
