from pxr import Usd

file_path = "_assets/prims.usda"
stage = Usd.Stage.Open(file_path)

prim = stage.GetPrimAtPath("/root/geo/sphere")
child_prim: Usd.Prim = Usd.Prim.GetChild(prim, "mesh")
if child_prim:
    print("Child prim exists")
else:
    print("Child prim DOES NOT exist")