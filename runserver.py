import os
from website import app, db


def run():
    host = os.environ.get("SERVER_HOST", "localhost")

    try:
        port = int(os.environ.get("SERVER_PORT", "5000"))
    except ValueError:
        port = 5000

    db.create_all(app=app)
    app.run(host, port)


if __name__ == "__main__":
    run()
