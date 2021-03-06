"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['pizza.py']
APP_NAME = "PizzaMe"
DATA_FILES = []
OPTIONS = {'argv_emulation': True,
			'iconfile': 'pizza.icns',
			'plist': {
        'CFBundleName': APP_NAME,
        'CFBundleDisplayName': APP_NAME,
        'CFBundleGetInfoString': "Express Pizza Delivery",
        'CFBundleIdentifier': "com.kedardes.osx.pizza",
        'CFBundleVersion': "0.1.0",
        'CFBundleShortVersionString': "0.1.0",
        'NSHumanReadableCopyright': "Copyright 2015 Kedar Deshpande, All Rights Reserved"
    }
			}

setup(
	name=APP_NAME,
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
