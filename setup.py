from distutils.core import setup

setup(
    # Application name:
    name="swirling",

    # Version number (initial):
    version="0.0.1",

    # Application author details:
    author="Wangolo Joel",
    author_email="wangoloj@mail.com",

    # Packages
    packages=["swirling"],
    
    package_dir={'swirling':'swirling'},
    # Include additional files into the package
    include_package_data=False,

    # Details
    url="", #"http://pypi.python.org/pypi/MyApplication_v010/",

    #
    license="GPL",
    description="Swirling cyber software client",

    long_description="Swirling is a cyber management software client",

    # Dependent packages (distributions)
    install_requires=[
        "python-wxgtk2.8",
        "configobj",
        "pynotify"
    ],
    
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: GPL",
    ],
)
