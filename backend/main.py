from sqlalchemy import func, update
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql://admin:password@localhost:5432/library?sslmode=disable'
db = SQLAlchemy(app)


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


class Members(db.Model):
    ''' Member Class '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    outstanding_debt = db.Column(db.Float, default=0.0)


class Transactions(db.Model):
    ''' Transaction Class '''
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey(
        'books.id'), nullable=False)
    member_id = db.Column(db.Integer, db.ForeignKey(
        'members.id'), nullable=False)
    issue_date = db.Column(db.Date, nullable=False)
    return_date = db.Column(db.Date, nullable=True)
    rent_fee = db.Column(db.Float, default=0.0)


@ app.route('/books', methods=['POST'])
def add_book():
    ''' Add a new book '''
    data = request.get_json()
    book = Books(**data)
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}, 201


@ app.route('/books/stock', methods=['POST'])
def add_book_stock():
    ''' Add a new book '''
    data = request.get_json()
    book_id = data.get('book_id')
    stock = data.get('stock')
    stmt = update(Books).where(
        Books.id == book_id).values({Books.stock: stock})
    db.session.execute(stmt)
    db.session.commit()
    return {'result': f'Stock update successfull for book_id: {book_id} to {stock}'}, 201


@ app.route('/members', methods=['POST'])
def add_member():
    ''' Add a new member '''
    data = request.get_json()
    member = Members(**data)
    db.session.add(member)
    db.session.commit()
    return {'id': member.id}, 201


@ app.route('/transactions', methods=['POST'])
def add_transaction():
    ''' Add a new transaction '''
    data = request.get_json()
    transaction = Transactions(**data)
    db.session.add(transaction)

    # Update the member's outstanding debt and the book's stock
    member = Members.query.get(transaction.member_id)
    book = Books.query.get(transaction.book_id)

    member.outstanding_debt += transaction.rent_fee
    book.stock -= 1

    if book.stock < 0:
        db.session.rollback()
        return {'error': "Not enough stock"}, 409

    db.session.commit()

    return {'id': transaction.id}, 201


@ app.route('/books/search', methods=['GET'])
def search_books():
    ''' Search for books by name and author '''
    title = request.args.get('title') or ""
    authors = request.args.get('authors') or ""
    books = Books.query.filter(func.lower(Books.title).contains(
        func.lower(title)), func.lower(Books.authors).contains(func.lower(authors))).all()
    return {'book_ids': [book.id for book in books]}, 200


@ app.route('/books/import', methods=['POST'])
def import_books():
    ''' Import books from the Frappe API '''
    data = request.get_json()
    response = requests.get('https://frappe.io/api/method/frappe-library',
                            params=data, timeout=30)
    books_data = response.json().get('message')

    for book_data in books_data:
        try:
            book_data_model = {
                "id": book_data.get("bookID"),
                "title": book_data.get("title"),
                "authors": book_data.get("authors"),
                "average_rating": book_data.get("average_rating"),
                "isbn": book_data.get("isbn"),
                "isbn13": book_data.get("isbn13"),
                "language_code": book_data.get("language_code"),
                "num_pages": book_data.get("  num_pages"),
                "ratings_count": book_data.get("ratings_count"),
                "text_reviews_count": book_data.get("text_reviews_count"),
                "publication_date": book_data.get("publication_date"),
                "publisher": book_data.get("publisher")
            }
            book = Books(**book_data_model)
            db.session.add(book)
        except Exception:
            db.session.rollback()

    db.session.commit()

    return {'no_imported_books': len(books_data)}, 201


@ app.route('/books/import-all', methods=['POST'])
def import_all_books():
    ''' Import books from the Frappe API '''

    i = 1
    while i <= 200:  # found by pure trial
        try:
            response = requests.get('https://frappe.io/api/method/frappe-library',
                                    params={"page": i}, timeout=30)
            books_data = response.json().get('message')
            print("Round 1" + str(i))

            for book_data in books_data:
                try:
                    book_data_model = {
                        "id": book_data.get("bookID"),
                        "title": book_data.get("title"),
                        "authors": book_data.get("authors"),
                        "average_rating": book_data.get("average_rating"),
                        "isbn": book_data.get("isbn"),
                        "isbn13": book_data.get("isbn13"),
                        "language_code": book_data.get("language_code"),
                        "num_pages": book_data.get("  num_pages"),
                        "ratings_count": book_data.get("ratings_count"),
                        "text_reviews_count": book_data.get("text_reviews_count"),
                        "publication_date": book_data.get("publication_date"),
                        "publisher": book_data.get("publisher")
                    }
                    book = Books(**book_data_model)
                    db.session.add(book)
                except Exception:
                    print("Error adding data")

            db.session.commit()
        except Exception:
            db.session.rollback()
            print("Duplicate data, rolling back db session")
        finally:
            i += 1

    return {'no_api_reqs': i}, 201


@app.route('/library/init')
def init_db():
    ''' Initialize the database '''
    db.create_all()  # create the tables
    db.session.commit()

    return {}, 201


if __name__ == '__main__':
    app.run(debug=True)
