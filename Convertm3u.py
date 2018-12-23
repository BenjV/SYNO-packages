#!/usr/bin/env python2

import io, os

iTunesBase = '/Volumes/music/iTunes Master/Music'
SynoBase   = '..'
PlaylistFolder = '/volume1/music/playlists'

#Skip_EXTINF = False
Skip_EXTINF = True
#Test = ''
Test = '.tst'

    # Here we walk through all files and folders in the "PlaylistFolder"
for DirName, DirNames, FileNames in os.walk(PlaylistFolder):
    for FileName in FileNames:
            # Just interested in playlist files (ending with .m3u)
        if FileName.lower().endswith('.m3u'):
            FileSpec = os.path.join(DirName, FileName)
                # Open the playlist and read all lines.
            with io.open(FileSpec,'r',encoding='utf-8') as fp:
                InputLines = fp.readlines()
            OutputLines= []
                # Process all lines
            for Line in InputLines:
                if Line.startswith('#EXTINF:'):
                    if not Skip_EXTINF:
                        OutputLines.append(Line)
                else:
                    OutputLines.append(Line.replace(iTunesBase,SynoBase))
                # Write the outputbuffer to the file
            OutFileSpec = FileSpec.replace('.m3u',Test +'.m3u')
            with io.open(OutFileSpec, 'w', encoding='utf-8',newline='\r\n') as fp:
                fp.writelines(OutputLines)