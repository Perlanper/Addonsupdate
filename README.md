# Addonsupdate
script for updating addons for wow
# Addon Update Script
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 1. Add Addons to download on the form of: addon1 = "url" (ex: Simulationcraft = "https://www.curseforge.com/wow/addons/simulationcraft/download")
# 2. Add your defined addons to the addonlist. (addonslist = [addon_1, addon_2, ..., addon_n])
# 3. Update path to YOUR wow folder (make sure to add "\_retail_\Interface\AddOns").
# step 1,2 and 3 is done in the "user defined addons" section on lines 16-22
# 4. Save and run script.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

#notes----------------------------------------------------------------------------------------------------------------------------------------------------------------
# script currently work for 2 addon download, haven't tested more at the moment. 
# unzipping of downloaded files seems to work as intended even if there are a folder with the same name in wow_path. if a folder with same name exists the unzipping occurs 
# recursively and replaces the files inside of the folder instead.
#---------------------------------------------------------------------------to do-------------------------------------------------------------------------------------
# 1. investigate sleeping function when more than 2 addons are being downloaded
# 2. implement a function that checks versions of the addons to avoid downloading an addon that is already up to date.
# 3. make a simple GUI for user friendliness but mostly for fun and learning purposes.