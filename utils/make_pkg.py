#!/bin/python

from shutil import *
from os import *

SCRIPT_DIR = path.dirname(path.realpath(__file__))

ZIP_NAME_NOEXT = path.join(SCRIPT_DIR, "../crx_gallery_pkg")
ZIP_FULL_NAME = ZIP_NAME_NOEXT + ".zip"

PKG_DIR = path.join(SCRIPT_DIR, "../pkg")

def cp(filename_in, target):
	print 'Copying:', filename_in
	target_fullpath = path.join(target, filename_in)
	dirpath, filename = path.split(target_fullpath)
	if not path.exists(dirpath):
		makedirs(dirpath)
	copyfile(filename_in, target_fullpath)

if path.exists(PKG_DIR):
	print 'Removing:', path.split(PKG_DIR)[1]
	rmtree(PKG_DIR)

mkdir(PKG_DIR)
chdir(path.join(SCRIPT_DIR, ".."))

cp("manifest.json", PKG_DIR)
cp("js/nobirthday.js", PKG_DIR)
cp("assets/icon-16.png", PKG_DIR)
cp("assets/icon-48.png", PKG_DIR)
cp("assets/icon-64.png", PKG_DIR)
cp("assets/icon-128.png", PKG_DIR)
cp("assets/icon-256.png", PKG_DIR)

chdir(PKG_DIR)

if path.exists(ZIP_FULL_NAME):
	print 'Removing: ', path.split(ZIP_FULL_NAME)[1]
	unlink(ZIP_FULL_NAME)

print 'Zipping:', path.split(ZIP_NAME_NOEXT)[1]
make_archive(ZIP_NAME_NOEXT, "zip")
