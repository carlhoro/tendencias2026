# app/models/item_pedido.py

from app.extensions import db

class ItemPedido(db.Model):
    __tablename__ = 'items_pedido'

    id = db.Column(db.Integer, primary_key=True)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedidos.id'), nullable=False)

    producto = db.Column(db.String(100), nullable=False)
    cantidad = db.Column(db.Integer, default=1)
    precio_base = db.Column(db.Float, nullable=False)
    extras = db.Column(db.JSON, default=[])
    precio_final = db.Column(db.Float)

    # -------------------------
    # Builder práctico
    # -------------------------
    @classmethod
    def construir(cls, producto, precio_base):
        return ItemBuilder(cls, producto, precio_base)


class ItemBuilder:
    def __init__(self, model_cls, producto, precio_base):
        self.model_cls = model_cls
        self.producto = producto
        self.precio_base = precio_base
        self.cantidad = 1
        self.extras = []

    def con_cantidad(self, cantidad):
        self.cantidad = cantidad
        return self

    def agregar_extra(self, nombre, precio):
        self.extras.append({"nombre": nombre, "precio": precio})
        return self

    def build(self):
        total_extras = sum(e["precio"] for e in self.extras)
        precio_final = (self.precio_base + total_extras) * self.cantidad

        return self.model_cls(
            producto=self.producto,
            cantidad=self.cantidad,
            precio_base=self.precio_base,
            extras=self.extras,
            precio_final=precio_final
        )