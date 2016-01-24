from setuptools import setup
from distutils import sysconfig
import os
import re
import sys


root_dir = os.path.dirname(__file__)
if root_dir not in sys.path:
    sys.path.insert(0, str(root_dir))
import version


site_packages_path = sysconfig.get_python_lib()
sprem = re.match(
    r'.*(lib[\\/](python\d\.\d[\\/])?site-packages)', site_packages_path, re.I)
rel_site_packages = sprem.group(1)


def collect_files(target, root):
    return [(os.path.join(target, dp), [os.path.join(dp, f)
                                        for f in filenames])
            for dp, dn, filenames in os.walk(root)]


setup(name='pygtk2-win',
      version=version.getVersion(),
      description='Python Gtk-2.0 bindings package for Windows.',
      keywords='',
      author='Christian Fobel',
      author_email='christian@fobel.net',
      url='https://github.com/wheeler-microfluidics/pygtk2-win',
      license='GPL',
      install_requires=['gtk2-win', 'pygio2-win', 'pyglib2-win',
                        'pygobject2-win'],
      data_files=[(rel_site_packages, ['pygtk.py'])] +
      collect_files(os.path.join(rel_site_packages, 'gtk-2.0'), 'gtk'),
      zip_safe=False)
