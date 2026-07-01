import os

from . import data

def write_tree(directory='.'):
    """
    """
    with os.scandir(directory) as it:
        for entry in it:
            full = f'{directory}/{entry.name}'
            if is_ignored(full):
                continue
            if entry.is_file(follow_symlinks=False):
                print(full)

    # TODO: Create tree object 

def is_ignored(path):
    return '.twit' in path.split('/')