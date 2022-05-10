from website import app
import os

if __name__ == "__main__":
    port_nr = os.getenv('PORT', default=8000)
    app.run(port=port_nr, host='0.0.0.0')
