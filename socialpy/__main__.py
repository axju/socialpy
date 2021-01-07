from socialpy.commands.root import RootCommand


def main(argv=None):
    cmd = RootCommand()
    cmd.parse_args(argv)


if __name__ == '__main__':
    main()
