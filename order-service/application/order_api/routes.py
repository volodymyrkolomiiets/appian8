from flask import jsonify, request, make_response
from . import order_api_blueprint
from .. import db
from ..models import Order, OrderItem
from .api.UserClient import UserClient


@order_api_blueprint.route("/api/orders", methods=["GET"])
def orders():
    items = []
    for item in Order.query.all():
        items.append(item.to_json())

    response = jsonify(items)
    return response


@order_api_blueprint.route("/api/order/add-item", methods=["POST"])
def order_add_item():
    # api_key = request.headers.get("Authorization")
    api_key = "$5$rounds=535000$JCaOzj9FuFwZ0CHE$9FFG84nHwBW1GmTCA0xaaYddO.VS4LuKJOLOYCq/nS/"
    response = UserClient.get_user(api_key)
    if not response:
        return make_response(jsonify({"message": "Not logged in"}), 404)
    user = response["result"]
    p_id = int(request.form["product_id"])
    qty = int(request.form['qty'])
    u_id = int(user['id'])

    known_order = Order.query.filter_by(user_id=u_id, is_open=True).first()

    if known_order is None:
        known_order = Order()
        known_order.is_open = True
        known_order.user_id = u_id

        order_item = OrderItem(p_id, qty)
        known_order.items.append(order_item)
    else:
        found = False
        for item in known_order.items:
            if item.product_id == p_id:
                found = True
                item.quantity += qty
        if found is False:
            order_item = OrderItem(p_id, qty)
            known_order.items.append(order_item)
    db.session.add(known_order)
    db.session.commit()
    response = jsonify({"result": known_order.to_json()})
    return response