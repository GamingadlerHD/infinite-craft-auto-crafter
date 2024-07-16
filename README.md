# Automatically Craft Items in Infinity Craft

This repository contains the code for a bot which simulates user input for the popular online game Infinite Craft.

## Features
The project offers multiple modes to craft.

### Crafting Modes

| Mode Name               | Description                                                                                                         | Purpose                                |
|-------------------------|---------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| Database Mode           | Craft items from a database with over 16k recipes. [Database Origin](https://github.com/admin-else/infinity-scrape) | Gain a starting inventory              |
| Create Collection Mode  | Create a collection of items to use in different modes                                                              | Use in different modes                 |
| Add to Collection Mode  | Add more items to a collection                                                                                      | Use in different modes                 |
| Load Collection Mode    | Craft every item in a collection together with every other item in this collection                                  | Gain new items in a controlled category|
| One to Collection Mode  | Craft an item together with all items of a collection                                                               | Gain new items                         |

### Additional Modes

| Mode Name      | Description                                                                                                                         |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Display Mode   | Displays your mouse position, helpful for filling out the settings file                                                             |
| Converter Mode | Convert a downloaded save file from [Infinite Craft Helper](https://greasyfork.org/en/scripts/488667-infinite-craft-helper) to a collection |

## Installation

### Prerequisites

1. **Python**: Make sure you have Python installed. You can download it from the [official Python website](https://www.python.org/downloads/).
    - To check if Python is installed, open your terminal or command prompt and run:
    ```bash
    python --version
    ```
    - If Python is installed, this command will display the version number. If not, follow the instructions on the Python website to install it.

2. **Git**: Ensure you have Git installed. You can download it from the [official Git website](https://git-scm.com/downloads).
    - To check if Git is installed, open your terminal or command prompt and run:
    ```bash
    git --version
    ```
    - If Git is installed, this command will display the version number. If not, follow the instructions on the Git website to install it.

### Cloning the Repository

1. Open your terminal or command prompt.

2. Navigate to a directory where you want to clone the repository. You can use the `cd` command to change directories. For example:
    ```bash
    cd path/to/your/directory
    ```

3. Clone the repository by running the following command:
    ```bash
    git clone https://github.com/GamingadlerHD/infinite-craft-auto-crafter
    ```

### Installing Dependencies

1. After cloning the repository, navigate into the cloned folder:
    ```bash
    cd infinite-craft-auto-crafter
    ```

2. Inside the folder, you need to install all the required Python packages. This can be done using `pip`, which is the package installer for Python. Run the following command:
    ```bash
    pip install -r requirements.txt
    ```
    - This command will read the `requirements.txt` file and install all the packages listed in it.

### Running the Bot

Once the dependencies are installed, you should be ready to run the bot. Follow additional instructions provided in the 'Usage' Category to configure and start the bot.



## Usage

This section provides detailed instructions on how to use the different modes available in the auto-crafting script.

### Prerequisites

Ensure you have completed the installation steps and have the necessary dependencies installed.

### Running the Script

1. Open your terminal or command prompt.
2. Navigate to the directory containing the script.
3. Run the script using the following command:
    ```bash
    python run.py
    ```
4. You will see a yellow information showing you that a settings.yaml file was created
5. You will need to fill out this file, you can restart the script with the default coordinates and run the display mode to help you fill out the settings
6. start the script agiain using
   ```bash
    python run.py
    ```

### Modes

When you run the script, you will be prompted to select one of the available modes. Below are detailed instructions for each mode:

#### 1. Database Mode

Craft items from a database with over 16,000 recipes.

1. Select "Database" mode.
2. Enter the start and stop numbers when prompted, 0 is the first number and is a basic recepie.
3. The script will automatically craft items within the specified range. Press and hold 'x' to stop the process at any time.

#### 2. Create Collection Mode

Create a collection of items to use in different modes.

1. Select "Create Collection" mode.
2. Enter the items one by one. Press enter without typing anything to finish.
3. Enter a name for the collection when prompted. The collection will be saved as a JSON file in the `saves` directory.

#### 3. Add to Collection Mode

Add more items to an existing collection.

1. Select "Add to Collection" mode.
2. Enter the name of the collection you want to add items to.
3. Enter the items one by one. Press enter without typing anything to finish. The updated collection will be saved.

#### 4. Load Collection Mode

Craft every item in a collection together with every other item in that collection.

1. Select "Load Collection" mode.
2. Enter the name of the collection when prompted.
3. The script will automatically craft items from the collection. Press 'x' to stop the process at any time.

#### 5. One to Collection Mode

Craft a specified item together with all items of a collection.

1. Select "One to Collection" mode.
2. Enter the name of the collection when prompted.
3. Enter the item to craft with.
4. The script will automatically craft the specified item with each item in the collection. Press 'x' to stop the process at any time.

#### 6. Converter Mode

Convert a downloaded save file from [Infinite Craft Helper](https://greasyfork.org/en/scripts/488667-infinite-craft-helper) to a collection.

1. Coppy your downloaded file to the `saves` directory.
2. Select "Converter" mode.
3. Enter the name of the existing collection to convert.
4. Enter the new name for the converted collection.
5. The script will save the converted collection with the new name.

#### 7. Display Mode

Displays your mouse position, helpful for filling out the settings file.

1. Select "Display" mode.
2. The current mouse position will be displayed on the screen.


### Notes

- Your collections are saved in the `saves` directory.
- You can press 'x' to stop the crafting process at any time.
- Sometimes the Bot will fail due to the search function of infinity craft, i recommend using [Infinite Craft Helper](https://greasyfork.org/en/scripts/488667-infinite-craft-helper) to fix this.

---





