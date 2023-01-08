import ctypes

lib = ctypes.CDLL('./libPython.so')
lib.print_python_string.argtypes = [ctypes.py_object]
s = "The spoon does not exist"
lib.print_python_string(s)
s = "ложка не сущест�
lib.print_python_string(s)
s = "La cuillère n'existe pas
lib.print_python_string(s)
s = "勺孨"
lib.print_python_string(s)
s = "숟가락은 존재하지 않는�"
lib.print_python_string(s)
s = "スプーンは存在しない
lib.print_python_string(s)
s = b"The spoon does not exist"
lib.print_python_string(s)
