# -*- coding: utf-8 -*-
"""
    Copyright (C) 2019 Dag Wieers (@dagwieers) <dag@wieers.com>
    This file implements the Kodi xbmcvfs module, either using stubs or alternative functionality

    SPDX-License-Identifier: GPL-3.0-only
    See LICENSES/GPL-3.0-only.md for more information.
"""
import os
import shutil


def File(path, flags='r'):
    """A reimplementation of the xbmcvfs File() function"""
    try:
        return open(path, flags)
    except IOError:
        from io import StringIO
        return StringIO('')


def Stat(path):
    """A reimplementation of the xbmcvfs Stat() function"""

    class stat:  # pylint: disable=too-few-public-methods
        """A reimplementation of the xbmcvfs stat class"""

        def __init__(self, path):
            """The constructor xbmcvfs stat class"""
            self._stat = os.stat(path)

        def st_mtime(self):
            """The xbmcvfs stat class st_mtime method"""
            return self._stat.st_mtime

    return stat(path)


def copy(source, destination):
    """A reimplementation of the xbmcvfs copy() function"""
    return shutil.copyfile(source, destination)


def delete(path):
    """A reimplementation of the xbmcvfs delete() function"""

    try:
        os.remove(path)
    except OSError:
        pass


def exists(path):
    """A reimplementation of the xbmcvfs exists() function"""
    return os.path.exists(path)


def listdir(path):
    """A reimplementation of the xbmcvfs listdir() function"""
    files = []
    dirs = []
    for f in os.listdir(path):
        if os.path.isfile(f):
            files.append(f)
        if os.path.isdir(f):
            dirs.append(f)
    return dirs, files


def mkdir(path):
    """A reimplementation of the xbmcvfs mkdir() function"""
    return os.mkdir(path)


def mkdirs(path):
    """A reimplementation of the xbmcvfs mkdirs() function"""
    return os.makedirs(path)


def rename(file, newFileName):  # pylint: disable=redefined-builtin
    """A reimplementation of the xbmcvfs rename() function"""
    return os.rename(file, newFileName)


def rmdir(path):
    """A reimplementation of the xbmcvfs rmdir() function"""
    return os.rmdir(path)


def makeLegalFilename(filename):
    """A reimplementation of the xbmc makeLegalFilename() function"""
    return os.path.basename(filename)


def translatePath(path):
    """A stub implementation of the xbmc translatePath() function"""
    if path.startswith('special://home'):
        return path.replace('special://home', os.path.join(os.getcwd(), 'test'))
    if path.startswith('special://profile'):
        return path.replace('special://profile', os.path.join(os.getcwd(), 'tests/usedata'))
    if path.startswith('special://userdata'):
        return path.replace('special://userdata', os.path.join(os.getcwd(), 'tests/userdata'))
    return path
