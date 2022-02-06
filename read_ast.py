import ast
with open("test.py", "r") as source:
    tree = ast.parse(source.read())
    print(tree)
    print(ast.dump(tree))  
