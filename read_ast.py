import ast
import requests

code = requests.get('https://raw.githubusercontent.com/potofpie/super-spork/main/test.py').text
tree = ast.parse(code)
ast.dump(tree)
obj = compile(tree, filename="<ast>", mode="exec")
exec(obj)
