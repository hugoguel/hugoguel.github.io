# imports - standard imports
import sys, os
import yaml

# imports - third-party imports
import addict

# imports - module imports
import build

DEFAULT_FNAME = '_config.yml'

yaml.add_representer(addict.Dict, yaml.representer.Representer.represent_dict)

def main(args = None):
    filename  = DEFAULT_FNAME
    
    with open(filename, 'w') as f:
        yaml.dump(build.CONFIG, f, allow_unicode = True)

if __name__ == '__main__':
    args = sys.argv[1:]

    code = main()

    sys.exit(code)
