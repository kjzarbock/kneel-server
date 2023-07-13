import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from views import get_all_metals, get_all_orders, get_all_sizes, get_all_styles, get_single_metal, get_single_order, get_single_size, get_single_style, create_order, delete_order, update_order


class HandleRequests(BaseHTTPRequestHandler):
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """

    # Here's a class function
    def parse_url(self, path):
        """Parses a request path and determines which resource (the first element of the path)"""
        # Just like splitting a string in JavaScript. If the
        # path is "/animals/1", the resulting list will
        # have "" at index 0, "animals" at index 1, and "1"
        # at index 2.
        path_params = path.split("/")
        resource = path_params[1]
        id = None

        # Try to get the item at index 2
        try:
            # Convert the string "1" to the integer 1
            # This is the new parseInt()
            id = int(path_params[2])
        except IndexError:
            pass  # No route parameter exists: /animals
        except ValueError:
            pass  # Request had trailing slash: /animals/

        return (resource, id)  # This is a tuple
    # Here's a method on the class that overrides the parent's method.
    # It handles any GET request.

    def do_GET(self):
        """Handles GET requests to the server"""
        self._set_headers(200)
        response = {}  # Default response
    # Parse the URL and capture the tuple that is returned
        (resource, id) = self.parse_url(self.path)

        if resource == "metals":
            if id is not None:
                metal = get_single_metal(id)
                if metal is not None:
                    response = f"{metal}"
                else:
                    self._set_headers(404)
                    response = "That metal is not currently in stock for jewelry."
            else:
                response = f"{get_all_metals()}"
            self.wfile.write(json.dumps(response).encode())

        if resource == "orders":
            if id is not None:
                order = get_single_order(id)
                if order is not None:
                    response = f"{order}"
                else:
                    self._set_headers(404)
                    response = "That order was never placed, or was cancelled."
            else:
                response = f"{get_all_orders()}"
            self.wfile.write(json.dumps(response).encode())

        if resource == "sizes":
            if id is not None:
                size = get_single_size(id)
                if size is not None:
                    response = f"{size}"
                else:
                    self._set_headers(404)
                    response = "That size is not currently in stock for jewelry."
            else:
                response = f"{get_all_sizes()}"
            self.wfile.write(json.dumps(response).encode())

        if resource == "styles":
            if id is not None:
                style = get_single_style(id)
                if style is not None:
                    response = f"{style}"
                else:
                    self._set_headers(404)
                    response = "That style is not currently in stock for jewelry."
            else:
                response = f"{get_all_styles()}"
            self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        """Handles POST requests to the server"""
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        # Convert JSON string to a Python dictionary
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Initialize new animal
        created_order = None

        # Add a new animal to the list. Don't worry about
        # the orange squiggle, you'll define the create_animal
        # function next.
        if resource == "orders":
            if "metalId" in post_body and "sizeId" in post_body and "styleId" in post_body:
                self._set_headers(201)
                created_order = create_order(post_body)
            else:
                self._set_headers(400)
                created_order = {
                    "message": f'{"Metal is required" if "metalId" not in post_body else ""} {"Size is required" if "sizeId" not in post_body else ""} {"Style is required" if "styleId" not in post_body else ""}'}

        self.wfile.write(json.dumps(created_order).encode())

    def do_DELETE(self):
        """Handles DELETE requests to the server"""
    # Set a 204 response code
        self._set_headers(405)

    # Parse the URL
        (resource, id) = self.parse_url(self.path)

    # Delete a single order from the list
        if resource == "orders":
            response = {
                "message": "Deleting orders is not allowed."
            }
            self.wfile.write(json.dumps(response).encode())
        elif resource == "customers":
            self._set_headers(405)
            response = {
                "message": "Deleting customers is not allowed."
            }
            self.wfile.write(json.dumps(response).encode())

    # A method that handles any PUT request.

    def do_PUT(self):
        self._set_headers(204)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

    # Parse the URL
        (resource, id) = self.parse_url(self.path)

    # Delete a single animal from the list
        if resource == "orders":
            update_order(id, post_body)
    # Encode the new animal and send in response
        self.wfile.write("".encode())

    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """Sets the options headers"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                         'X-Requested-With, Content-Type, Accept')
        self.end_headers()


# point of this application.
def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
