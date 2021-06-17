import math
def packing_code(objects, space):
    packed = math.ceil(objects / space)
    return packed
num_objects = int(input("How many items are being manufactured? "))
objects_packed = int(input("How many items are packed per box? "))

print(f"for {num_objects} items, packing {objects_packed} items in each box, you will need {packing_code(num_objects, objects_packed)} boxes.")
