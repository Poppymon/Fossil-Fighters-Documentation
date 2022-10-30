# Fossil-Fighters-Documentation
The documentation stuff in Chunk Editor was getting kind of unwieldy, and I discovered the stuff for teams
which is very important but also very much not chunked. So I decided to make a new repo with all my
documentation in it, and take the opportunity to clean some stuff up too.

If you somehow got here without going through Chunk Editor, please do check it out! It can be found at
https://github.com/opiter09/FF1-FFC-Chunk-Editor.

A note on general terminology (since I have nowhere else to put it):
- When I say that everything everywhere is little-endian, I mean that you have to reverse the bytes before
  converting to get the correct value. For example, 2C 01 --> 0x12C --> 300.
- In order to interpret all my locations, you need to be able to read a hex editor's layout. The leftmost
  column represents all digits except the last one, while the topmost row is for the last digit. So to find
  location 0x28, head to row 00000020 and column 08.

