
from distutils.core import setup
import py2exe, os

origIsSystemDLL = py2exe.build_exe.isSystemDLL # save the orginal before we edit it
def isSystemDLL(pathname):
    # checks if the freetype and ogg dll files are being included
    if os.path.basename(pathname).lower() in ("libfreetype-6.dll", "libogg-0.dll", "sdl_ttf.dll"):
            return 0
    return origIsSystemDLL(pathname) # return the orginal function
py2exe.build_exe.isSystemDLL = isSystemDLL # override the default function with this one

setup(console = ['main.py'],
author='Jose Castelo',
author_email='jbcastelo@hotmail.com',
url='http://www.reddit.com/r/gamedev',
data_files=[('.', [
'AnonymousPro.ttf']
), ('sprites', [
'sprites/water.png', 'sprites/player.png', 'sprites/zombie.png', 'sprites/uibackground.png', 'sprites/tree.png', 'sprites/grass.png', 'sprites/bullet.png']
)]
) 

