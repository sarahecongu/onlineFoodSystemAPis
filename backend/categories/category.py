from backend.db import db

class Category(db.Model):
    __tablename__ = "categories"
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255),unique=True)
    image = db.Column(db.String(255),nullable=False)

#function call   
   
    def __init__(self,name,image):
        self.image = image
        self.name = name
    
    

    def __repr__(self):
        return f"<Category {self.name} >"
