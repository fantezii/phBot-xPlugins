from phBot import *
from threading import Timer
import shutil
import time
import os

pName = 'xAutoConfig'
pVersion = '0.2.5'
pUrl = 'https://raw.githubusercontent.com/JellyBitz/phBot-xPlugins/master/xAutoConfig.py'

# Copy or replace a file while print an user message
def ReplaceFile(newPath,oldPath,message):
	shutil.copyfile(newPath,oldPath)
	log(message)

# Called when the user successfully selects a character. No character data has been loaded yet.
def joined_game():
	# JSON config check
	configFile = get_config_path()
	if not os.path.exists(configFile):
		# JSON default configs path
		defaultConfig = get_config_dir()+"Default.json"
		if os.path.exists(defaultConfig):
			ReplaceFile(defaultConfig,configFile,"Plugin: Default JSON loaded")
	# Db3 config check
	configFile = get_config_path().replace(".json",".db3")
	if os.path.exists(configFile):
			# db3 default filter path
		defaultConfig = get_config_dir()+"Default.db3"
		if os.path.exists(defaultConfig):
			# Check modification time at seconds
			lastModification = time.time() - os.path.getmtime(configFile)
			# Replace filter if was created or edited a few seconds ago
			if lastModification < 2:
				log("Plugin: Filter was probably created a few seconds ago")
				log("Plugin: Filter by default will be loaded in 10 seconds..")
				Timer(10.0,ReplaceFile,(defaultConfig,configFile,"Plugin: Default Filter loaded"),).start()
	else:
		defaultConfig = get_config_dir()+"Default.db3"
		if os.path.exists(defaultConfig):
			log("Plugin: Filter not found. Default will be loaded in 10 seconds..")
			Timer(10.0,ReplaceFile,(get_config_dir()+"Default.db3",configFile,"Plugin: Default Filter loaded"),).start()

log('Plugin: '+pName+' v'+pVersion+' successfully loaded')