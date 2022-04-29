import os
from website import app


def run():
    host = os.environ.get("SERVER_HOST", "localhost")

    try:
        port = int(os.environ.get("SERVER_PORT", "5000"))
    except ValueError:
        port = 5000

    app.run(host, port)


if __name__ == "__main__":
    run()
