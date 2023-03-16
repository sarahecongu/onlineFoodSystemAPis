#importing some modules
from flask import  jsonify, request, Blueprint
from backend.regions.region import Region
from backend.db import db
#creating a blueprint of address
regions = Blueprint('regions',__name__,url_prefix='/regions' )

#getting all regions
@regions.route('/')
def all_regions():
    regions = Region.query.all()
    results = [
        {
                        "name" :y.name,

        } for y in regions
    ]

    return {"count":len(results),"Addresses":results}

#creating a new address ids are auto generated
@regions.route('/create', methods= ['POST','GET'])
def create_new_address():

    name = request.json['name']

    
    
#validations
    if not name:
        return jsonify({'message':'name is required'}),400
#constaits
    if Region.query.filter_by(name=name).first() is not None:
        return jsonify({'error': "name is required"}), 400
    if not name:
        return jsonify({'message':'Region name is required' ,'success':'false'}),409
    existing_name =Region.query.filter_by(name=name).first() is not None
    if existing_name:
        return jsonify({'message':'Region name already exist'}),409
#storing values
    new_region =Region(name=name) 
    db.session.add( new_region)
    db.session.commit()
    return jsonify({'success':True,'message':'New region confirmed ','data':new_region.name}),201
        
# # get
@regions.route('/get/<int:id>', methods=['GET'])
def get_region(id):
    region = Region.query.get_or_404(id)
    region.name = request.json['name']
    
    db.session.add(region)
    db.session.commit()
    return jsonify({"success": True,"region":region,"message":"region details retrieved"})

          
#     # put
@regions.route('/update/<int:id>', methods=['PUT'])
def update_region(id):
    region = Region.query.get_or_404(id)

    region.name =request.json['name']
       
    db.session.add(region)
    db.session.commit()
    return jsonify({"message":"address updated successfully"})
   

# # delete
@regions.route('/delete/<int:id>', methods=['DELETE'])
def delete_region(id):
    region = Region.query.get_or_404(id)

    db.session.delete(region)
    db.session.commit()
    return jsonify ({"message":"region successfully deleted."})