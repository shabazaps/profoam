import runpy
import os

try:
    runpy.run_path(r'C:\Users\shabaza\PycharmProjects\Project\Profoam\tests\test_login.py')
except FileNotFoundError as e:
    print(f"Error: {e}")

try:
    runpy.run_path(r'C:\Users\shabaza\PycharmProjects\Project\Profoam\tests\test_checkout.py')
except FileNotFoundError as e:
    print(f"Error: {e}")
