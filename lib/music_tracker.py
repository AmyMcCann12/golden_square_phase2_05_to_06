class MusicTracker():

    def __init__(self):
        self.track_list = []
        
    def add_track(self, track_name):
        self.track_list.append(track_name)
        
    def get_track_list(self):
        if self.track_list == []:
            raise Exception("No tracks have been added")
        return self.track_list