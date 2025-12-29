from setuptools import setup, find_packages


HYPEN_E_DOT = '-e .'
def get_requirements(file_path):
    with open(file_path) as file:
        lines = file.readlines()

    cleaned = []
    for req in lines:
        s = req.strip()
        if not s or s.startswith('#'):
            continue
        # Ignore editable installs and pip options or VCS/URL/file entries
        # Keep them in requirements.txt but don't pass to install_requires
        if s.startswith('-e') or s.startswith(('-', '--')) or s.startswith(('git+', 'http:', 'https:', 'file:', 'ssh:', 'svn:', 'hg:', 'bzr:')) or s.startswith(('.', '/')):
            continue
        cleaned.append(s)

    return cleaned

setup(
    name='mlprojects',
    version='0.0.1',
    author='Kishor Kumar Naidu',
    author_email='kishorkumar.theella@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt')
)