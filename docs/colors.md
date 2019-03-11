# Color managment in sketcher

Methods that take a color in argument can use different format as input.
These different format are the ones supported by the constructor of the
class `sketcher.common.Color`.

Supported format are:
- color name string in  'black', 'white', 'red', 'green', 'blue', grey'
- three component tuple of numbers between 0 and 255 like `(255, 0, 255)`
  (purple) representing the three components red, green and blue of the color.
- a single number, between 0 and 255, produce a grey level
- another instance of `Color`

The `Color` instance are then converted to a backend specific format using one of
the methods.

Currently there are three methods:
- `color.hashtag()` output the HTML style string (`#FF00FF` for purple)
- `color.tuple255()` output a tuple of three integers between 0 and 255.
- `color.tuple255alpha()` output a tuple of four integers between 0 and 255.
  The last component is the alpha (transparency) and is currently always 255
  (fully opaque)
