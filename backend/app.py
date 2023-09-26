from flask import Flask
from flask_migrate import Migrate

from .models import db
from .books.routes import books
from .members.routes import members
from .transactions.routes import transactions

app = Flask(__name__)
app.register_blueprint(books)
app.register_blueprint(members)
app.register_blueprint(transactions)

app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql://admin:password@localhost:5432/library?sslmode=disable'

db.init_app(app)
migrate = Migrate(app, db)


@app.route('/library/init')
def init_db():
    ''' Initialize the database '''
    db.create_all()  # create the tables
    db.session.commit()

    return {}, 201


if __name__ == '__main__':
    app.run(debug=True)
