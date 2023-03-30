from evennia import Command, CmdSet

class CmdEnterTrain(Command):
    """
    entering the train

    Usage:
        enter train

    This will be available to players in
    the same location as the train and allows
    them to embark the train.
    """

    key = "enter train"
    locks = "cmd:not cmdinside()"

    def func(self):
        train = self.obj
        self.caller.msg("You get on the train.")
        self.caller.move_to(train, move_type="board")

class CmdExitTrain(Command):
    """
    exiting the train

    Usage:
        exit train

    This will be available to everyone inside the
    train. It allows them to exit the train at
    its current location.
    """

    key = "exit train"
    locks = "cmd:cmdinside()"

    def func(self):
        train = self.obj
        parent = train.location
        self.caller.msg("You get off the train.")
        self.caller.move_to(parent, move_type="disembark")

class TrainCmdSet(CmdSet):

    def at_cmdset_creation(self):
        self.add(CmdEnterTrain())
        self.add(CmdExitTrain())
