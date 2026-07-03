# Object classes from AP that represent different types of options that you can create
from Options import Option, FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange, OptionGroup, PerGameCommonOptions, OptionList
# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value
from typing import Type, Any


####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################

class ExcludedNations(OptionList):
    """List of Countries/Nations that you don't want to play with.
    Allowed values: USA, Germany, USSR, Great Britain, Japan, China, France, Italy, Sweden, Israel
    """
    display_name = "Excluded Nations"

class ExcludedVehicles(OptionList):
    """List of Countries/Nations that you don't want to play with.
    Allowed values: Aviation, Helicopters, Ground Targets, Bluefleet, Coastal Fleet
    """
    display_name = "Excluded Vehicle Types"

class ExcludedVehiclesComplex(OptionList):
    """List of Vehicle Game Roles that you don't want to play with. If "Excluded Vehicle Types" has entries, then the respective Game Roles will already be excluded.
    Excluding Roles like "Fighter" or "Medium Tank" will greatly shrink the possible amount of checks!
    Allowed values:
    - Aviation: Fighter, Bomber, Strike Aircraft
    - Helicopters: Attack Helicopter, Utility Helicopter
    - Ground Targets: Light Tank, Medium Tank, Heavy Tank, Tank Destroyer, SPAA
    - Bluefleet: Light Cruiser, Heavy Cruiser, Battlecruiser, Battleship
    - Coastal Fleet: Destroyer, Frigate, Boat, Heavy Boat, Barge
    """
    display_name = "Excluded Game Roles"

class ExcludedBR(OptionList):
    """List of Battle Ratings that you don't want to play with. This can lessen the pool greatly and is to be used with consideration!
    Allowed Range: 1.X - 14.X
    """
    display_name = "Excluded Battle Ratings"

# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith
#

# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict[str, Type[Option[Any]]]) -> dict[str, Type[Option[Any]]]:
	#   options["total_characters_to_win_with"] = TotalCharactersToWinWith

    options["excluded_nations"] = ExcludedNations
    options["excluded_vehicles"] = ExcludedVehicles
    options["excluded_complex_vehicles"] = ExcludedVehiclesComplex
    options["excluded_br"] = ExcludedBR
    
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: Type[PerGameCommonOptions]):
    # To access a modifiable version of options check the dict in options.type_hints
    # For example if you want to change DLC_enabled's display name you would do:
    # options.type_hints["DLC_enabled"].display_name = "New Display Name"

    #  Here's an example on how to add your aliases to the generated goal
    # options.type_hints['goal'].aliases.update({"example": 0, "second_alias": 1})
    # options.type_hints['goal'].options.update({"example": 0, "second_alias": 1})  #for an alias to be valid it must also be in options

    pass

# Use this Hook if you want to add your Option to an Option group (existing or not)
def before_option_groups_created(groups: dict[str, list[Type[Option[Any]]]]) -> dict[str, list[Type[Option[Any]]]]:
    # Uses the format groups['GroupName'] = [TotalCharactersToWinWith]
	
    return groups

def after_option_groups_created(groups: list[OptionGroup]) -> list[OptionGroup]:
    return groups
