rsync
=====

rsync is a utility for efficiently transferring and synchronizing files between a computer and a storage
drive and across networked computers by comparing the modification times and sizes of files.

Rsync is written in C as a single threaded application.
The rsync algorithm is a type of delta encoding, and is used for minimizing network usage.
Zlib may be used for additional data compression, and SSH or stunnel can be used for security.
Rsync is the facility typically used for synchronizing software repositories on mirror sites used by package management systems.

Rsync is typically used for synchronizing files and directories between two different systems.
For example, if the command `rsync local-file user@remote-host:remote-file` is run, rsync will use SSH to connect as user to remote-host.
Once connected, it will invoke the remote host's rsync and then the two programs will determine what parts of the
local file need to be transferred so that the remote file matches the local one.

Rsync can also operate in a daemon mode (rsyncd), serving and receiving files in the native rsync protocol (using the "rsync://" syntax).

Vulnerabilities
---------------

.. toctree::
   :maxdepth: 1

   CVE-2022-29154