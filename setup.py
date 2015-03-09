from setuptools import setup


setup(
    name='pwgen_xkcd',
    version='1.0',
    url='http://github.com/cburmeister/pwgen_xkcd/',
    license='MIT',
    author='Corey Burmeister',
    author_email='burmeister.corey@gmail.com',
    oescription='',
    py_modules=['pwgen_xkcd'],
    platforms='any',
    install_requires=[
        'click==3.3',
    ],
    entry_points='''
        [console_scripts]
        pwgen_xkcd=pwgen_xkcd:main
    '''
)
