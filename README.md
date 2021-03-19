# SYNO-packages
The SickChill and Medusa packages are just wrappers around the official package from their githubs.  
So these are not different applications but just all the stuf needed to make a Synology package for them.  

The sources are:  
https://github.com/pymedusa/Medusa  
https://github.com/SickChill/SickChill  

During installation they do a git fetch from those githubs.  
So you alway get the latest version.  
Updating these applications can be done from within the application itself.  

Both packages needs Git and Python3.  
Python3 can be from the SynoCommunity(3 or 3.8) or from Synology 
  
Because of the way DSM is designed, used ports are fixed during package installation.  
So changing the port whithin the application will not function.

This package is not an upgrade of an old (python 2) package.  
So make a backup from within SickChil or Medusa first and restore it after the new installation.
