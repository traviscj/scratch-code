from setuptools import setup

setup(
    name='scratch',
    version='0.1',
    py_modules=['scratch'],
    install_requires=[
        'arrow',
        'click',
        'pystache',

    ],
    entry_points='''
        [console_scripts]
        scratch=scratch:main
    ''',
    exclude_package_data={'': ['.gitignore'],},
)
