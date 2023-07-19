import sqlite3
import json
from models import Order
from models import Metal
from models import Size
from models import Style


"""defining orders"""
ORDERS = [
    {
        "metal_id": 4,
        "size_id": 3,
        "style_id": 2,
        "id": 1
    },
    {
        "metal_id": 5,
        "size_id": 5,
        "style_id": 3,
        "id": 2
    },
    {
        "metal_id": 5,
        "size_id": 3,
        "style_id": 2,
        "id": 3
    },
    {
        "metal_id": 4,
        "size_id": 3,
        "style_id": 3,
        "id": 4
    },
    {
        "metal_id": 4,
        "size_id": 3,
        "style_id": 1,
        "id": 5
    },
    {
        "metal_id": 3,
        "size_id": 4,
        "style_id": 2,
        "id": 6
    },
    {
        "metal_id": 2,
        "size_id": 3,
        "style_id": 3,
        "id": 7
    },
    {
        "metal_id": 3,
        "size_id": 4,
        "style_id": 1,
        "id": 8
    }
]

def get_all_orders():
    # Open a connection to the database
    with sqlite3.connect("./kneel.sqlite3") as conn:
        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            o.id,
            o.metal_id,
            o.size_id,
            o.style_id,
            m.metal metal,
            s.carets carets,
            st.style style,
            m.price metal_price,
            s.price size_price,
            st.price style_price
        FROM orders o
        JOIN metals m ON m.id = o.metal_id
        JOIN sizes s ON s.id = o.size_id
        JOIN styles st ON st.id = o.style_id
        """)

        # Initialize an empty list to hold all order representations
        orders = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from the database
        for row in dataset:
            # Create an order instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Order class above.
            order = Order(
                row['id'],
                row['metal_id'],
                row['size_id'],
                row['style_id']
            )

            # Create Metal, Size, and Style instances and assign them to the order
            metal = Metal(row['metal_id'], row['metal'], row['metal_price'])
            size = Size(row['size_id'], row['carets'], row['size_price'])
            style = Style(row['style_id'], row['style'], row['style_price'])

            order.metal = metal.__dict__
            order.size = size.__dict__
            order.style = style.__dict__

            orders.append(order.__dict__)

    return orders


def get_single_order(id):
    # Variable to hold the found metal, if it exists
    """getting a single order"""
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