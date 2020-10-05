#!/usr/bin/env python3
# Copyright (C) 2015-2018 Camille Scott
# All rights reserved.
#
# This software may be modified and distributed under the terms
# of the BSD license.  See the LICENSE file for details.

import sys, platform

from setuptools import *

from glob import glob

if sys.version_info < (3, 6):
    print >> sys.stderr, "ERROR: dammit! requires python 3.6 or greater"
    sys.exit()

version = open('dammit/VERSION').read().strip()

def main():
    setup(  name = 'dammit',
            version = version,
            description = 'dammit!',
            url = 'https://github.com/camillescott/dammit',
            author = 'Camille Scott, Tessa Pierce',
            author_email = 'camille.scott.w@gmail.com',
            license = 'BSD',
            test_suite = 'pytest-runner',
            tests_require = ['pytest',
                             'codecov'],
            packages = find_packages(),
            scripts = glob('bin/*'),
            entry_points = {
                'console_scripts': [
                    'dammit=dammit.cli:main'
                ]
            },
            install_requires = ['setuptools',
                                'pandas>=1.0',
                                'khmer>=2.0',
                                'click',
                                'ope>=0.6',
                                'shmlast>=1.6',
                                'snakemake==5.20.1'],
            include_package_data = True,
            zip_safe = False,  )

if __name__ == "__main__":
    main()
