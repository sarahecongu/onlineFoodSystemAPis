from backend import create_app,db
from flask_migrate import Migrate
from backend.addresses.address import Address
from backend.categories.category import Category
from backend.users.user import User
from backend.districts.district import District
from backend.regions.region import Region
from backend.fooditems.food import FoodItem
from backend.orders.order import Order
from backend.sub_categories.sub_category import subCategory




app = create_app('development')
migrate = Migrate(app,db)


@app.shell_context_processor
def make_shell_context():
   return dict(db=db,Address=Address,User=User,Category=Category,District=District
               ,Region=Region,Order=Order,FoodItem=FoodItem,subCategory=subCategory)