#!/usr/bin/python3

"""Unit test for the file storage class

"""

import unittest

import json

import pep8

from io import StringIO

from unittest.mock import patch

from console import HBNBCommand

from models.engine.file_storage import FileStorage

import os
