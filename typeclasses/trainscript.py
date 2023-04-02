from evennia import DefaultScript


class TrainStoppedScript(DefaultScript):

    def at_script_creation(self):
        self.key = 'trainstopped'
        self.interval = 30
        self.persistant = True
        self.repeats = 1
        self.smart_delay = True

    def at_repeat(self):
        self.obj.start_driving()

    def at_stop(self):
        self.obj.scripts.add(TrainDrivingScript)


class TrainDrivingScript(DefaultScript):

    def at_script_creation(self):
        self.key = 'traindriving'
        self.interval = 5
        self.persistant = True

    def is_valid(self):
        return self.obj.db.driving

    def at_repeat(self):
        if not self.obj.db.driving:
            self.stop()
        else:
            self.obj.goto_next_room()

    def at_stop(self):
        self.obj.scripts.add(TrainStoppedScript)
