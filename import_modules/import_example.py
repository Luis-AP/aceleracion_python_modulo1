import sys
import os

abs_path = os.path.abspath(__file__)
parent_dir = os.path.dirname(os.path.dirname(abs_path))

sys.path.append(parent_dir)  # Agrega el directorio padre al sys.path

from functions.average_args import average

print(average(1, 2, 3, 4, 5))
