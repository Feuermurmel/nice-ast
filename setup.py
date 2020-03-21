import setuptools

name = 'nice-ast'
dependencies = []
dependencies_dev = ['pytest']
console_scripts = ['nice-ast = niceast:entry_point']

setuptools.setup(
    name=name,
    entry_points=dict(console_scripts=console_scripts),
    install_requires=dependencies,
    extras_require={'dev': dependencies_dev},
    setup_requires=['setuptools>=42', 'wheel', 'setuptools_scm[toml]>=3.4'],
    use_scm_version=True,
    packages=setuptools.find_packages(exclude=['tests']))
