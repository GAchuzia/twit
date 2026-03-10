import argparse

def parse_args():
    """
    Implements sub commands using the built-in Python library
    """
    parser = argparse.ArgumentParser()
    
    commands = parser.add_subparsers(dest='comman')
    commands.required = True

    init_parser = commands.add_parser('init')
    init_parser.set_defaults(func=init)

    return parser.parse_args()

def init(args):
    """
    """
    print("Hello, World!") #TODO: make this an actual init command

def main():
    args = parse_args()
    args.func(args)