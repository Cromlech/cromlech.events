# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages


def text(path):
    with open(path) as f:
        text = f.read()
    return text

version = '0.2.dev0'
readme = text(os.path.join('README.txt'))
history = text(os.path.join('docs', 'HISTORY.txt'))

install_requires = [
    'crom',
    'setuptools',
    'zope.interface',
    'zope.event',
    ]

tests_require = [
    'pytest',
    ]

setup(name='cromlech.events',
      version=version,
      description="Cromlech Web Framework events definitions.",
      long_description="%s\n\n%s" % (readme, history),
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='Cromlech Dolmen Framework',
      author='The Dolmen team',
      author_email='dolmen@list.dolmen-project.org',
      url='http://gitweb.dolmen-project.org/',
      license='ZPL',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      namespace_packages=['cromlech'],
      include_package_data=True,
      zip_safe=False,
      tests_require=tests_require,
      install_requires=install_requires,
      extras_require={'test': tests_require},
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
