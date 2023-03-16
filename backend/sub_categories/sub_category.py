from backend.db import db

class subCategory(db.Model):
    __tablename__ = "sub_categories"
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255),unique=True)
    image = db.Column(db.String(255),nullable=False)
    categories_id = db.Column(db.Integer,db.ForeignKey('categories.id'))

#function call   
   
    def __init__(self,name,image,category_id):
        self.image = image
        self.name = name
        self.categories_id = category_id
    
    

    def __repr__(self):
        return f"<subCategory {self.name} >"
