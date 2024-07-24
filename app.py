from flask import Flask, request, jsonify
from config import Config
from repositories import get_repository

app = Flask(__name__)
config = Config()
repository = get_repository(config.repository_type)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = repository.create_user(data['name'])
    return jsonify(user.to_dict()), 201

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = repository.get_user(user_id)
    if user:
        return jsonify(user.to_dict())
    return jsonify({'error': 'User not found'}), 404

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = repository.update_user(user_id, data['name'])
    if user:
        return jsonify(user.to_dict())
    return jsonify({'error': 'User not found'}), 404

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    success = repository.delete_user(user_id)
    if success:
        return jsonify({}), 204
    return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
