from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import DEXAccount, db

dex_bp = Blueprint('dex', __name__, url_prefix='/api/dex')

@dex_bp.route('/connect', methods=['POST'])
@jwt_required()
def connect_dex_account():
    user_id = get_jwt_identity()
    data = request.get_json()
    exchange_name = data.get('exchange_name')
    api_key = data.get('api_key')
    api_secret = data.get('api_secret')
    
    # Check if the DEX account already exists for the user
    existing_account = DEXAccount.query.filter_by(user_id=user_id, exchange_name=exchange_name).first()
    if existing_account:
        return jsonify({'message': 'DEX account already connected'}), 400
    
    # Create a new DEX account
    new_account = DEXAccount(user_id=user_id, exchange_name=exchange_name, api_key=api_key, api_secret=api_secret)
    db.session.add(new_account)
    db.session.commit()
    
    return jsonify({'message': 'DEX account connected successfully'}), 201

@dex_bp.route('/accounts', methods=['GET'])
@jwt_required()
def get_dex_accounts():
    user_id = get_jwt_identity()
    accounts = DEXAccount.query.filter_by(user_id=user_id).all()
    
    account_data = []
    for account in accounts:
        account_data.append({
            'id': account.id,
            'exchange_name': account.exchange_name
        })
    
    return jsonify({'accounts': account_data}), 200

@dex_bp.route('/balances', methods=['GET'])
@jwt_required()
def get_dex_balances():
    user_id = get_jwt_identity()
    accounts = DEXAccount.query.filter_by(user_id=user_id).all()
    
    balances_data = []
    for account in accounts:
        # Retrieve token balances for each connected DEX account
        # You'll need to implement the logic to fetch balances from the respective DEX APIs
        # Example:
        # balances = fetch_balances_from_dex(account.api_key, account.api_secret)
        # balances_data.append({
        #     'exchange_name': account.exchange_name,
        #     'balances': balances
        # })
        pass
    
    return jsonify({'balances': balances_data}), 200