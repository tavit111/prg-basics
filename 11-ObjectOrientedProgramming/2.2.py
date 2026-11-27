# class definition
class Song:

  def __init__(self, artist, title, album, year):
    self.artist = artist
    self.title = title
    self.album = album
    self.year = year

  def __str__(self):
    return (                                #zawsze używamy return, ponieważ metoda ta musi zwrócić gotowy ciąg znaków 
        f"{'Performer:':<11}{self.artist}\n"
        f"{'Title:':<11}{self.title}\n"
        f"{'Album:':<11}{self.album}\n"
        f"{'Year:':<11}{self.year}"
    )


# object creation
song1 = Song("Ed Sheeran", "Hearts Don't Break Around Here", "Divide", 2017)
song2 = Song("Queen", "Bohemian Rhapsody", "A Night at the Opera", 1975)

# object usage
print(song1)
print()
print(song2)
