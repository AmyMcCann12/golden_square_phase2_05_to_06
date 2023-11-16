## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
class MusicTracker():
    # No user facing properties
    def __init__(self):
        pass # No code here yet

    def add_track(self, track_name):
        # Parameters: 
        #   track_name: string (provides the name of the track I have listened to)
        # Returns:
        #   Nothing
        # Side Effect: adds the track_name to a list of all tracks listened to.
    
    def get_track_list(self):
        # Parameters: none
        # Returns:
        # a list of all the tracks listened to
        # Side effect:
        #   throws an exception if track list is empty

```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
""" 
If we do not add any tracks, then throw an exception
when requesting track list 
"""

music_tracker = MusicTracker()
music_tracker.get_track_list() # => "No tracks have been added."

"""
If we add one track, then we can view that track in the track list
"""

music_tracker = MusicTracker()
music_tracker.add_track("Song Title 1")
music_tracker.get_track_list() # => ["Song Title 1"]

"""
If we add three tracks, then we can view all those tracks in the track list
"""

music_tracker = MusicTracker()
music_tracker.add_track("Song Title 3")
music_tracker.add_track("Song Title 1")
music_tracker.add_track("Song Title 2")
music_tracker.get_track_list() # => ["Song Title 3", "Song Title 1", "Song Title 2]



```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._