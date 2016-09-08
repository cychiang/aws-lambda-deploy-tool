import argparse
import zipfile
import sys
import os
import datetime
from shutil import copyfile

# Parse input arguments
parser = argparse.ArgumentParser()
parser.add_argument('--base')
parser.add_argument('--files', nargs='*')
args = parser.parse_args()

# Is zipfile?
if zipfile.is_zipfile(args.base):
    isFiles = [ os.path.isfile(obj) for obj in args.files ]
    if False in isFiles:
        for idx, val in enumerate(isFiles):
            if val is False:
                print('%s seems not a file.' %args.files[idx])
        sys.exit()
    else:
        # copy 
        print('copy zipfile...')
        copyfile(args.base, 'out.zip')
        # packing up
        print('Packing up!!!')
        # append mode
        packing = zipfile.ZipFile('out.zip', mode='a')
        for obj in args.files:
            try:
                packing.write(obj)
            finally:
                packing.close()
else:
    print('Seems your %s not a proper zipfile.' %args.base)
    sys.exit()