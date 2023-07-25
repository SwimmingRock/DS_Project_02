import os
import json
import shutil
import zipfile
from typing import List, Dict

# ==================================================================================== BEGIN SHOWS ====================================================================================

class ShowManager:
    def __init__(self, directory_path: str, directory_name: str):
        """
        Initialize the ShowManager with the directory path and name.

        Args:
            directory_path (str): The base directory path.
            directory_name (str): The name of the show directory.
        """
        self.directory_path = directory_path
        self.directory_name = directory_name

    def create_directory(self, directory_path: str, directory_name: str) -> None:
        """
        Create a new directory.

        Args:
            directory_path (str): The base directory path.
            directory_name (str): The name of the new directory.
        """
        directory = os.path.join(directory_path, directory_name)
        if os.path.exists(directory):
            print(f"Directory '{directory}' already exists.")
        else:
            os.makedirs(directory)
            print(f"Directory '{directory}' created successfully!")

    def create_subdirectories(self, subdirectories: List[str]) -> None:
        """
        Create subdirectories within the main show directory.

        Args:
            subdirectories (List[str]): A list of subdirectory names to create.
        """
        main_directory_path = os.path.join(self.directory_path, self.directory_name)
        self.create_directory(self.directory_path, self.directory_name)

        for subdirectory in subdirectories:
            subdirectory_path = os.path.join(main_directory_path, subdirectory)
            self.create_directory(main_directory_path, subdirectory)

    def get_subdirectories(self) -> List[str]:
        """
        Get a list of subdirectory names within the main show directory.

        Returns:
            List[str]: A list of subdirectory names.
        """
        subdirectories = []
        for entry in os.scandir(os.path.join(self.directory_path, self.directory_name)):
            if entry.is_dir():
                subdirectories.append(entry.name)
        return subdirectories

    def create_json_file(self, subdir_name: str, filename: str, data: Dict) -> None:
        """
        Create a JSON file in the specified subdirectory.

        Args:
            subdir_name (str): The name of the subdirectory.
            filename (str): The name of the JSON file.
            data (Dict): The data to be written to the JSON file.
        """
        subdir_path = os.path.join(self.directory_path, self.directory_name, subdir_name)
        file_path = os.path.join(subdir_path, filename)
        with open(file_path, 'w', encoding='utf-8') as file:  # Specify 'utf-8' encoding
            json.dump(data, file, indent=4)
        print(f"JSON file '{filename}' created successfully!")

    def get_description_file(self, subdir_name: str) -> Dict:
        """
        Get the contents of the description file in the specified subdirectory.

        Args:
            subdir_name (str): The name of the subdirectory.

        Returns:
            Dict: The contents of the description file as a dictionary, or None if the file does not exist.
        """
        subdir_path = os.path.join(self.directory_path, self.directory_name, subdir_name)
        description_file = os.path.join(subdir_path, "description.json")

        if os.path.exists(description_file):
            with open(description_file, 'r') as file:
                description = json.load(file)
            return description
        else:
            print(f"Description file does not exist in '{subdir_name}' subdirectory.")
            return None

    def update_description_file(self, subdir_name: str, description: Dict) -> None:
        """
        Update the contents of the description file in the specified subdirectory.

        Args:
            subdir_name (str): The name of the subdirectory.
            description (Dict): The updated description data to be written to the file.
        """
        subdir_path = os.path.join(self.directory_path, self.directory_name, subdir_name)
        description_file = os.path.join(subdir_path, "description.json")

        if os.path.exists(description_file):
            with open(description_file, 'w') as file:
                json.dump(description, file, indent=4)
            print(f"Description file in '{subdir_name}' subdirectory updated successfully!")
        else:
            print(f"Description file does not exist in '{subdir_name}' subdirectory.")

    def delete_subdirectory(self, subdirectory_name: str) -> None:
        """
        Delete a subdirectory and its contents.

        Args:
            subdirectory_name (str): The name of the subdirectory to be deleted.
        """
        subdirectory_path = os.path.join(self.directory_path, self.directory_name, subdirectory_name)

        if os.path.exists(subdirectory_path):
            shutil.rmtree(subdirectory_path)
            print(f"Subdirectory '{subdirectory_name}' and its contents have been deleted successfully!")
        else:
            print(f"Subdirectory '{subdirectory_name}' does not exist.")

    def zip_show(self, zip_file_name: str) -> None:
        """
        Zip the entire show directory.

        Args:
            zip_file_name (str): The name of the zip file to be created.
        """
        main_directory_path = os.path.join(self.directory_path, self.directory_name)
        zip_file_path = os.path.join(self.directory_path, zip_file_name)

        with zipfile.ZipFile(zip_file_path, 'w') as zip_file:
            for root, _, files in os.walk(main_directory_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, main_directory_path)
                    zip_file.write(file_path, arcname)

        print(f"Show '{self.directory_name}' has been zipped to '{zip_file_name}'.")

    def read_data_from_zip(self, zip_file_name: str) -> None:
        """
        Read and display the contents of a ZIP file.

        Args:
            zip_file_name (str): The name of the ZIP file to be read.
        """
        zip_file_path = os.path.join(self.directory_path, zip_file_name)

        if not os.path.exists(zip_file_path):
            print(f"ZIP file '{zip_file_name}' does not exist in the specified directory.")
            return

        with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
            print(f"Contents of ZIP file '{zip_file_name}':")

            for file_name in zip_file.namelist():
                with zip_file.open(file_name) as file:
                    try:
                        data = file.read().decode('utf-8', errors='replace')
                        print(f"\nFile: {file_name}\nData:\n{data}")
                    except UnicodeDecodeError:
                        print(f"\nFile: {file_name}\nData: Unable to decode data (binary file).")

# ==================================================================================== END SHOWS ====================================================================================


# ==================================================================================== BEGIN SHOTS ====================================================================================

class ShotManager:
    def __init__(self, directory_path: str):
        """
        Initialize the ShotManager with the directory path.

        Args:
            directory_path (str): The base directory path.
        """
        self.directory_path = directory_path

    def create_character_info(self, file_name: str, character_name: str, info: Dict) -> None:
        """
        Create a new character info JSON file.

        Args:
            file_name (str): The name of the JSON file.
            character_name (str): The name of the character.
            info (Dict): A dictionary containing character information.
        """
        os.makedirs(self.directory_path, exist_ok=True)
        character_file = os.path.join(self.directory_path, f"{file_name}.json")

        if os.path.exists(character_file):
            print(f"Character file '{character_file}' already exists.")
        else:
            character_info = {
                "name": character_name,
                "age": info.get("age", ""),
                "breed": info.get("breed", ""),
                "assets": info.get("assets", []),
            }

            with open(character_file, 'w') as file:
                json.dump(character_info, file, indent=4)

            print(f"Character file '{character_file}' created successfully!")

    def get_json_files(self) -> None:
        """
        Print a list of JSON files in the current directory.

        Returns:
            None
        """
        json_files = []
        for file_name in os.listdir(self.directory_path):
            file_path = os.path.join(self.directory_path, file_name)
            if file_name.endswith(".json") and file_name != "description.json":
                json_files.append(file_name)

        if len(json_files) > 0:
            print("The Shots in this subdirectory are:")
            for file_name in json_files:
                print(file_name)
        else:
            print("No Shots found in this subdirectory.")

    def get_json_file_info(self, file_name: str) -> Dict:
        """
        Get the contents of a JSON file.

        Args:
            file_name (str): The name of the JSON file.

        Returns:
            Dict: The contents of the JSON file as a dictionary, or None if the file does not exist.
        """
        file_path = os.path.join(self.directory_path, file_name)

        if os.path.exists(file_path) and file_name.endswith(".json"):
            with open(file_path, 'r') as file:
                json_data = json.load(file)
            return json_data
        else:
            print(f"JSON file '{file_name}' does not exist in the specified directory.")
            return None

    def edit_json_file(self, file_name: str, new_data: Dict) -> None:
        """
        Edit the contents of a JSON file.

        Args:
            file_name (str): The name of the JSON file to be edited.
            new_data (Dict): The updated data to be written to the file.
        """
        file_path = os.path.join(self.directory_path, file_name)

        if os.path.exists(file_path) and file_name.endswith(".json"):
            with open(file_path, 'w') as file:
                json.dump(new_data, file, indent=4)
            print(f"JSON file '{file_name}' has been successfully updated!")
        else:
            print(f"JSON file '{file_name}' does not exist in the specified directory.")

    def delete_json_file(self, file_name: str) -> None:
        """
        Delete a JSON file.

        Args:
            file_name (str): The name of the JSON file to be deleted.
        """
        file_path = os.path.join(self.directory_path, file_name)

        if os.path.exists(file_path) and file_name.endswith(".json"):
            os.remove(file_path)
            print(f"JSON file '{file_name}' has been successfully deleted!")
        else:
            print(f"JSON file '{file_name}' does not exist in the specified directory.")

    def print_assets_key_values(self, file_name: str) -> None:
        """
        Print the 'assets' key values from a JSON file.

        Args:
            file_name (str): The name of the JSON file.

        Returns:
            None
        """
        file_path = os.path.join(self.directory_path, file_name)

        if os.path.exists(file_path) and file_name.endswith(".json"):
            with open(file_path, 'r') as file:
                json_data = json.load(file)

            assets_values = json_data.get("assets", [])

            if assets_values:
                print(f"Assets key values in '{file_name}':")
                for asset in assets_values:
                    print(asset)
            else:
                print(f"No assets key values found in '{file_name}'.")
        else:
            print(f"JSON file '{file_name}' does not exist in the specified directory.")

# ==================================================================================== END SHOTS ====================================================================================


# ==================================================================================== BEGIN ASSETS ====================================================================================

class AssetManager:
    def __init__(self, directory_path: str):
        """
        Initialize the AssetManager with the directory path.

        Args:
            directory_path (str): The base directory path.
        """
        self.directory_path = directory_path

    def create_folders(self, folder_names: list) -> None:
        """
        Create multiple folders within the asset manager directory.

        Args:
            folder_names (list): A list of folder names to be created.

        Returns:
            None
        """
        for folder_name in folder_names:
            folder_path = os.path.join(self.directory_path, folder_name)
            if os.path.exists(folder_path):
                print(f"Folder '{folder_name}' already exists.")
            else:
                os.makedirs(folder_path)
                print(f"Folder '{folder_name}' created successfully!")

    def add_description_file(self, folder_name: str, description_data: dict) -> None:
        """
        Add a description file to a folder.

        Args:
            folder_name (str): The name of the folder.
            description_data (dict): The data to be written to the description file.

        Returns:
            None
        """
        folder_path = os.path.join(self.directory_path, folder_name)
        if os.path.exists(folder_path):
            description_path = os.path.join(folder_path, 'description.json')
            if os.path.exists(description_path):
                print(f"Description file already exists in folder '{folder_name}'.")
            else:
                with open(description_path, 'w') as file:
                    json.dump(description_data, file, indent=4)
                print(f"Description file added successfully to folder '{folder_name}'.")
        else:
            print(f"Folder '{folder_name}' does not exist.")

    def read_asset_folders(self, folder_name: str) -> list:
        """
        Get a list of asset folders within a folder.

        Args:
            folder_name (str): The name of the folder.

        Returns:
            list: A list of asset folder names.
        """
        folder_path = os.path.join(self.directory_path, folder_name)
        if os.path.exists(folder_path):
            asset_folders = []
            for entry in os.listdir(folder_path):
                entry_path = os.path.join(folder_path, entry)
                if os.path.isdir(entry_path):
                    asset_folders.append(entry)

            if len(asset_folders) == 0:
                print(f"No asset folders found in folder '{folder_name}'.")
            return asset_folders
        else:
            print(f"Folder '{folder_name}' does not exist.")
            return []
        
    def print_description_file(self, folder_name: str) -> None:
        """
        Print the contents of the description file in a folder.

        Args:
            folder_name (str): The name of the folder.

        Returns:
            None
        """
        folder_path = os.path.join(self.directory_path, folder_name)
        description_path = os.path.join(folder_path, 'description.json')
        if os.path.exists(description_path):
            with open(description_path, 'r') as file:
                description_data = json.load(file)
                print("Description File Contents:")
                print(json.dumps(description_data, indent=4))
        else:
            print(f"Description file not found in folder '{folder_name}'.")

    def update_description_file(self, folder_name: str, updated_data: dict) -> None:
        """
        Update the contents of the description file in a folder.

        Args:
            folder_name (str): The name of the folder.
            updated_data (dict): The updated data to be written to the description file.

        Returns:
            None
        """
        folder_path = os.path.join(self.directory_path, folder_name)
        description_path = os.path.join(folder_path, 'description.json')
        if os.path.exists(description_path):
            with open(description_path, 'r+') as file:
                existing_data = json.load(file)
                existing_data.update(updated_data)
                file.seek(0)
                json.dump(existing_data, file, indent=4)
                file.truncate()
                print(f"Description file in folder '{folder_name}' updated successfully.")
        else:
            print(f"Description file not found in folder '{folder_name}'.")

    def delete_asset_folder(self, folder_name: str) -> None:
        """
        Delete an asset folder.

        Args:
            folder_name (str): The name of the asset folder to be deleted.

        Returns:
            None
        """
        folder_path = os.path.join(self.directory_path, folder_name)
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)
            print(f"Asset folder '{folder_name}' deleted successfully.")
        else:
            print(f"Folder '{folder_name}' does not exist.")

    def create_json_file(self, folder_name: str, description_data: dict, file_name: str) -> None:
        """
        Create a JSON file in an asset folder.

        Args:
            folder_name (str): The name of the asset folder.
            description_data (dict): The data to be written to the JSON file.
            file_name (str): The name of the JSON file.

        Returns:
            None
        """
        folder_path = os.path.join(self.directory_path, folder_name)
        if os.path.exists(folder_path):
            file_path = os.path.join(folder_path, file_name)

            if os.path.exists(file_path):
                print(f"JSON file '{file_name}' already exists in folder '{folder_name}'.")
            else:
                with open(file_path, 'w') as file:
                    json.dump(description_data, file, indent=4)

                print(f"JSON file '{file_name}' created successfully in folder '{folder_name}'.")
        else:
            print(f"Folder '{folder_name}' does not exist.")