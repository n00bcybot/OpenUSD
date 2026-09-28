from pxr import Usd

# Create a new stage stored only in memory:
stage = Usd.Stage.CreateInMemory()


# Add a prim so the stage contains some data:
stage.DefinePrim("/World", "Xform")

# Print the stage's contents:
print("In-memory stage:")
print(stage.ExportToString(addSourceFileComment=False))

# Write the stage to disk if needed:
stage.Export("_assets/in_memory_stage.usda")