import os
import backend_file_explorer
from backend_file_explorer import InputsMethod as IM
import backend_file_explorer as b

print(backend_file_explorer.files_list("c:")[12])

print( f"C:/{backend_file_explorer.files_list('c:')[12]}")