# app/models/pedido.py

from app.extensions import db

class Pedido(db.Model):
    __tablename__ = 'pedidos'

    id = db.Column(db.Integer, primary_key=True)
    cliente_nombre = db.Column(db.String(100), nullable=False)
    total = db.Column(db.Float, default=0)

    items = db.relationship('ItemPedido', backref='pedido', lazy=True)