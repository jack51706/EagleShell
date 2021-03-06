#!/usr/bin/python3

# Imports all the needed variables
from assets.properties import version


# Functions for all the commands that can be executed
def help_list():
    print('''
Core Commands
=============

    Command       Description
    -------       -----------
    ?             Help menu
    help          Help menu
    exit          Exit the console
    quit          Exit the console
    version       Show the framework and console library version numbers

=============
''')


def eagleshell_version():
    print('Framework: ' + version)
    print('Console: ' + version)
