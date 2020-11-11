from setuptools import setup, find_packages

setup(
    name='mrunner',
    version='0.2.9',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['cryptography>=2.2.2', 'PyYAML', 'fabric', 'path.py', 'jinja2', 'six', 'attrs>=17.3', 'click',
                      'docker', 'kubernetes>=5.0.0', 'google-cloud', 'termcolor', 'pyperclip',
                      'cloudpickle', 'neptune-client', 'munch', 'gin-config'],
    entry_points={
        'console_scripts': [
            'mrunner=mrunner.cli.mrunner_cli:cli'
        ],
    },
)
