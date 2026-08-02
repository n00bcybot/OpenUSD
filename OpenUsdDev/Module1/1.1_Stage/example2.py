from pxr import Usd

extension = ".usda"
file_name = "first_stage"
_dir = "_assets/"

# Define a file path name:
file_path = _dir + file_name + extension

# Open an existing USD stage from disk
stage = Usd.Stage.Open(file_path)

# Create prim in this stage
stage.DefinePrim("/World", "Xform")

# Save stage
stage.Save()

# Print the stage as text, so we can inspect the result:
print(stage.ExportToString(addSourceFileComment=False))

