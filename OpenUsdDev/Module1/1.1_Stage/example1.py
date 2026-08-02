from pxr import Usd

extension = ".usda"
file_name = "first_stage"
_dir = "_assets/"

# Define a file path name:
file_path = _dir + file_name + extension
# Create a stage at the given `file_path`:
stage = Usd.Stage.CreateNew(file_path)
print(stage.ExportToString(addSourceFileComment=False))
