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
    return ORDERS

def get_single_order(id):
    # Variable to hold the found metal, if it exists
    requested_order = None

    # Iterate the METALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for order in ORDERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if order["id"] == id:
            requested_order = order

    return requested_order

def create_order(order):
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