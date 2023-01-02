from cookiecutter.main import cookiecutter
import os
import json
from jproperties import Properties

HERE = os.path.abspath(os.path.dirname(__file__))


# create app-config.properties and expose env variable COOKIE_CONFIG_HOME= { path to app-config.properties }
def loadPropertiesFile():
  configs = Properties()
  CONFIG_FILE=""
  # load app-config.properties from ENV variable
  if(os.getenv("COOKIE_CONFIG_HOME")):
    CONFIG_FILE=os.getenv("COOKIE_Home")
  # loads app-config.properties from repo
  else:
    CONFIG_FILE="app-config.properties"
    
  with open(CONFIG_FILE, 'rb') as config_file:
    configs.load(config_file) 
  return configs

# To read config from external coockiecutter Yml file
def loadConfigFromYmlFile(configs:Properties):
  if(configs.get('externalConfigYml')):
    return configs.get('externalConfigYml').data
  else:
    return os.path.join(HERE,'default_inputs_cookiecutter.yml') 

# To override properties from YML file
def loadConfigFromJsonFile(configs:Properties):
  data = {}
  jsonFile=configs.get('externalConfigJson')
  if(jsonFile):
    with open(os.path.join(HERE, jsonFile.data), 'r') as f:
      data = json.load(f)
  return data


def main():
  configs = loadPropertiesFile()
  configFile = loadConfigFromYmlFile(configs)
  overrideData = loadConfigFromJsonFile(configs)
  templateGitUrl=configs.get('templateGitUrl').data

  cookiecutter(template=templateGitUrl,
              #  skip inputs from keyboard
              no_input=True,
              # override default properties from cookiecutter.json 
              extra_context=overrideData,
              # Apply any new changes to already created template as cruft update
              overwrite_if_exists=True,
              # override default properties from cookiecutter.yml
              config_file=configFile,
              # project out directory or we can update existing at out dir
              output_dir=HERE
              )


if __name__ == "__main__":
    main()
