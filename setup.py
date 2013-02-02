from setuptools import setup, find_packages

print find_packages()

desc = '''Allows run commands in bunch of django apps
deployed in the same manner in common folder.'''

setup(
    name='django-projectgroup-command-runner',
    version='0.1',
    description=desc,
    author='Vaclav Klecanda',
    author_email='vencax77@gmail.com',
    url='https://github.com/vencax/django-projectgroup-command-runner',
    packages=find_packages(),
    install_requires=[
        'git+git://github.com/vencax/django-projectgroup-settings-iterator.git'
    ],
    include_package_data=True,
)
