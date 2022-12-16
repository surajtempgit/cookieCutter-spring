from cookiecutter.main import cookiecutter
import os
import json


HERE = os.path.abspath(os.path.dirname(__file__))



templateGitUrl= 'https://github.com/surajtempgit/cookieCutter-spring.git'

def loadDataFromJsonFile():
  with open(os.path.join(HERE, 'override_cookiecutter.json'), 'r') as f:
    data = json.load(f)
  return data


def main():
  overrideData = loadDataFromJsonFile()
  print(HERE)
  cookiecutter(template=templateGitUrl,
              #  skip inputs from keyboard
              no_input=True,
              # override default properties from cookiecutter.json 
              extra_context=overrideData,
              # Apply any new changes to already created template as cruft update
              overwrite_if_exists=True,
              # override default properties from cookiecutter.yml
              config_file=os.path.join(HERE,'default_inputs_cookiecutter.yml'),
              # project out directory or we can update existing at out dir
              output_dir=HERE
              )

if __name__ == "__main__":
    main()
