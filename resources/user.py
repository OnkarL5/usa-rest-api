from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.user import UserModel
#changed

class UserRegister(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('username',
		type=str,
		required=True,
		help="username cannot be blank."
	)

	parser.add_argument('firstName',
		type=str,
		required=True,
		help="firstName cannot be blank"
	)

	parser.add_argument('lastName',
		type=str,
		required=True,
		help="lastName cannot be blank"
	)

	parser.add_argument('email',
		type=str,
		required=True,
		help="email cannot be blank"
	)

	parser.add_argument('phone',
		type=str,
		required=True,
		help="phone cannot be blank"
	)

	parser.add_argument('profilePic',
		type=str,
		required=True,
		help="insert profilePic"
	)

	parser.add_argument('pincode',
		type=str,
		required=True,
		help="pincode cannot be blank"
	)

	parser.add_argument('password',
		type=str,
		required=True,
		help="password cannot be blank"
	)

	def post(self):
		data = UserRegister.parser.parse_args()

		if UserModel.find_by_username(data['username']):
			return {"message": "A user with that username already exists"}, 400

		user = UserModel(data['username'], data['firstName'], data['lastName'], data['email'], data['phone'], data['profilePic'], data['pincode'], data['password'])
		user.save_to_db()
		return {"message": "User created successfully."}, 201


class User(Resource):
	def get(self,username):
		usa = UserModel.find_by_username(username)
		if usa:
			return usa.json(), 200
		return {'message': 'user not found'}, 404
