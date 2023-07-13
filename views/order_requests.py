from .metal_requests import get_single_metal
from .size_requests import get_single_size
from .style_requests import get_single_style
ORDERS = [
    {
        "metalId": 4,
        "sizeId": 3,
        "styleId": 2,
        "id": 1
    },
    {
        "metalId": 5,
        "sizeId": 5,
        "styleId": 3,
        "id": 2
    },
    {
        "metalId": 5,
        "sizeId": 3,
        "styleId": 2,
        "id": 3
    },
    {
        "metalId": 4,
        "sizeId": 3,
        "styleId": 3,
        "id": 4
    },
    {
        "metalId": 4,
        "sizeId": 3,
        "styleId": 1,
        "id": 5
    },
    {
        "metalId": 3,
        "sizeId": 4,
        "styleId": 2,
        "id": 6
    },
    {
        "metalId": 2,
        "sizeId": 3,
        "styleId": 3,
        "id": 7
    },
    {
        "metalId": 3,
        "sizeId": 4,
        "styleId": 1,
        "id": 8
    }
]


def get_all_orders():
    """getting all orders"""
    return ORDERS

def get_single_order(id):
    """getting a single order"""
    # Variable to hold the found metal, if it exists
    requested_order = None

    # Iterate the METALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for order in ORDERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if order["id"] == id:
            requested_order = order
            metal = get_single_metal(requested_order["id"])
            size = get_single_size(requested_order["id"])
            style = get_single_style(requested_order["id"])

            requested_order["metal"] = metal
            requested_order["size"] = size
            requested_order["style"] = style
            requested_order.pop("metalId", None)
            requested_order.pop("sizeId", None)
            requested_order.pop("styleId", None)


    return requested_order

def create_order(order):
    """creating an order"""
    # Get the id value of the last animal in the list
    max_id = ORDERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    order["id"] = new_id

    # Add the animal dictionary to the list
    ORDERS.append(order)

    # Return the dictionary with `id` property added
    return order

def delete_order(id):
    # Initial -1 value for animal index, in case one isn't found
    order_index = -1

    # Iterate the ORDERS list, but use enumerate() so that you
    # can access the index value of each item
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            # Found the order. Store the current index.
            order_index = index

    # If the order was found, use pop(int) to remove it from list
    if order_index >= 0:
        ORDERS.pop(order_index)

def update_order(id, new_order):
    # Iterate the ORDERS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            # Found the order. Update the value.
            ORDERS[index] = new_order
            break