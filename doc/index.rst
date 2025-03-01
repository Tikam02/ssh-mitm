SSH-MITM - ssh audits made simple
=================================

ssh man-in-the-middle (ssh-mitm) server for security audits supporting **publickey authentication**, **session hijacking** and **file manipulation**

.. image:: _static/ssh-mitm-password.png

Introduction
------------

**SSH-MITM** is a man in the middle SSH Server for security audits and malware analysis.

Password and publickey authentication are supported and SSH-MITM is able to detect, if a user is able to
login with publickey authentication on the remote server. This allows SSH-MITM to accept the same key as
the destination server. If publickey authentication is not possible, the authentication will fall
back to password-authentication.

When publickey authentication is possible, a forwarded agent is needed to login to the remote server.
In cases, when no agent was forwarded, SSH-MITM can rediredt the session to a honeypot.

Installation
------------

This part of the documentation covers the installation of SSH-MITM.
The first step to using any software package is getting it properly installed.

To install SSH-MITM, simply run one of those commands in your terminal of choice:

.. tab-set::

    .. tab-item:: Snap

        .. code-block:: bash

            $ sudo snap install ssh-mitm

    .. tab-item:: PIP

        .. code-block:: bash

            $ python -m pip install ssh-mitm

    .. tab-item:: AppImage

        .. code-block:: bash

            $ wget https://github.com/ssh-mitm/ssh-mitm/releases/latest/download/ssh-mitm-x86_64.AppImage
            $ chmod +x ssh-mitm*.AppImage

    .. tab-item:: Nixpkgs

        For Nix or NixOS is a `package <https://search.nixos.org/packages?channel=unstable&show=ssh-mitm&type=packages&query=ssh-mitm>`_
        available. The lastest release is usually present in the ``unstable`` channel.

        .. code-block:: bash

            $ nix-env -iA nixos.ssh-mitm

Start SSH-MITM
--------------

Let’s get started with some simple examples.

Starting an intercepting mitm-ssh server with password authentication is very simple.

All you have to do is run this command in your terminal of choice.

.. code-block:: bash

    $ ssh-mitm server --remote-host 192.168.0.x

Now let's try to connect to the ssh-mitm server.
The ssh-mitm server is listening on port 10022.

.. code-block:: bash

    $ ssh -p 10022 testuser@proxyserver

You will see the credentials in the log output.


.. code-block:: none

    INFO     Remote authentication succeeded
        Remote Address: 192.168.0.x:22
        Username: testuser
        Password: secret
        Agent: no agent


Hijack a SSH terminal session
-----------------------------

Getting the plain text credentials is only half the fun.
SSH-MITM proxy server is able to hijack a ssh session and allows you to interact with it.

Let's get started with hijacking the session.

When a client connects, the ssh-mitm proxy server starts a new server, where you can connect with another ssh client.
This server is used to hijack the session.

.. code-block:: none

    INFO     ℹ created mirrorshell on port 34463. connect with: ssh -p 34463 127.0.0.1

To hijack the session, you can use your favorite ssh client. This connection does not require authentication.

.. code-block:: bash

    $ ssh -p 34463 127.0.0.1

After you are connected, your session will only be updated with new responses, but you are able to execute commands.

Try to execute somme commands in the hijacked session or in the original session.

The output will be shown in both sessions.


Publickey authentication
------------------------

SSH-MITM is able to verify, if a user is able to login with publickey authentication on the remote server.
If publickey authentication is not possible, SSH-MITM falls back to password authentication.
This step does not require a forwarded agent.

For a full login on the remote server agent forwarding is still required. When no agent was forwarded,
SSH-MITM can redirect the connection to a honeypot.

.. code-block:: bash

    $ ssh-mitm server --enable-auth-fallback \
      --fallback-host HONEYPOT \
      --fallback-username HONEYPOT_USER \
      --fallback-password HONEYPOT_PASSWORD


.. toctree::
   :maxdepth: 1
   :hidden:

   get_started/index
   user_guide
   ssh_vulnerabilities
   develop/contributing
