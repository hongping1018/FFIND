# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Image():
    def __init__(self, iid, iname, thumbpath, detailpath, tags, kvals):
        self.iid = iid
        self.iname = iname
        self.thumbpath = thumbpath
        self.detailpath = detailpath
        self.pathpath = "https://omero.app.vumc.org/pathviewer/viewer/" + str(iid)
        self.tags = tags
        self.kvals = kvals

class ImageSet():
    def __init__(self, setname, setlength, imgs):
        self.setname = setname
        self.setlength = setlength
        self.imgs = imgs

class Dataset():
    def __init__(self, did, dsname):
        self.did = did
        self.dsname = dsname

class DatasetImages():
    def __init__(self, dsetname, dsetlength, imgs):
        self.dsetname = dsetname
        self.dsetlength = dsetlength
        self.imgs = imgs
class TagSet():
    def __init__(self, set_name, tags):
        self.set_name = set_name
        self.tags = tags

class Matrix():
    def __init__(self, tag_a, tag_b, matrix):
        self.tag_a = tag_a
        self.tag_b = tag_b
        self.matrix = matrix