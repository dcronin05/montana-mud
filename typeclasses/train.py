from typeclasses.objects import Object
from commands.train import TrainCmdSet


class Train(Object):

    def at_object_creation(self):
        # We'll add in code here later.
        self.cmdset.add_default(TrainCmdSet)
        self.db.desc = "Its the train from the movies!"
