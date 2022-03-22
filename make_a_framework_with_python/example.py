"""
Simple example
"""

from custom_py_web_framework.app import App
from custom_py_web_framework.router import Path
from custom_py_web_framework.response import HttpResponse, RenderResponse, JsonResponse
from wsgiref.simple_server import make_server

app = App()
app.set_static('/static/', '.')


def print_received(request):
    print(request.query_string)
    return RenderResponse(request, 'home.html',None)


def json_point(request):
    data = [{'hello': 'hi', 'there': 'me'},
            {'name': 'John', 'age': 15},
            {'name': 'Ama', 'age': 18},
            {'name': 'Someone', 'age': 20},

            ]
    return JsonResponse(request, data)


# def form(request):
#     if request.method == "POST":
#         age = request.post.get('age')
#         return MemoryFileResponse(request, age.file)
#     return HttpResponse(request, """
#     <html>
#     <body>
#     <form method="post" action="", enctype="multipart/form-data">
#     <input type="file" id="age" name="age" value="age">
#     <input type="submit" value="submit">
#     </form>
#     </body>
#     </html>
#     """)


routes = [
    Path('/', print_received),
    Path('/json/', json_point),
    # Path('/form/', form),
]

app.set_routes(routes)

if __name__ == '__main__':
    host = "127.0.0.1"
    port = 8000
    server = make_server(host, port, app)
    print(f"Developement Server at http://{host}:{port}")
    server.serve_forever()
