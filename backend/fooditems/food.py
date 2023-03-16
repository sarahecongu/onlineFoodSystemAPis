from backend.db import db;

# creating an instance of a class

class FoodItem(db.Model):
    __tablename__='fooditems'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100))
    status = db.Column(db.String(100))
    price = db.Column(db.String(100))
    image = db.Column(db.String(100))
    categories_id = db.Column(db.Integer,db.ForeignKey("categories.id"))



    

    

# function definition
    def __init__(self,name,status,image,price,categories_id):
        self.name=name
        self.status=status
        self.image=image
        self.price=price
        self.categories_id=categories_id


        
        

        

#function invoking
    def __repr__(self):
        return f"<FoodItem {self.name} >"
    
    