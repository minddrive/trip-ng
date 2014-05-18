from setuptools import setup

# Let's add this later
# long_description = open('README.txt').read()

# Get version of project
import trip_ng.version


def reqfile_read(fname):
    with open(fname, 'r') as reqfile:
        reqs = reqfile.read()

    return filter(None, reqs.strip().splitlines())


def load_requirements(fname):
    requirements = []

    for req in reqfile_read(fname):
        if 'git+' in req:
            req = '>='.join(req.rsplit('=')[-1].split('-', 3)[:2])
        requirements.append(req)

    return requirements

REQUIREMENTS = dict()
REQUIREMENTS['install'] = load_requirements('requirements.txt')
REQUIREMENTS['tests'] = load_requirements('requirements-tests.txt')

setup_args = dict(
    name='TRipNG',
    version=trip_ng.version.__version__,
    description='Audio CD ripper/encoder application',
    # long_description = long_description,
    author='Kenneth Lareau',
    author_email='elessar@numenor.org',
    license='MIT',
    packages=[
        'trip_ng',
        # 'trip_ng.<something>' if needed
    ],
    install_requires=REQUIREMENTS['install'],
    entry_points={
        'console_scripts': [
            'tds = trip_ng.scripts.trip_ng:main',
        ]
    },
)

if __name__ == '__main__':
    setup(**setup_args)
