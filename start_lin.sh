export FLASK_APP=website
export FLASK_ENV=development
export FLASK_DEBUG=true
flask db init
flask db migrate
flask run