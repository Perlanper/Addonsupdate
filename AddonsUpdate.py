# Addon Update Script
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 1. Add Addons to download on the form of: addon1 = "url" (ex: Simulationcraft = "https://www.curseforge.com/wow/addons/simulationcraft/download")
# 2. Add your defined addons to the addonlist. (addonslist = [addon_1, addon_2, ..., addon_n])
# 3. Update path to YOUR wow folder (make sure to add "\_retail_\Interface\AddOns").
# step 1,2 and 3 is done in the "user defined addons" section on lines 16-22
# 4. Save and run script.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
import webbrowser
import os
import glob
import time
import zipfile

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::user defined addons::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
simc = "https://www.curseforge.com/wow/addons/simulationcraft/download"
wa =   "https://www.curseforge.com/wow/addons/weakauras-2/download"

addonlist = [simc, wa]
wow_path = "C:\Program Files (x86)\World of Warcraft\_retail_\Interface\AddOns" # <- this is where you put YOUR wow path!
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::function declaration::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def FindDownloadPath():
    download_path = os.path.expanduser('~')
    return download_path + '\Downloads'

def GetLatestDownload(path):
    list_of_files = glob.glob(path +'\*') 
    latest_file = max(list_of_files, key=os.path.getmtime)
    latest_file = latest_file.split('\\')
    return latest_file[-1]

def CheckCacheExist(path):
    if os.path.exists(path):
        return
    os.mkdir(path)

#def CheckDownload():

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::variable declarations::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

download_path = FindDownloadPath()
temp_dir = "AddonsUpdateCache" #might be used for cool stuff later, but simply just a placeholder for now
cache_path = os.path.join(wow_path,temp_dir)
CheckCacheExist(cache_path) #if cache doesn't exist creates it 

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::actual downloading and move to cache:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

for i in addonlist:
   webbrowser.open(i)
   #print("sleeping - waiting for website")
   time.sleep(10) # waiting time on webpage "latest_file" will not work correctly if not sleeping
   file_name = GetLatestDownload(download_path)
   os.rename(download_path +'\\' + file_name, cache_path +'\\' + file_name)

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::extracting from downloaded archives::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
zipfile_names = os.listdir(cache_path)
for j in zipfile_names:
    #print(cache_path + '\\' + j)
    with zipfile.ZipFile(cache_path + '\\' + j, 'r') as zip_ref:
        zip_ref.extractall(wow_path)


#notes----------------------------------------------------------------------------------------------------------------------------------------------------------------
# script currently work for 2 addon download, haven't tested more at the moment. 
# unzipping of downloaded files seems to work as intended even if there are a folder with the same name in wow_path. if a folder with same name exists the unzipping occurs 
# recursively and replaces the files inside of the folder instead.
#---------------------------------------------------------------------------to do-------------------------------------------------------------------------------------
# 1. investigate sleeping function when more than 2 addons are being downloaded
# 2. implement a function that checks versions of the addons to avoid downloading an addon that is already up to date.
# 3. make a simple GUI for user friendliness but mostly for fun and learning purposes.