#importing some modules
from flask import  jsonify, request, Blueprint
from backend.addresses.address import Address
from backend.db import db
#creating a blueprint of address
addresses = Blueprint('addresses',__name__,url_prefix='/addresses' )

#getting all addresses
@addresses.route('/')
def all_addresses():
    addresses = Address.query.all()
    results = [
        {
         "name" :y.name,

        } for y in addresses
    ]

    return {"count":len(results),"Addresses":results}

#creating a new address ids are auto generated
@addresses.route('/create', methods= ['POST'])
def create_new_address():

    name = request.json['name']
    district_id = request.json['district_id']


    
    


    


#validations
    if not name:
        return jsonify({'message':'name is required'}),400
    
    if not district_id:
        return jsonify({'message':'district_id is required'}),400

    


#storing values
    new_address =Address(name=name,district_id=district_id) 
    db.session.add( new_address)
    db.session.commit()
    return jsonify({'success':True,'message':'New Address confirmed ','data':new_address.name}),201
        
@addresses.route('/address/<int:id>', methods=['GET'])
def get_address(id):
    address = Address.query.get_or_404(id)
    
    return jsonify({"success": True, "address": address,"message":"address details retrieved"})

          
#     # put
@addresses.route('/update/<int:id>', methods=['PUT'])
def update_address(id):
    address = Address.query.get_or_404(id)

    address.name =request.json['name']
       
    db.session.add(address),
    db.session.commit()
    return jsonify({"message":"address updated successfully"})
   

# # delete
@addresses.route('/delete/<int:id>', methods=['DELETE'])
def delete_address(id):
    address = Address.query.get_or_404(id)

    db.session.delete(address)
    db.session.commit()
    return jsonify ({"message":"address successfully deleted."})