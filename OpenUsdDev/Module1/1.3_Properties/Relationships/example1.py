from pxr import Usd, UsdGeom, Gf

file_path = "_assets/relationships_ex1.usda"
stage = Usd.Stage.CreateNew(file_path)

world_xform = UsdGeom.Xform.Define(stage, "/World")

# Define a sphere under the World Xform:
sphere = UsdGeom.Sphere.Define(stage, world_xform.GetPath().AppendPath("Sphere"))

# Define a cube under the World Xform and set it to be 5 units away from the sphere:
cube = UsdGeom.Cube.Define(stage, world_xform.GetPath().AppendPath("Cube"))
UsdGeom.XformCommonAPI(cube).SetTranslate(Gf.Vec3d(5, 0, 0))

# Create typeless container for the group
group = stage.DefinePrim("/World/Group")

# Define the relationship
group.CreateRelationship("members", custom=True).SetTargets(
    [sphere.GetPath(), cube.GetPath()]
)

# List relationship targets
members_rel = group.GetRelationship("members")
print("Group members:", [str(p) for p in members_rel.GetTargets()])

stage.Save()