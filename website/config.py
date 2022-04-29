from website import app

app.config['SECRET_KEY'] = 'a6ffe27dfffdee4138f79a9dc7f5619c'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
