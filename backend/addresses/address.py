from backend.db import db;

# creating an instance of a class

class Address(db.Model):
    __tablename__='addresses'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    district_id = db.Column(db.Integer)
    district_id = db.Column(db.ForeignKey('districts.id'))
    

    

# function definition
    def __init__(self,name,district_id):
    
        self.name=name
        self.district_id = district_id
        
        

        

#function invoking
    def __repr__(self):
        return f"<Address {self.name} >"
    
    