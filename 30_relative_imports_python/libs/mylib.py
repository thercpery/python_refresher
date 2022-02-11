from .operations import operators # this will run first.
# This is an absolute import that you have to define the path that you are importing from.

# A relative import is one can import the current folder that the file is in, but it cannot import unless there is a folder name in the path in the module path.

print("mylib.py",__name__)