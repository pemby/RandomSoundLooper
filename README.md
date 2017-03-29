# Random Sound Looper
This project was created so I could play a onerandom bird call/song out of a set of audio files.
This this could be used anywhere random sounds need to be played at random intervals. 
Haunted houses -> to play ghostly sounds.
Near Birdfeeders -> to attract birds. 
ETC... 
## Installation
Requires: Python 3.5 or greater, written in linux. So "OS" calls may have to be changed for WIN or OSX.
    
 
    import time
    import os
    import random
    import pygame

## Usage
1. Drop sound files into the "Sound Directory"
2. Set Max and Min constants in seconds


    min_time_between_calls = 5
    max_time_between_calls = 300

3. Set Max and min Volumes  

     
     (.0 < volume < 1)  
     randome_volume_max = 1
     random_volume_min = .1

## Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D




# License
MIT License

Copyright (c) 2017 Brian Pemberton

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.