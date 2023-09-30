import requests

from decimal import Decimal
from flask import Blueprint, request
from ..models import db, Transactions, Members, Books


transactions = Blueprint('transactions', __name__)


@transactions.route('/transactions/<int:transaction_id>', methods=['GET'])
def get_transaction(transaction_id):
    ''' Get a transaction by id '''
    transaction = Transactions.query.get(transaction_id)
    if transaction is None:
        return {'error': 'Transaction not found'}, 404
    return {'transaction': transaction.to_dict()}, 200


@ transactions.route('/transactions', methods=['POST'])
def add_transaction():
    ''' Add a new transaction '''
    data = request.get_json()
    # Convert rent_fee to decimal type for database
    data['rent_fee'] = Decimal(data['rent_fee'])
    transaction = Transactions(**data)
    db.session.add(transaction)

    # Update the member's outstanding debt and the book's stock
    member = Members.query.get(transaction.member_id)
    book = Books.query.get(transaction.book_id)

    if member.outstanding_debt + transaction.rent_fee > 500:
        db.session.rollback()
        return {'error': "Outstanding debt cannot exceed Rs.500"}, 409

    member.outstanding_debt += transaction.rent_fee
    book.stock -= 1

    if book.stock < 0:
        db.session.rollback()
        return {'error': "Not enough stock"}, 409

    db.session.commit()

    return {'id': transaction.id}, 201


@ transactions.route('/transactions/<int:transaction_id>', methods=['DELETE'])
def delete_transaction(transaction_id):
    ''' Delete a transaction by id '''
    transaction = Transactions.query.get(transaction_id)
    if transaction is None:
        return {'error': 'Transaction not found'}, 404

    # Update the member's outstanding debt and the book's stock
    member = Members.query.get(transaction.member_id)
    book = Books.query.get(transaction.book_id)

    member.outstanding_debt -= transaction.rent_fee
    book.stock += 1

    db.session.delete(transaction)
    db.session.commit()

    return {}, 204


@ transactions.route('/transactions/<int:transaction_id>/return', methods=['PUT'])
def return_book(transaction_id):
    ''' Handle book return and payment of outstanding debt for that book '''
    data = request.get_json()
    return_date = data.get('return_date')
    if not return_date:
        return {'error': 'Return date is required'}, 400

    transaction = Transactions.query.get(transaction_id)
    if transaction is None:
        return {'error': 'Transaction not found'}, 404

    # Update the member's outstanding debt and the book's stock
    member = Members.query.get(transaction.member_id)
    book = Books.query.get(transaction.book_id)

    # Check if the book has already been returned
    if transaction.return_date is not None:
        return {'error': 'Book has already been returned'}, 409

    # Update the return date
    transaction.return_date = return_date

    # Reduce the member's outstanding debt by the rent fee of the transaction
    member.outstanding_debt -= transaction.rent_fee
    if member.outstanding_debt < 0:
        member.outstanding_debt = 0

    # Increase the book's stock by 1
    book.stock += 1

    db.session.commit()

    return {'transaction': transaction.to_dict()}, 200
