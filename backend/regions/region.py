from backend.db import db;

# creating an instance of a class

class Region(db.Model):
    __tablename__='regions'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100),unique =True )
    district = db.Relationship("District", backref = "region")
    

    

# function definition
    def __init__(self,name):
        # self.id = id
        self.name=name
    
        
        

        

#function invoking
    def __repr__(self):
        return f"<Region {self.name} >"
    
    