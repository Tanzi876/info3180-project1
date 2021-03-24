from . import db


class RealEstate(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'realestate'

    pid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80),unique=True)
    bedroom= db.Column(db.String(80))
    bathroom=db.Column(db.String(80))
    location=db.Column(db.String(80))
    price=db.Column(db.String(80))
    types=db.Column(db.String(80))
    descrp=db.Column(db.String(80))
    photo=db.Column(db.String(80))
    
    def __init__(self,title,bedroom,bathroom,location,price,types,descrp,photo):
        self.title=title
        self.bedroom=bedroom
        self.bathroom=bathroom
        self.location=location
        self.price=price
        self.types=types
        self.descrp=descrp
        self.photo=photo
        
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<RealEstate %r>' % (self.title)
