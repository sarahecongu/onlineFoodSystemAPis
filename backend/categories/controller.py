from flask import  jsonify, request, Blueprint
from backend.categories.category import Category
from backend.db import db


categories = Blueprint('categories', __name__, url_prefix='/categories')

#get all categories
@categories.route("/")
def all_categories():
    categories= Category.query.all()
    results = [
        {
            "name" :y.name,
            "image" :y.image,


        } for y in categories
    ]

    return {"count":len(results),"Categories":results}



#creating categories
@categories.route('/create', methods= ['POST'])
def new_food_category():
    name = request.json['name']
    image = request.json['image']

  
    #validations
    if not name:
         return jsonify({'error':"Food category name is required"})
    if not image:
         return jsonify({'error':"Food category image is required"})
    
    

    if Category.query.filter_by(name=name).first() is not None:
        return jsonify({'error': "Food category name exists"}), 409 

   
      
    #inserting values
    new_food_category = Category(name=name,image=image) 
    db.session.add(new_food_category)
    db.session.commit()
    return jsonify({'success':True,'message':'New food category created sucessfully','data': [new_food_category.name,new_food_category.image]}),201
    
  # get
@categories.route('/category/<int:id>', methods=['GET'])
def get_category(id):
    category = Category.query.get_or_404(id)
    
    return jsonify({"success": True, "category": category,"message":"category details retrieved"})

          
#     # put
@categories.route('/update/<int:id>', methods=['PUT'])
def update_category(id):
    category = Category.query.get_or_404(id)

    category.name =request.json['name']
       
    db.session.add(category),
    db.session.commit()
    return jsonify({"message":"address updated successfully"})
   

# # delete
@categories.route('/delete/<int:id>', methods=['DELETE'])
def delete_category(id):
    category = Category.query.get_or_404(id)

    db.session.delete(category)
    db.session.commit()
    return jsonify ({"message":"category successfully deleted."})
        
  
   



