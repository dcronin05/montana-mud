# in a new file mygame/commands/mechcommands.py

from evennia import Command

class CmdFire(Command):
    """
    Firing the mech’s gun

    Usage:
      fire [target]

    This will fire your mech’s main gun. If no
    target is given, you will shoot in the air.
    """
    key = "fire"
    aliases = ["fire", "fire!", "shoot"]

    def func(self):
        "This shoosts the gun thing."

        caller = self.caller
        location = caller.location

        if not self.args:
            # no argument given to command - shoot in the air
            message = "BANG! The mech fires its gun wildly!"
            location.msg_contents(message)
            return

        # we have an argument, search for target
        target = caller.search(self.args.strip())
        if target:
            location.msg_contents(
                f"BANG! The mech shoots its guns at {target.key}"
            )

class CmdLaunch(Command):
    """
    Firing the mech's rocket launchers

    Usage:
      launch [target]

    This will fire your mech's missile launcher.
    If no target is given, you will shoot the ground.
    """

    key = "launch"
    aliases = ["launch!", "missile", "missiles"]

    def func(self):
        "This launches the missiles."

        caller = self.caller
        location = caller.location

        if not self.args:
            message = "WOOOSH! The mech launches missiles into the distance."
            location.msg_contents(message)
            return

        target = caller.search(self.args.strip())
        if target:
            location.msg_contents(
                f"BOOOM! The mech launches missiles at {target.key} which explode violently."
            )

