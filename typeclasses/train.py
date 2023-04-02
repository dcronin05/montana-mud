from evennia import DefaultObject, search_object

from commands.train import TrainCmdSet


class Train(DefaultObject):

    def at_object_creation(self):

        self.cmdset.add_default(TrainCmdSet)
        self.db.desc = "Its the train from the movies, ya know?!"

        self.db.driving = False
        self.db.direction = 1
        self.db.rooms = ['#77', '#81', '#84', '#87', '#93']

    def start_driving(self):
        self.db.driving = True

    def stop_driving(self):
        self.db.driving = False

    def goto_next_room(self):
        currentroom = self.location.dbref
        idx = self.db.rooms.index(currentroom) + self.db.direction

        if idx < 0 or idx >= len(self.db.rooms):
            self.stop_driving()
            self.db.direction *= -1

        else:
            roomref = self.db.rooms[idx]
            room = search_object(roomref)[0]
            self.move_to(room)
            self.msg_contents(f'The train is moving forward to {room.name}.')
