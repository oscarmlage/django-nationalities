from setuptools import setup, find_packages

setup(
    name='django-nationalities',
    version='0.1',
    author='Kapt',
    author_email='dev@kapt.mobi',
    package_dir={'': 'src'},
    packages=find_packages("src",),
    include_package_data=True,
    description='A django field providing nationalities',
    long_description=open('README.rst').read(),
    zip_safe=False,
    install_requires=[
        "Django==1.5.1",
        "South==0.7.6",
    ],
)
