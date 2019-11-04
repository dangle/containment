# -*- coding: utf-8 -*-
"""Contains the init command and helper methods.

Functions:
    init: Initialize the current directory as a project and create the
    contain metasource.
"""

import os.path


_CONFIG_FILE = "containment.json"


def init():
    """
    Usage:
      contain init
    """
    if os.path.isfile(_CONFIG_FILE):
        reinit()
    else:
        clean_init()


def reinit():
    """
    """
    print(
        f"{_CONFIG_FILE} already exists. Would you like to re-initialize your "
        "containment?"
    )


def clean_init():
    """
    """
    print("Initializing containment...")
