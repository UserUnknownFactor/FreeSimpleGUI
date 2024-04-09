import setuptools

def readme():
    try:
        with open('README.md') as f:
            return f.read()
    except:
        return ''

setuptools.setup(
    name="FreeSimpleGUI",
    version="1.0.0",
    author="",
    author_email="",
    description="Python GUIs for Humans.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    keywords="programming library GUI UI UX simple minimalism",
    url="https://github.com/UserUnknownFactor/FreeSimpleGUI",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Topic :: Software Development :: Libraries",
        "Operating System :: OS Independent"
    ),
    entry_points={
        'gui_scripts': [
            'fsgmain=FreeSimpleGUI.FreeSimpleGUI:_main_entry_point' #,
            #'fsgsettings=FreeSimpleGUI.FreeSimpleGUI: main_global_freesimplegui_settings',
        ],},
)