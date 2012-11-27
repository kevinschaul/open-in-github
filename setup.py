from setuptools import setup

setup(
    name='opengithub',
    version='0.1.1',
    author='Kevin Schaul',
    author_email='kevin.schaul@gmail.com',
    url='http://www.kevinschaul.com',
    description='Open your project in GitHub from the command line.',
    long_description='Check out the project on GitHub for the latest information <http://github.com/kevinschaul/open-in-github>',
    license='MIT',
    classifiers=[
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: Unix',
    'Programming Language :: Python',
    'Topic :: Software Development',
    ],
    packages=[
    'opengithub',
    ],
    entry_points = {
        'console_scripts': [
            'opengithub = opengithub.opengithub:main',
        ],
    },
)

