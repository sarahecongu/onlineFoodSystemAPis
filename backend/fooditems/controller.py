#importing some modules
from flask import  jsonify, request, Blueprint
from backend.fooditems.food import FoodItem
from backend.db import db
#creating a blueprint of address
fooditems = Blueprint('fooditems',__name__,url_prefix='/fooditems' )

#getting all fooditems
@fooditems.route('/')
def all_fooditems():
    fooditems = FoodItem.query.all()
    results = [
        {
            "name" :y.name,
            "status" :y.status,
            "image" :y.image,
            "price" :y.price,


        } for y in fooditems
    ]

    return {"count":len(results),"fooditems":results}

#creating a new fooditem ids are auto generated
@fooditems.route('/create', methods= ['POST','GET'])
def create_new_fooditem():

    name = request.json['name']
    price = request.json['price']
    status = request.json['status']
    image = request.json['image']

    

    
    


    


#validations
    if not name:
        return jsonify({'message':'name is required'}),400
    if not status:
        return jsonify({'message':'status is required'}),400
    
    if not price:
        return jsonify({'message':'price is required'}),400
    if not image:
        return jsonify({'message':'image is required'}),400
    
#storing values
    new_fooditem =FoodItem(name=name,price=price,image=image,status=status) 
    db.session.add(new_fooditem)
    db.session.commit()
    return jsonify({'success':True,'message':'New fooditem confirmed ','data':new_fooditem.name}),201
        
    
# # get
@fooditems.route('/fooditems/<int:id>', methods=['GET'])
def get_order(id):
    fooditem = FoodItem.query.get_or_404(id)
    
    return jsonify({"success": True, "fooditem": fooditem,"message":"fooditem details retrieved"})

          
#     # put
@fooditems.route('/update/<int:id>', methods=['PUT'])
def update_fooditem(id):
    fooditem = FoodItem.query.get_or_404(id)

    fooditem.name =request.json['name']
    fooditem.price =request.json['price']
    fooditem.image =request.json['image']
    fooditem.status =request.json['status']


       
    db.session.add(fooditem),
    db.session.commit()
    return jsonify({"message":"fooditem updated successfully"})
   

# # delete
@fooditems.route('/delete/<int:id>', methods=['DELETE'])
def delete_fooditem(id):
    fooditem = FoodItem.query.get_or_404(id)

    db.session.delete(fooditem)
    db.session.commit()
    return jsonify ({"message":"fooditem successfully deleted."})