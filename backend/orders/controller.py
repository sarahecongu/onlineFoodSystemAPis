#importing some modules
from flask import  jsonify, request, Blueprint
from backend.orders.order import Order
from backend.db import db
#creating a blueprint of address
orders = Blueprint('orders',__name__,url_prefix='/orders' )

#getting all orders
@orders.route('/')
def all_orders():
    orders = Order.query.all()
    results = [
        {
            "name" :y.name,
            "quantity":y.quantity,
            "location":y.location,
            "status":y.status,
            "user_id":y.user_id,
            "fooditem_id":y.fooditem

        } for y in orders
    ]

    return {"count":len(results),"orders":results}

#creating a new address ids are auto generated
@orders.route('/create', methods= ['POST','GET'])
def create_new_order():

    name = request.json['name']
    quantity = request.json['quantity']
    location = request.json['location']
    status = request.json['status']
    user_id = request.json['user_id']
    fooditem_id = request.json['fooditem_id']


    
    

#validations
    if not name:
        return jsonify({'message':'name is required'}),400
    if not status:
        return jsonify({'message':'status is required'}),400
    if not quantity:
        return jsonify({'message':'quantity is required'}),400
    if not location:
        return jsonify({'message':'location is required'}),400
    if not user_id:
        return jsonify({'message':'user-id is required'}),400
    if not fooditem_id:
        return jsonify({'message':'fooditem-id is required'}),400

# storing values
    new_order =Order(name=name,status=status,location=location,quantity=quantity) 
    db.session.add( new_order)
    db.session.commit()
    return jsonify({'success':True,'message':'New Address confirmed ','data':new_order.name}),201
        
# # get
@orders.route('/region/<int:id>', methods=['GET'])
def get_order(id):
    order = Order.query.get_or_404(id)
    
    return jsonify({"success": True, "region": order,"message":"order details retrieved"})

          
#     # put
@orders.route('/update/<int:id>', methods=['PUT'])
def update_order(id):
    order = Order.query.get_or_404(id)

    order.name =request.json['name']
    order.user_id =request.json['user_id']
    order.status =request.json['status']
    order.quantity =request.json['quantity']
    order.fooditem_id =request.json['fooditem_id']


       
    db.session.add(order),
    db.session.commit()
    return jsonify({"message":"orders updated successfully"})
   

# # delete
@orders.route('/delete/<int:id>', methods=['DELETE'])
def delete_order(id):
    order = Order.query.get_or_404(id)

    db.session.delete(order)
    db.session.commit()
    return jsonify ({"message":"order successfully deleted."})