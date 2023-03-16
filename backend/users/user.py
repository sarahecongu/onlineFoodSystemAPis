from app import db;



class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    contact = db.Column(db.String(100),unique = True)
    email = db.Column(db.String(100),unique = True)
    address = db.Column(db.String(100))
    usertype = db.Column(db.String(100))
    password = db.Column(db.String(100),unique=True)
    orders = db.Relationship("Order",backref = "order")
    




#function call
def __init__(self,name,contact,address,usertype,password,email):
    # self.id = id
    self.name= name
    self.contact = contact
    self.address = address
    self.usertype = usertype
    self.password = password
    self.email =email



def __repr__(self):
    return f"<User{self.name}>"

