"""NEW REPO CLI
Usage:
    new_repo [NAME] 
                [--private] 
    new_repo -h|--help
    new_repo -v|--version
Arguments:
  NAME  repo name
Options:
    -p --private  private repo
    -h --help  Show this screen.
    -v --version  Show version.
"""

from docopt import docopt
from subprocess import call
import os

def new_repo(params):
    visibility = '--public' if params['visible'] else "--private"
    cmd = f"gh repo create {params['name']} -y {visibility}"
    os.system(cmd)
    if not os.path.exists(params['name']):
        print("Couldn't find repo")
    else:
        filename = os.path.join(params['name'], "README.md")
        with open(filename, "w") as file:
            file.write(f"# {params['name']}")
        folder = os.path.join(os.getcwd(), params['name'])
        call("git add .",cwd=folder, shell=True)
        call('git commit -m "first commit"',cwd=folder, shell=True)
        call("git push -u origin master",cwd=folder, shell=True)
        


if __name__ == '__main__':
    params = {
        "name": "",
        "visible": True
    }
    arguments = docopt(__doc__, version='version 1.0')
    if arguments['NAME']:
        params['name'] = arguments['NAME']
        if arguments['--private']:
            params['visible'] = False
        new_repo(params)
