import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()


setup(
    name='sphinx-links',
    version='0.0.7',
    description='Added external links to Sphinx project as :l:`name of link`.',
    long_description=README,
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Programming Language :: Python",
        "License :: Repoze Public License",
        "Topic :: Internet",
        "Topic :: Software Development :: Documentation",
    ],
    keywords='sphinx documentation',
    author="uralbash",
    author_email="sacrud@uralbash.ru",
    url="https://github.com/ITCase/sphinx-links",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
