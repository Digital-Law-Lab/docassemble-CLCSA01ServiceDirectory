import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.CLCSA01ServiceDirectory',
      version='1.1.1',
      description=('CLCSA Legal Services Directory'),
      long_description='# Community Legal Centres South Australia\r\n\r\n## Legal Services Directory\r\n\r\nThis application asks users a simple set of questions and provides them with a set of legal services tailored to their particular circumstances\r\n\r\n## Authors\r\n\r\n- Jessica Phuong-Rafferty\r\n- Andjela Jovic\r\n- Zahraa Alwan\r\n- Shae Smith\r\n- Mattea Romano',
      long_description_content_type='text/markdown',
      author='Jessica Phuong-Rafferty, Andjela Jovic, Zahraa Alwan, Shae Smith, Mattea Romano',
      author_email='ferr0182@flinders.edu.au',
      license='Copyright (C) 2023 Flinders University All Rights Reserved',
      url='https://flinders.edu.au',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/CLCSA01ServiceDirectory/', package='docassemble.CLCSA01ServiceDirectory'),
     )

