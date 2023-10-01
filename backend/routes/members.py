import requests

from flask import Blueprint, request
from ..models import db, Members


members = Blueprint('members', __name__)


@members.route('/members', methods=['GET'])
def get_members():
    ''' Get members ordered by id with pagination '''
    page = request.args.get('page', 1, type=int)
    per_page = 10
    members_list = Members.query.order_by(Members.id).paginate(
        page=page, per_page=per_page, error_out=False)
    return {'members': [member.to_dict() for member in members_list.items]}, 200


@ members.route('/members/<int:member_id>', methods=['GET'])
def get_member(member_id):
    ''' Get a member by id '''
    member = Members.query.get(member_id)
    if member is None:
        return {'error': 'Member not found'}, 404
    return {'member': member.to_dict()}, 200


@ members.route('/members', methods=['POST'])
def add_member():
    ''' Add a new member '''
    data = request.get_json()
    member = Members(**data)
    db.session.add(member)
    db.session.commit()
    return {'id': member.id}, 201


@ members.route('/members/<int:member_id>', methods=['PUT'])
def update_member(member_id):
    ''' Update a member by id '''
    data = request.get_json()
    member = Members.query.get(member_id)
    if member is None:
        return {'error': 'Member not found'}, 404
    for key, value in data.items():
        setattr(member, key, value)
    db.session.commit()
    return {'member': member.to_dict()}, 200


@ members.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    ''' Delete a member by id '''
    member = Members.query.get(member_id)
    if member is None:
        return {'error': 'Member not found'}, 404
    db.session.delete(member)
    db.session.commit()
    return {}, 204
