# SYNO-packages
DUE TO THE FACT THAT THE SICKCHILL DEVELOPERS HAVE CHOOSEN TO BLOCK THIS PYTHON APPLICATION TO RUN FROM SOURCE, MY PACKAGE DOES NOT RUN ANYMORE.
SO I HAVE REMOVED THEM FROM MY GITHUB.

The medusa package is still able to run from source, so I will keep supporting it for Synology devices both for DSM7 and pre DSM 7.

The Medusa packages are just wrappers around the official package from their githubs.  
So these are not different applications but just all the stuf needed to make a Synology package for them.
During installation or upgrading the source will be cloned from their github.

The sources are:  
https://github.com/pymedusa/Medusa  
https://github.com/SickChill/SickChill  

During installation they do a git fetch from those githubs.  
So you alway get the latest version.  
Updating these applications can be done from within the application itself.
So upgrading the package will normally not be needed unless Synology change the package structure again.

Both packages needs Git from the SynoCommunity.
On the versions for DSM 6 a Python 3 package is needed (either from Synology or the SynoCommunity.
On the DSM 7 version it will use the SynoCommunity Python3.8 is installed, if not the Python3 which is part of DSM 7

The DSM 7 packages can only be installed on DSM 7.0-4000 or later.
The other packages will not function on DSM 7
  
Because of the way DSM is designed, used ports are fixed during package installation.  
So changing the port whithin the application will not function.

When you are upgrading to DSM 7 it is best to make a backup from within the packages and remove them before upgrading to DSM 7.
After upgrading to DSM 7 install the DSM 7 version and restore the data.

If you upgrade to DSM 7 and did not do it this way, the packages will try to recover the database and config.
No garantee it will succeed.

Permissions to shares must be granted via the "system internal user"
If you have existing folders and files on an existing share, don't forget also to grand privs recursively with FileStation
For details see:
https://github.com/SynoCommunity/spksrc/wiki/Permission-Management