from website import app


@app.route("/test_view")
def test_view():
    return "Hello, world"
