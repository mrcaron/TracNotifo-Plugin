from setuptools import setup

PACKAGE='TracNotifo'
VERSION='0.1'

setup(name=PACKAGE,
        version=VERSION,
        packages=['notifo'],
        entry_points={'trac.plugins': '%s = notifo' % PACKAGE},
        )
