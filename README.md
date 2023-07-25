**Project Description: ShowShotManager - Organizing Entertainment Data in Animal Kingdom**

The ShowShotManager is a Python library designed to organize and manage data related to shows, shots, and assets within the Animal Kingdom entertainment project. The primary goal of this library is to provide an efficient way for developers and project managers to handle the complex data hierarchy associated with entertainment projects, making it easier to create, update, and archive show content.

The library is divided into three main classes:

1. `ShowManager`: Manages show-related data, including creating subdirectories for individual shows, adding and updating description files for shows, and archiving shows into ZIP files for easy storage and sharing.

2. `ShotManager`: Handles shot-related data, such as creating character information files, reading and updating JSON files, and managing assets linked to specific shots.

3. `AssetManager`: Takes care of asset-related data, allowing users to create folders for different types of assets, add and update description files for assets, and link assets to shots.

The library aims to provide an easy-to-use and comprehensive API, enabling developers and content creators to efficiently organize and access the vast amount of data associated with a complex entertainment project like Animal Kingdom.

NOTE: `ShowShotManager.py` is the main python file containing all the class libraries. `Shows.Shots.Assets_Manager_V2.py` is the file containing the Usage examples which you can run to perform your tests.

**Running Examples:**

To run the code examples provided in the documentation, you will need to have Python installed on your system. The examples are written in Python 3.x, so make sure you have a compatible version.

1. Save the provided code examples into separate Python files, or copy them into a single Python script.
2. Make sure the `ShowShotManager.py` file is in the same directory as your Python script or add the path to the file in the Python script.
3. Install any required dependencies specified in the code examples, such as the `typing` module.
4. Execute the Python script to see the output of each example.

Please ensure that the paths specified in the examples exist and are writable. For example, replace `"D:/BCIT/Term 3/Data Structures/Assignment 2"` with a valid directory path on your system.

**Example Usage:**

Below are some example usage scenarios demonstrating the functionality of the ShowShotManager API:

**1. Managing Shows:**

```python
# ShowManager example
from typing import Dict
from ShowShotManager import ShowManager

# Create ShowManager instance
show_manager = ShowManager("D:/BCIT/Term 3/Data Structures/Assignment 2", "Animal_Kingdom")

# Create subdirectories for shows
show_manager.create_subdirectories(["Dogs", "Cats", "Birds", "Bunnys"])

# Get existing subdirectories
subdirectories_list = show_manager.get_subdirectories()
print(subdirectories_list)

# Add description to a show
subdir_name = "Dogs"
description = {
    "Description": "This show is about a family of Dogs in the Animal Kingdom",
}
show_manager.create_json_file(subdir_name, "description.json", description)

# Get description of a show
description = show_manager.get_description_file(subdir_name)
if description is not None:
    print(description)

# Update description of a show
show_manager.update_description_file("Cats", {"Description": "This show is a Comedy series about Cats in the Animal Kingdom"})

# Delete a show
show_manager.delete_subdirectory("Dogs")

# Archive a show
zip_file_name_to_create = "Birds.zip"
directory_path = "D:/BCIT/Term 3/Data Structures/Assignment 2/Animal_Kingdom"
show_manager = ShowManager(directory_path, "Birds")
show_manager.zip_show(zip_file_name_to_create)
```

**2. Managing Shots and Assets:**

```python
# ShotManager example
from typing import Dict
from ShowShotManager import ShotManager

# Create ShotManager instance
shot_manager = ShotManager("D:/BCIT/Term 3/Data Structures/Assignment 2/Animal_Kingdom/Birds")

# Create character information for a shot
character_name = "Doggo"
character_info = {
    "age": 5,
    "breed": "Golden Retriever",
    "assets": ["Prop_collar", "SuperPower_toy_bone", "Environment_Cat_house"],
}
shot_manager.create_character_info("Bird1_info", character_name, character_info)

# Get list of JSON files in the shot directory
shot_manager.get_json_files()

# Get information from a JSON file
print(shot_manager.get_json_file_info("doggo1_info.json"))

# Edit information in a JSON file
shot_manager.edit_json_file("doggo1_info.json", {"name": "Charlie", "age": 4, "breed": "Golden Retriever", "assets": ["collar_Props", "toy_bone_Props", "Cat_house_Environmentsdwa"]})

# Delete a JSON file
shot_manager.delete_json_file("doggo1_info.json")

# Find assets by shot
shot_manager = ShotManager("D:/BCIT/Term 3/Data Structures/Assignment 2/Animal_Kingdom/Dogs")
file_name = "doggo1_info.json"
shot_manager.print_assets_key_values(file_name)
```

```python
# AssetManager example
from typing import Dict, List
from ShowShotManager import AssetManager

# Create AssetManager instance
assets_manager = AssetManager("D:/BCIT/Term 3/Data Structures/Assignment 2/Animal_Kingdom")

# Create folders for different asset types
folder_names = ["Dogs/Prop", "Dogs/Environment", "Dogs/SuperPowers"]
assets_manager.create_folders(folder_names)

# Add description file to an asset folder
folder_name = "Dogs/Props"
description_data = {
    "description": "This contains a list of environments to be used by certain characters",
}
assets_manager.add_description_file(folder_name, description_data)

# Read a list of all created asset folders
folder_name = "Dogs"
asset_folders = assets_manager.read_asset_folders(folder_name)
print(asset_folders)

# Read information from a description file
folder_name = "Dogs/Prop"
assets_manager.print_description_file(folder_name)

# Update data in a description file
folder_name = "Dogs/SuperPowers"
updated_data = {
    "description": "This contains a list of SuperPowers to be used by certain characters",
}
assets_manager.update_description_file(folder_name, updated_data)

# Delete an asset folder
folder_name = "Dogs/SuperPowers"
assets_manager.delete_asset_folder(folder_name)

# Create actual item/scene files for the assets and link them to shots
folder_name = "Dogs/Prop"
desired_file_name = "Staff1.json"
custom_description_data = {
    "name": "Custom Asset2",
    "additional_info": "This is a custom asset with user-defined data.",
    "Shots": ["character3", "character5", "character7"],
}
assets_manager.create_json_file(folder_name, custom_description_data, desired_file_name)

# Update the shots linked to an asset
folder_name = "Dogs/Prop"
file_name = "Staff2.json"
new_shots_data = ["character2", "character6", "character9"]
assets_manager.update_shots_key(folder_name, file_name, new_shots_data)

# Find assets by category
folder_name = "Dogs/Prop"
json_files_list = assets_manager.list_json_files(folder_name)
print("

JSON files in the chosen asset folder:")
print(json_files_list)

# Read "Shots" key values from a specific JSON file in a specific folder
folder_name = "Dogs/Prop"
file_name = "Staff2.json"
shots_key_values = assets_manager.get_shots_key_values(folder_name, file_name)
print(shots_key_values)

# Archive an asset
folder_names_to_zip = ["Dogs/Prop", "Dogs/Environment", "Dogs/SuperPowers"]
assets_manager.zip_asset_folders(folder_names_to_zip)

# Load archived asset
zip_file_directory_to_read = "D:/BCIT/Term 3/Data Structures/Assignment 2/Animal_Kingdom/Dogs"
zip_file_name_to_read = "Prop.zip"
assets_manager.read_data_from_zip(zip_file_name_to_read, zip_file_directory_to_read)
```

Please make sure to adjust the file paths and folder names according to your specific project structure and requirements.