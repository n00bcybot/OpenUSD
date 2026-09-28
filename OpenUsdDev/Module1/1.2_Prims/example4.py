from pxr import Usd

file_path = "_assets/prims.usda"
stage = Usd.Stage.Open(file_path)
prim_name = "mesh"

prim_path = stage.GetPrimAtPath("/root/geo/sphere")
child_prim = Usd.Prim.GetChild(prim_path, prim_name)

if child_prim:
    print("Child prim exists")
else:
    print("Child prim DOES NOT exist")