import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid',
    'pyramid_debugtoolbar',
    'waitress',
    'colander',
    'babel'
]

setup(name='you_tee_eff_eight',
      version='0.0',
      description='you_tee_eff_eight',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="you_tee_eff_eight",
      entry_points="""\
      [paste.app_factory]
      main = you_tee_eff_eight:main
      """
    , message_extractors = {'you_tee_eff_eight': [
            ('**.py', 'python', None),
            ('templates/**.mako', 'mako', None),
        ]
    },
)
