import argparse

from socialpy.funcs import clear, setup, check

def main():
    parser = argparse.ArgumentParser(description='SocialPy')
    parser.add_argument('action', type=str, choices=['setup', 'clear'])

    args = parser.parse_args()

    if args.action == 'setup':
        setup()
        exit()

    if args.action == 'clear':
        clear()
        exit()

    parser.print_help()

if __name__ == '__main__':
    main()
