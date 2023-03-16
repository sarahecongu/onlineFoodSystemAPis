#end point file
#registering a user
from flask import jsonify,request,Blueprint
#from validate_email import validate_email
from werkzeug.security import check_password_hash,generate_password_hash
from backend .users.user import User,db

users = Blueprint('users',__name__,url_prefix='/users')

#get all users
@users.route('/')
def all_users():
    users = User.query.all()
    results = [
        {
            "name":k.name,
            "email":k.email,
            "contact":k.contact
        } for k in users
    ]

    return jsonify({"count":len(results),"users":results})

#creating a user
@users.route("/create",methods =['POST',"GET"])
def create_user():
    name = request.json['name']
    email = request.json['email']
    contact = request.json['contact']
    address = request.json['address']
    password = request.json['password']
    usertype = request.json['usertype']
    hashed_password = generate_password_hash(password)

#Validation
    if not name:
        return jsonify({'message':'Username is required'}),400
    
    if not email:
        return jsonify({'message':'Email is required'}),400
    
    if not address:
        return jsonify({'message':'Address is required'}),400
    
    if not contact:
        return jsonify({'message':'contact is required'}),400
    
    if not password:
        return jsonify({'message':'password is required'}),400

    if len(password) <7:
        return jsonify({'message':'password must be greater than 7 characters'})
    
    
#storing a new user
    new_user = User(name=name,contact=contact,email=email,address=address,password=hashed_password,usertype=usertype)
    # adding a new user
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'Success':True,'Message':'You have successfully registered','Data':[new_user.name,new_user.address,new_user.contact,new_user.email,new_user.password]}),201

# # get
@users.route('/get/<int:id>', methods=['GET'])
def get_users(id):
    user = User.query.get_or_404(id)
    user.name = request.json['name']
    user.email = request.json['email']
    user.contact = request.json['contact']
    user.address = request.json['address']
    user.password = request.json['password']
    user.usertype = request.json['usertype']
    user.hashed_password = generate_password_hash['password']

    
    db.session.add(user)
    db.session.commit()
    return jsonify({"success": True,"user":user,"message":"user details retrieved"})

          
#     # put
@users.route('/update/<int:id>', methods=['PUT'])
def update_users(id):
    user = User.query.get_or_404(id)

    user.name =request.json['name']
       
    db.session.add(user)
    db.session.commit()
    return jsonify({"message":"user updated successfully"})
   

# # delete
@users.route('/delete/<int:id>', methods=['DELETE'])
def delete_users(id):
    user = User.query.get_or_404(id)

    db.session.delete(user)
    db.session.commit()
    return jsonify ({"message":"user successfully deleted."})