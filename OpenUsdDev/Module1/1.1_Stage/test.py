from pxr import Usd, Sdf, UsdGeom
import os

# Create a new stage:
stage: Usd.Stage = Usd.Stage.CreateNew("_assets/root_layer_example.usda")

# Get the root layer object:
root_layer = stage.GetRootLayer()

# Get relative path of the layer
rel_path = os.path.relpath(root_layer.identifier)


# Add a simple prim so the stage is not empty, both work
stage.DefinePrim("/World", "Xform")
UsdGeom.Xform.Define(stage, "/World")

# Create an additional layer (in a different format) and add it as a sublayer:

new_layer = Sdf.Layer.CreateNew("_assets/extra_layer.usdc")
print(os.path.basename(new_layer.identifier))
new_layer_name = "./" + os.path.basename(new_layer.identifier)

# Add the new layer to the existing stage
root_layer.subLayerPaths.append(new_layer_name)

# Save both layers:
new_layer.Save()
stage.Save()

# Print the contents of the root layer:
print(root_layer.ExportToString())
