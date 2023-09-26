from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Books(db.Model):
    ''' Book Class '''
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    authors = db.Column(db.String, nullable=False)
    average_rating = db.Column(db.Float, nullable=False)
    isbn = db.Column(db.String, nullable=False)
    isbn13 = db.Column(db.String, nullable=False)
    language_code = db.Column(db.String, nullable=False)
    num_pages = db.Column(db.Integer, nullable=False)
    ratings_count = db.Column(db.Integer, nullable=False)
    text_reviews_count = db.Column(db.Integer, nullable=False)
    publication_date = db.Column(db.String, nullable=False)
    publisher = db.Column(db.String, nullable=False)
    stock = db.Column(db.Integer, nullable=False, default=0)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Members(db.Model):
    ''' Member Class '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    outstanding_debt = db.Column(db.Numeric(10, 2), default=0.0)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Transactions(db.Model):
    ''' Transaction Class '''
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey(
        'books.id'), nullable=False)
    member_id = db.Column(db.Integer, db.ForeignKey(
        'members.id'), nullable=False)
    issue_date = db.Column(db.Date, nullable=False)
    return_date = db.Column(db.Date, nullable=True)
    rent_fee = db.Column(db.Numeric(10, 2), default=0.0)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
