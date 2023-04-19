from setuptools import setup, find_packages

setup(
    name='flaskr',
    version='1.0.0',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)
