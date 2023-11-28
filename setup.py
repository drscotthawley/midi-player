from setuptools import setup, find_packages

# Read the contents of your README file
with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()


setup(
    name='midi-player',
    version='0.2',
    url='https://github.com/drscotthawley/midi-player',
    project_urls={
        'Source': 'https://github.com/drscotthawley/midi-player',  
        #'Documentation': 'URL_FOR_DOCUMENTATION',  # Optional
    },
    packages=find_packages(),
    # install_requires=[  ], # -- No required packages! 
    # Add additional metadata about your package
    author='Scott H. Hawley',
    author_email='scott.hawley@belmont.edu',
    description='Python launcher of animated MIDI player by @cifkao & @magenta',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
)

