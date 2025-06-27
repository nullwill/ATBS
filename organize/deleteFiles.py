import os
from pathlib import Path

for filename in Path.cwd().glob('*.rxt'):
    os.unlink(filename) # <--- this would delete files ending in '.rxt'
    print('Deleting', filename)