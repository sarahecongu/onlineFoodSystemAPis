from flask import  jsonify, request, Blueprint
from backend.sub_categories.sub_category import subCategory
from backend.db import db


sub_categories = Blueprint('sub_categories', __name__, url_prefix='/sub_categories')

#get all categories
@sub_categories.route("/")
def all_categories():
    sub_categories= subCategory.query.all()
    results = [
        {
            "name" :y.name,
            "categories_id" :y.categories_id


        } for y in sub_categories
    ]

    return {"count":len(results),"sub_Categories":results}



#creating sub_categories
@sub_categories.route('/create', methods= ['POST'])
def new_sub_category():
    name = request.json['name']
    categories_id = request.json['categories_id']
    image = request.json['image']


  
    #validations
    if not name:
         return jsonify({'error':"Food sub_category name is required"})
    if not image:
         return jsonify({'error':"Image name is required"})
    if not categories_id:
         return jsonify({'error':"Food sub_category categories_id is required"})
    
    

    if subCategory.query.filter_by(name=name).first() is not None:
        return jsonify({'error': "Food sub_category name exists"}), 409 

   
      
    #inserting values
    new_sub_category = subCategory(name=name,image=image,categories_id=categories_id) 
    db.session.add(new_sub_category)
    db.session.commit()
    return jsonify({'success':True,'message':'New food sub_category created sucessfully','data': [new_sub_category.name,new_sub_category.categories_id]}),201
    
  # get
@sub_categories.route('/sub_category/<int:id>', methods=['GET'])
def get_subcategory(id):
    sub_category = subCategory.query.get_or_404(id)
    
    return jsonify({"success": True, "sub_category": sub_category,"message":"sub_category details retrieved"})

          
#     # put
@sub_categories.route('/update/<int:id>', methods=['PUT'])
def update_subcategory(id):
    sub_category = subCategory.query.get_or_404(id)

    sub_category.name =request.json['name']
    sub_category.categories_id =request.json['categories_id']
    sub_category.image =request.json['image']


       
    db.session.add(sub_category),
    db.session.commit()
    return jsonify({"message":"address updated successfully"})
   

# # delete
@sub_categories.route('/delete/<int:id>', methods=['DELETE'])
def delete_subcategory(id):
    sub_category = subCategory.query.get_or_404(id)

    db.session.delete(sub_category)
    db.session.commit()
    return jsonify ({"message":"sub_category successfully deleted."})
        
  
   



