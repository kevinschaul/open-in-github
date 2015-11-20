from setuptools import setup

setup(
    name='opengithub',
    version='0.3.4',
    author='Kevin Schaul',
    author_email='kevin.schaul@gmail.com',
    url='http://kevin.schaul.io',
    description='Open your project in GitHub from the command line.',
    long_description='Check out the project on GitHub for the latest information <http://github.com/kevinschaul/open-in-github>',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
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
            'git-open = opengithub.opengithub:main',
        ],
    },
    test_suite = 'test.test_opengithub'
)

