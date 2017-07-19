# The cinder snap

This repository contains the source code for the cinder snap.

Cinder provides on demand, self-service access to software defined block
storage resources on top of various traditional backend block storage devices.

## Installing this snap

The cinder snap can be installed directly from the snap store:

    sudo snap install --edge cinder

The cinder snap is working towards publication across tracks for
OpenStack releases. The edge channel for each track will contain the tip
of the OpenStack project's master branch, with the beta, candidate and
release channels being reserved for released versions. These three channels
will be used to drive the CI process for validation of snap updates. This
should result in an experience such as:

    sudo snap install --channel=ocata/stable cinder
    sudo snap install --channel=pike/edge cinder

This snap can make use of the Linux SCSI target user-space daemon running on the
host operating system when using the LVM backend. To do this, the tgt package
must be installed:

    sudo apt install tgt

## Configuring cinder

The cinder snap gets its default configuration from the following $SNAP
and $SNAP_COMMON locations:

    /snap/cinder/current/etc/
    └── cinder
        ├── cinder.conf
        └── ...

    /var/snap/cinder/common/etc/
    ├── cinder
    │   └── cinder.conf.d
    │       └── cinder-snap.conf
    ├── nginx
    │   ├── snap
    │   │   ├── nginx.conf
    │   │   └── sites-enabled
    │   │       └── cinder.conf
    └── uwsgi
        └── snap
            └── cinder-api.ini

The cinder applications can be configured in a few ways. The directory
structure can be modified to override config as follows:

The cinder snap supports configuration updates via its $SNAP_COMMON writable
area. The default cinder configuration can be overridden as follows:

    /var/snap/cinder/common/etc/
    ├── cinder
    │   ├── cinder.conf.d
    │   │   ├── cinder-snap.conf
    │   │   ├── database.conf
    │   │   ├── keystone.conf
    │   │   ├── lvm.conf
    │   │   └── rabbitmq.conf
    │   └── cinder.conf
    ├── nginx
    │   ├── snap
    │   │   ├── nginx.conf
    │   │   └── sites-enabled
    │   │       └── cinder.conf
    │   ├── nginx.conf
    │   ├── sites-enabled
    │   │   └── cinder.conf
    └── uwsgi
        ├── snap
        │   └── cinder-api.ini
        └── cinder-api.ini

The cinder configuration can be overridden or augmented by writing
configuration snippets to files in the cinder.conf.d directory.

Alternatively, cinder configuration can be overridden by adding a full
cinder.conf file to the cinder/ directory. If overriding in this way, you'll
need to either point this config file at additional config files located in $SNAP,
or add those to $SNAP_COMMON as well.

The cinder nginx configuration can be overridden by adding an nginx/nginx.conf
and new site config files to the nginx/sites-enabled directory. In this case the
nginx/nginx.conf file would include that sites-enabled directory. If
nginx/nginx.conf exists, nginx/snap/nginx.conf will no longer be used.

The cinder uwsgi configuration can be overridden similarly by adding a
uwsgi/cinder.ini file. If uwsgi/cinder.ini exists, uwsgi/snap/cinder.ini
will no longer be used.

## Logging cinder

The services for the cinder snap will log to its $SNAP_COMMON writable area:
/var/snap/cinder/common/log.

## Restarting cinder services

To restart all cinder services:

    sudo systemctl restart snap.cinder.*

or an individual service can be restarted by dropping the wildcard and
specifying the full service name.

## Building the cinder snap

Simply clone this repository and then install and run snapcraft:

    git clone https://github.com/openstack/snap-cinder
    sudo apt install snapcraft
    cd snap-cinder
    snapcraft

## Support

Please report any bugs related to this snap at:
[Launchpad](https://bugs.launchpad.net/snap-cinder/+filebug).

Alternatively you can find the OpenStack Snap team in `#openstack-snaps` on
Freenode IRC.
