from flask import  jsonify, request, Blueprint
from backend.districts.district import District
from backend.db import db

districts = Blueprint('districts', __name__, url_prefix='/districts')

#get all districts
@districts.route("/")
def all_districts():
    districts= District.query.all()
    results = [
        {
            "name" :y.name,
            "address_id" :y.address_id,
            "region_id" :y.region_id,


            
        } for y in districts
    ]

    return {"count":len(results),"districts":results}



#creating districts
@districts.route('/create', methods= ['POST'])
def create_new_district():

    name = request.json['name']
    address_id = request.json['address_id']
    region_id = request.json['region_id']

    
    
      
  
    #validations
    if not name:
         return jsonify({'error':"District name is required"})
    if not address_id:
         return jsonify({'error':"District address_id is required"})
    if not region_id:
         return jsonify({'error':"District region_id is required"})
   
      

    if District.query.filter_by(name=name).first():
        return jsonify({'error': "District name exists"}), 409 

    new_district = District(name=name,address_id=address_id,region_id=region_id) 
      
    #inserting values
    db.session.add( new_district)
    db.session.commit()
    return jsonify({'message':'New district created sucessfully','data': {'name':new_district.name,'region_id':new_district.region_id,'address_id':new_district.address_id}}),201

# get
@districts.route('/districts/<int:id>', methods=['GET'])
def get_district(id):
    district = District.query.get_or_404(id)
    
    return jsonify({"success": True, "district": district,"message":"district details retrieved"})

          
#     # put
@districts.route('/update/<int:id>', methods=['PUT'])
def update_region(id):
    district = District.query.get_or_404(id)

    district.name =request.json['name']
       
    db.session.add(district),
    db.session.commit()
    return jsonify({"message":"address updated successfully"})
   

# # delete
@districts.route('/delete/<int:id>', methods=['DELETE'])
def delete_region(id):
    district = District.query.get_or_404(id)

    db.session.delete(district)
    db.session.commit()
    return jsonify ({"message":"district successfully deleted."})