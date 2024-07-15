from dataclasses import dataclass
from typing import TYPE_CHECKING

import yaml

if TYPE_CHECKING:
    from pathlib import Path


@dataclass
class Settings:
    """
    Global bot settings

    Attributes
    ----------
    search_x: int
        The x coordinate of the search bar
    search_y: int
        The y coordinate of the search bar
    clean_x: int
        The x coordinate of the clean button
    clean_y: int
        The y coordinate of the clean button
    item_x: int
        The x coordinate of the item
    item_y: int
        The y coordinate of the item
    board_x: int
        The x coordinate of the board
    board_y: int
        The y coordinate of the board
    clean_search_x: int
        The x coordinate of the clean button
    clean_search_y: int
        The y coordinate of the clean button
    no_item_x: int
        The x coordinate of the no item text
    no_item_y: int
        The y coordinate of the no item text
    save_factor: float
        The factor by which wait times are multiplied
    
    """

    # coordinates
    search_x: int = 1840
    search_y: int = 1124

    clean_x: int = 1464
    clean_y: int = 1127

    item_x: int = 1546
    item_y: int = 97

    board_x: int = 900
    board_y: int = 500

    clean_search_x: int = 1840
    clean_search_y: int = 1124

    no_item_x: int = 1664
    no_item_y: int = 113

    # config
    save_factor: float = 1

settings = Settings()


def read_settings(path: "Path"):
    content = yaml.load(path.read_text(), yaml.Loader)

    settings.save_factor = content["config"]["save_factor"]

    settings.search_x = content["coordinates"]["search_bar"]["search_x"]
    settings.search_y = content["coordinates"]["search_bar"]["search_y"]

    settings.clean_x = content["coordinates"]["clean_board"]["clean_x"]
    settings.clean_y = content["coordinates"]["clean_board"]["clean_y"]

    settings.item_x = content["coordinates"]["item"]["item_x"]
    settings.item_y = content["coordinates"]["item"]["item_y"]

    settings.board_x = content["coordinates"]["board"]["board_x"]
    settings.board_y = content["coordinates"]["board"]["board_y"]

    settings.clean_search_x = content["coordinates"]["clean_search"]["clean_search_x"]
    settings.clean_search_y = content["coordinates"]["clean_search"]["clean_search_y"]
    
    settings.no_item_x = content["coordinates"]["no_item"]["no_item_x"]
    settings.no_item_y = content["coordinates"]["no_item"]["no_item_y"]


def write_default_settings(path: "Path"):
    path.write_text(
        """# yaml-language-server: $schema=json-config-ref.json

# configuration for the bot
config:

    # the factor by which wait times are multiplied, recommended to be 1 or above.
    # if you want to speed up the bot, you can increase this value
    # but be aware that it might cause the bot to fail, since
    # the website might not be able to keep up with the bot

    save_factor: 1    
    
# Contains all the coordinates needed for the bot to function
# default values are for Microsoft Edge, 1920x1080 resolution
coordinates:

    # coordinates for the search bar, where you search for items
    search_bar:

        search_x: 1840

        search_y: 1124

    # coordinates for the clean button, which clears the board
    clean_board:
        
        clean_x: 1464
    
        clean_y: 1127

    # coordinates for the item, which is the item you want to craft
    item:
    
        item_x: 1546
    
        item_y: 97

    # coordinates for the board, where you place the items
    board:
    
        board_x: 900
    
        board_y: 500

    # coordinates for the clean button in the search bar
    clean_search:

        clean_search_x: 1840
    
        clean_search_y: 1124

    # coordinates for the no item text, 
    # which appears when the item is not found (position on black text, rgb has to be 0, 0, 0)
    no_item:

        no_item_x: 1664

        no_item_y: 113

  """
    )

