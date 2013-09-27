# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
import os
import re
from setuptools import setup, find_packages
from setuptools.command.easy_install import easy_install as _easy_install
## See http://docs.python.org/distutils/setupscript.html ##


logging.basicConfig()
log = logging.getLogger('stnb.setup')
log.setLevel(logging.INFO)

COMMENT = re.compile(r'(^|\s+)\#.*$')


VCS_REQUIREMENT = \
    re.compile(r'^(?P<editable>-e )?(?P<link>(?P<vcs>git|svn|hg|bzr)\+\w+://'
               r'.+#egg=(?P<package>'
               r'.+?)(-(?P<version>\d[\.\w]*))?)$')
STD_REQUIREMENT = re.compile(r'^(-e )?(?P<package>[-\w]*)'
                             r'((?P<version_match>[<>=\!]{2})'
                             r'(?P<version>[-\w\.]+))?$')
LINK_REQUIREMENT = \
    re.compile(r'^(-e )?(?P<link>\w+://.+#egg=(?P<package>'
               r'.+?)(-(?P<version>\d[\.\w]*))?)$')

pip_installs = []
install_requires = []
dependency_links = []

for requirement in (l.strip() for l in
            open(os.path.join(os.path.dirname(__file__), 'requirements.txt'))):
    requirement = COMMENT.sub('', requirement)
    if not requirement:
        continue
    vcs_match = VCS_REQUIREMENT.match(requirement)
    link_match = LINK_REQUIREMENT.match(requirement)
    std_match = STD_REQUIREMENT.match(requirement)
    if link_match:
        if link_match.groupdict().get('version', None) is not None:
            package = '{package}=={version}'.format(**link_match.groupdict())
            link = link_match.group('link')
        else:
            package = '{package}>=0'.format(**link_match.groupdict())
            link = '{link}-0'.format(link=link_match.group('link'))
        install_requires.append(bytes(package))
        dependency_links.append(bytes(link))
    elif vcs_match:
        link = vcs_match.group('link')
        if vcs_match.groupdict().get('version', None) is not None:
            package = '{package}=={version}'.format(**vcs_match.groupdict())
        else:
            package = '{package}'.format(**vcs_match.groupdict())
        pip_installs.append(bytes(link))
    elif std_match:
        if std_match.groupdict().get('version', None) is not None:
            frmt = std_match.groupdict()
            frmt.setdefault('version_match', '==')
            package = '{package}{version_match}{version}'.format(**frmt)
        else:
            package = std_match.groupdict().get('package')
        install_requires.append(bytes(package))
    else:
        log.error('{requirement} is not a valid requirement'
                  .format(requirement=requirement))

if pip_installs:
    log.info('setup.py can\'t install requirements:\n    {0}\n'
             'You should use pip to install these seperately.'
             .format('\n    '.join(pip_installs)))


class easy_install(_easy_install):

    def run(self):
        try:
            import pip
            log.info('pip installer found, attempting pip install...')
            pip.main(['install'] + pip_installs)
        except:
            pass
        _easy_install.run(self)


version = re.search("__version__\s*=\s*'(.*)'",
                    open('digital/__init__.py').read(), re.M).group(1)
setup(
    name='stnb',
    version=version,
    description='STNB Web',
    author='Hayden Stainsby',
    author_email='hds@mat.uab.cat',
    maintainer='Hayden Stainsby',
    maintainer_email='hds@mat.uab.cat',
    url='http://stnb.tk/',
    download_url='git+ssh://git@github.com:hds/stnb.git',
    include_package_data=True,
    packages=find_packages(),
    setup_requires=['pip'],
    install_requires=install_requires,
    dependency_links=dependency_links,
    cmdclass={'easy_install': easy_install},
)
