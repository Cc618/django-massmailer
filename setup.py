import os.path
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), "README.md"), "r") as fh:
    long_description = fh.read()

setup(
    name="django-massmailer",
    version='0.1',
    author="Association Prologin",
    author_email="info@prologin.org",
    license="GPL3",
    packages=["massmailer"],
    description=(
        "A standalone Django app to send templated emails in batch. "
        "Features a custom query engine and template editor with preview."
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "bleach",  # HTML sanitizer
        "celery>4",  # task queue
        "django>=2.1",
        "django-bootstrap-breadcrumbs",  # breadcrumbs in default templates
        "django-reversion",  # model revision/history
        "django-crispy-forms",  # form builder compatible with Bootstrap
        "jinja2",  # sane templates
        "Babel",  # i18n template filters
        "markdown",
        "pyparsing",  # query language parser
    ],
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'Topic :: Communications :: Email',
    ],
    project_urls={
        'Source': 'https://github.com/prologin/django-massmailer/',
        'Issue Tracker': 'https://github.com/prologin/django-massmailer/issues',
    },
)
