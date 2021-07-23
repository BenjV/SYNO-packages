# SYNO-packages
DUE TO THE FACT THAT THE SICKCHILL DEVELOPERS HAVE CHOOSEN TO BLOCK THIS PYTHON APPLICATION TO RUN FROM SOURCE, MY PACKAGE DOES NOT RUN ANYMORE.

SO I HAVE REMOVED THEM FROM MY GITHUB.


The medusa package is still able to run from source, so I will keep supporting it for Synology devices both for DSM7 and pre DSM 7.

The Medusa package is just wrappers around the official package from their githubs.  
So it is not a different applications but just all the stuff needed to make a Synology package.
During installation or upgrading the source will be cloned from their github.

The sources are:  
https://github.com/pymedusa/Medusa  

During installation they do a git fetch from those githubs.  
So you alway get the latest version.  
Updating these applications can be done from within the application itself.
So upgrading the package will normally not be needed unless Synology change the package structure again.

Both packages needs Git from the SynoCommunity.
The package can use the python 3.8 from the SYnocommunity or the Python 3 from Synology
On the versions for DSM 6 a Python 3 package needs to be installed (either from Synology or the SynoCommunity.
On the DSM 7 version it will use the SynoCommunity Python3.8 is installed, if not the Python3 which is included in DSM 7. 

The DSM 7 packages can only be installed on DSM 7.0-4000 or later.

The DSM 6 packages cannot be installed on DSM 7
  
Because of the way DSM is designed, used ports are fixed during package installation.  
So changing the port whithin the application will not function en will be reversed during startup.

When you are upgrading to DSM 7 it is best to make a backup from within the packages and remove them before upgrading to DSM 7.
After upgrading to DSM 7 install the DSM 7 version and restore the data.

If you upgrade to DSM 7 and did not do it this way, the packages will try to recover the database and config.
No garantee it will succeed.

Permissions to shares where your downloader puts the video's must be granted via the "system internal user" sc-medusa/
If you use postprocessing to copy or move video's the share where you want to put the files must also be given permissions to the same user.

If you have existing folders and files on an existing share, don't forget also to grand prermissions recursively to that user with FileStation.
For details see:
https://github.com/SynoCommunity/spksrc/wiki/Permission-Management