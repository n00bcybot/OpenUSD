# Import the `Usd` module from the `pxr` package:
from pxr import Usd, UsdGeom

# Create a new USD stage with root layer named "prims.usda":
stage: Usd.Stage = Usd.Stage.CreateNew("_assets/prims.usda")

# Define a new primitive at the path "/hello" on the current stage:
stage.DefinePrim("/root", "Xform")
stage.DefinePrim("/root/geo", "Scope")

# Define a new primitive at the path "/world" on the current stage with the prim type, Sphere.
stage.DefinePrim("/root/geo/sphere", "Xform")
# stage.DefinePrim("/root/geo/sphere/sphere_mesh", "Sphere")

sphere = UsdGeom.Sphere.Define(stage, "/root/geo/sphere/mesh")
# sphere.CreateRadiusAttr().Set(2)

stage.Save()
