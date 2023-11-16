import pytest #type: ignore
from lib.music_tracker import *

""" 
If we do not add any tracks, then throw an exception
when requesting track list 
"""
def test_music_tracker_no_tracks_added_raises_error():
    music_tracker = MusicTracker()
    with pytest.raises(Exception) as err:
        music_tracker.get_track_list()
    assert str(err.value) == "No tracks have been added"

"""
If we add one track, then we can view that track in the track list
"""
def test_music_tracker_one_track_added():
    music_tracker = MusicTracker()
    music_tracker.add_track("Song Title 1")
    assert music_tracker.get_track_list() == ["Song Title 1"]

"""
If we add three tracks, then we can view all those tracks in the track list
"""
def test_music_tracker_three_tracks_added():
    music_tracker = MusicTracker()
    music_tracker.add_track("Song Title 3")
    music_tracker.add_track("Song Title 1")
    music_tracker.add_track("Song Title 2")
    assert music_tracker.get_track_list() == ["Song Title 3", "Song Title 1", "Song Title 2"]