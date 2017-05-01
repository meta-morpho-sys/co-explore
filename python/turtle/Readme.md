# About the turtledemo folder
I copied the turtledemo folder from my Mac laptop's Python library location
(which was /Users/boultoa/anaconda/lib/python3.5/turtledemo).

This contains many demos of the Python 3.5 turtle library.

## To run the main example viewer
There is a viewer application that provides a nice way to select and run any of the demos.  To run this app:

    cd <path of this turtle folder>
    export PYTHONPATH=.
    python3 -m turtledemo

**Note:**  I'm explictly using python3 in the above, to ensure **all** the demos work. If you just use python then the `round_dance` demo fails.

## To run an individual demo file
You can run an individual demo example, e.g. tree.py,  just as a normal python script, as follows:

    cd turtledemo
    python3 tree.py


