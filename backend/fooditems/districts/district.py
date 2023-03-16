from backend.db import db

class District(db.Model):
    __tablename__ = "districts"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255),unique=True)
    region_id = db.Column(db.Integer,db.ForeignKey("regions.id"))
    addresses = db.Relationship("Address",backref="district")
   

    def __init__(self,name,region_id):
    
        self.name = name
        self.region_id = region_id

        
     
    

    def __repr__(self):
        return f"<District {self.name} >"
