print("operator.py: ", __name__) # this will run first.

from ..mylib import * # this accesses the parent folder.
# this reuses the import that's already on sys.modules.