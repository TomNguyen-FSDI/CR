"""
id, title, featured_artist, length, written_by
"""

class Song:
    id = 0
    title = ''
    featured_artist = ''
    length_of_track = ''
    written_by = ''

    def __init__(self, id, title, featured_artist, length_of_track, written_by):
            self.id = id
            self.title = title
            self.featured_artist = featured_artist
            self.length_of_track = length_of_track
            self.written_by = written_by
    
    def __str__(self):
        return "ID: {}, Title: {}, Featured Artist: {}, Length: {}, Written By: {}".format(self.id, self.title, self.featured_artist, self.length_of_track, self.written_by)
