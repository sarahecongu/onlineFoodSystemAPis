from backend.db import db

class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key = True)
    quantity = db.Column(db.Integer)
    location = db.Column(db.String(255),nullable=False)
    status = db.Column(db.String(255),nullable =False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    fooditem_id = db.Column(db.Integer, db.ForeignKey('fooditems.id'))
   


    def __init__(self, quantity,location,status, user_id,food_item_id):
     self.quantity = quantity
     self.location = location
     self.user_id = user_id
     self.food_item_id = food_item_id
     self.status = status
    

    def __repr__(self):
        return f"<Order {self.user_id} >"
