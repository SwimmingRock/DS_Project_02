from typing import Dict
from ShowShotManager import ShowManager, ShotManager, AssetManager

# ==================================================================================== BEGIN EXAMPLE USAGE SHOWS ====================================================================================


show_manager = ShowManager("D:/BCIT/Term 3/Data Structures/Assignment 2", "Animal_Kingdom")
show_manager.create_subdirectories(["Dogs", "Cats", "Birds", "Bunnys"])

subdirectories_list = show_manager.get_subdirectories()
print(subdirectories_list)

subdir_name = "Dogs"
description = {
    "Description": "This show is about a family of Dogs in the Animal Kingdom",
}
show_manager.create_json_file(subdir_name, "description.json", description)

description = show_manager.get_description_file(subdir_name)
if description is not None:
    print(description)

#show_manager.update_description_file("Dogs", {"Description": "This show is a Comedy series about Cats in the Animal Kingdom"})
#show_manager.delete_subdirectory("Dogs")


# Archive a show
#zip_file_name_to_create = "Dogs.zip"  # Replace with the desired ZIP file name
#directory_path = "D:/BCIT/Term 3/Data Structures/Assignment 2/Animal_Kingdom"  # Replace with the path to the Animal Kingdom directory
#show_manager = ShowManager(directory_path, "Dogs")  # Replace "Dog" with the desired show directory name
#show_manager.zip_show(zip_file_name_to_create)


# Load archived shots and assets
#zip_file_name_to_read = "Dogs.zip"  # Replace 'Dogs.zip' with the name of the ZIP file you want to read
#show_manager.read_data_from_zip(zip_file_name_to_read)


# ==================================================================================== END EXAMPLE USAGE SHOWS ====================================================================================

# ==================================================================================== BEGIN EXAMPLE USAGE SHOTS ====================================================================================

shot_manager = ShotManager("D:/BCIT/Term 3/Data Structures/Assignment 2/Animal_Kingdom/Dogs")


character_name = "Doggo"
character_info = {
    "age": 5,
    "breed": "Golden Retriever",
    "assets": ["Prop_collar", "SuperPower_toy_bone", "Environment_Cat_house"],
}
shot_manager.create_character_info("doggo1_info", character_name, character_info)

shot_manager.get_json_files()

print(shot_manager.get_json_file_info("doggo1_info.json"))

#shot_manager.edit_json_file("doggo1_info.json", {"name": "Charlie", "age": 4, "breed": "Golden Retriever", "assets": ["collar_Props", "toy_bone_Props", "Cat_house_Environmentsdwa"]})

#shot_manager.delete_json_file("doggo1_info.json")

#Find assets by shot
shot_manager = ShotManager("D:/BCIT/Term 3/Data Structures/Assignment 2/Animal_Kingdom/Dogs")
file_name = "doggo1_info.json"  # Choose the JSON file you want to print the assets from
shot_manager.print_assets_key_values(file_name)
# ==================================================================================== END EXAMPLE USAGE SHOTS ====================================================================================

# ==================================================================================== BEGIN EXAMPLE USAGE ASSETS ====================================================================================
# Create new assets
assets_manager = AssetManager("D:/BCIT/Term 3/Data Structures/Assignment 2/Animal_Kingdom")
folder_names = ["Dogs/Prop", "Dogs/Environment", "Dogs/SuperPowers"]
assets_manager.create_folders(folder_names)


# Add a description file to the assets
folder_name = "Dogs/Prop"  # Choose the folder where you want to add the description file
description_data = {
    "description": "This contains a list of environments to be used by certain characters",
}
assets_manager.add_description_file(folder_name, description_data)


# Read a list of all created assets
folder_name = "Dogs"  # Choose the folder from which you want to read the asset folders
asset_folders = assets_manager.read_asset_folders(folder_name)
print(asset_folders)


# Read information for a single asset
folder_name = "Dogs/Prop"  # Choose the folder from which you want to print the description file
assets_manager.print_description_file(folder_name)


# Update the data for an asset
folder_name = "Dogs/Prop"  # Choose the folder in which you want to update the description file
updated_data = {
    "description": "This contains a list of SuperPowers to be used by certain characters",
}
assets_manager.update_description_file(folder_name, updated_data)


# Delete an asset
#folder_name = "Dogs/SuperPowers"  # Choose the folder that you want to delete
#assets_manager.delete_asset_folder(folder_name)


# Create actual item/scene files for the assets   AND Add an asset to a shot
folder_name = "Dogs/Prop"  # Choose the folder in which you want to create a new JSON file
# Choose the desired file name for the new JSON file
desired_file_name = "Staff1.json"

custom_description_data = {
    "name": "Custom Asset2",
    "additional_info": "This is a custom asset with user-defined data.",
    "Shots": ["character3", "character5", "character7"],  # Add multiple values as a list
}

assets_manager.create_json_file(folder_name, custom_description_data, desired_file_name)


# Update the data for the shots linked to an asset
folder_name = "Dogs/Prop"  # Choose the folder in which you want to update the Shots key
file_name = "Staff1.json"  # Choose the JSON file you want to update
new_shots_data = ["character2", "character6", "character9"]  # New shots data

assets_manager.update_shots_key(folder_name, file_name, new_shots_data)


# Find assets by category
folder_name = "Dogs/Prop"  # Choose the folder from which you want to list JSON files
json_files_list = assets_manager.list_json_files(folder_name)
print("JSON files in the chosen asset folder:")
print(json_files_list)


# Read "Shots" key values from a specific JSON file in a specific folder
folder_name = "Dogs/Prop"
file_name = "Staff2.json"
shots_key_values = assets_manager.get_shots_key_values(folder_name, file_name)
print(shots_key_values)


# Archive an asset
#folder_names_to_zip = ["Dogs/Prop", "Dogs/Environment", "Dogs/SuperPowers"]
#assets_manager.zip_asset_folders(folder_names_to_zip)


# Load archived asset
#zip_file_directory_to_read = "D:/BCIT/Term 3/Data Structures/Assignment 2/Animal_Kingdom/Dogs"  # Replace with the path to the ZIP file's directory
#zip_file_name_to_read = "Prop.zip"  # Replace 'Dogs.zip' with the name of the ZIP file you want to read
#assets_manager.read_data_from_zip(zip_file_name_to_read, zip_file_directory_to_read)

# ==================================================================================== END EXAMPLE USAGE ASSETS ====================================================================================

