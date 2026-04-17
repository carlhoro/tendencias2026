# app/services/pedido_service.py

from app.extensions import db
from app.domain.models.Pedido import Pedido
from app.domain.models.ItemPedido import ItemPedido

def crear_pedido(data):
    pedido = Pedido(cliente_nombre=data["cliente"])

    total = 0

    for item in data["items"]:
        builder = ItemPedido.construir(
            item["producto"],
            item["precio_base"]
        )

        builder.con_cantidad(item.get("cantidad", 1))

        for extra in item.get("extras", []):
            builder.agregar_extra(extra["nombre"], extra["precio"])

        item_obj = builder.build()
        pedido.items.append(item_obj)

        total += item_obj.precio_final

    pedido.total = total

    db.session.add(pedido)
    db.session.commit()

    return pedido