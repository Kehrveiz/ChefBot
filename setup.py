from setuptools import setup, find_packages
from config import *


setup(
    name = __name__,
    version = __version__,
    description = 'Bot de ayuda sobre cocina.',
    long_description = read('README.md'),
    long_description_content_type = "text/markdown",
    author = 'danielangelarro',
    author_email = 'danielangelarro@gmail.com',
    url = 'https://github.com/Kehrveiz/ChefBot',
    scripts = ['run.py'],
    packages = find_packages(),
    keywords = 'telegram bot task-organized',
    install_requires = ['pyTelegramBotAPI'],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Environment :: Console',
        'License :: MIT-LICENSE',
    ]
)