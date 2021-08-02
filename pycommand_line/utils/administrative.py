from .command_line import CommandLine


class AdminCommandLine(CommandLine):
    def __init__(self, argv: list[str]):
        super(AdminCommandLine, self).__init__(argv=argv)
        self.registered_commands.append(self.test)

    def test(self):
        print("TESTING: function works...")
