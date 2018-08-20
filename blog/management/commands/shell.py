from django.core.management.commands.shell import Command as ShellCommand
import os


class Command(ShellCommand):
    # ShellCommand.shells.insert(0,'ptpython')
    # Note when you define a class with brackets after then what you are doing is actually defining a subclass of what is in teh brackets - so ShellCommand here (which is actually originally Command from core/management if you look at the import) is a class that already exists. In the above commented out line I was mutating it to include ptypthon BUT its a bad idea to mutate classes so Ive used below instead:

    shells = ['ptpython'] + ShellCommand.shells

    def ptpython(self, options):
        from ptpython.repl import embed
        embed(globals(), locals(), vi_mode=False)
