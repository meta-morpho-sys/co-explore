# PyCharm Installation

To save you some awkward steps I've downloaded the files you need here:

- pycharm-community-2017.1.3.tar.gz
- jdk-8u131-linux-arm32-vfp-hflt.tar.gz

## Background about the files
Both files are binary files, in a typical unix/linux file format of .tar.gz. These extensions have meanings:

- .gz means gzip format, which is a compressed format manipulated with the GNU zip utilities (`gzip` and `gunzip`)
- .tar means a *tape archive* format, manipulated with the `tar` command.

Since it is common for .tar files to be compressed, the `tar` command actually has support for invoking the GNU zip utility automatically.

The first file contains all the pieces for the PyCharm program. The second file contains an up to date version of the java development kit (JDK) needed by PyCharm. We'll install Java first.

## Installing Java
Install java using the following commands (note that the $ is the command line prompt, don't type it!):

1. Install the jdk8 files into `/opt`:
```
$ sudo tar zxvf jdk-8u131-linux-arm32-vfp-hflt.tar.gz -C /opt
```

2. Make the newly installed javac and java be known to the Debian alternatives system:
```
$ sudo update-alternatives --install /usr/bin/javac /opt/jdk1.8.0_131/bin/javac 1
$ sudo update-alternatives --install /usr/bin/java /opt/jdk1.8.0_131/bin/java 1
```

3. Interactively specify these alternatives to be the default ones:
```
$ sudo update-alternatives --config javac
$ sudo update-alternatives --config java
```
  
  (you will need to respond by choosing the jdk1.8.0_131 options)

4. Verify that this worked, using the -version option to javac and java.
```
$ javac -version
$ java -version
```

   (you should get messages that confirm that javac and java are indeed version 1.8.0_131).

## Installing PyCharm
Now that you have a correct Java installed, you can proceed to install PyCharm, using the following steps:

1. Make a directory to put PyCharm into. I chose `~/apps/pycharm` (note that tilde (`~`) in this context represents the current user's home directory, so it will automatically be interpreted as `/home/pi`):
```
$ mkdir -p ~/apps/pycharm
```

2. Unpack the contents of the .tar.gz file into this folder:
```
$ tar zxvf pycharm-community-2017.1.3.tar.gz -C ~/apps/pycharm
```

3. Launch PyCharm by running pycharm.sh from the bin directory:
```
$ ~/apps/pycharm/bin/pycharm.sh
```

If everything was installed ok, then PyCharm should launch, and prompt you to open a new location. 
