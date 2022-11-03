from datetime import datetime
from . import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    slug = db.Column(db.String(255), unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(255), unique=False, nullable=True)
    data_added = db.Column(db.DateTime, default=datetime.utcnow)
    data_updated = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def to_json(self):
        return {
            "id": self.id,
            "name":self.name,
            "slug": self.slug,
            "price": self.price,
            "image": self.image,

        }