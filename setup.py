from setuptools import setup

setup(
    name='proompt',
    version='0.0.1',
    packages=['proompt'],
    author='Colin Horgan',
    description='A minimal interface to work with a variety of LLMs hosted'
                'via Groq. This is mostly built for my own use, but if you'
                'have ideas or issues feel free to submit a PR or issue on GH',
    entry_points={
        'console_scripts': ['proompt=proompt.main:main'],
    },
    install_requires=[
        "tomli",
        "tomli_w",
        "groq"
    ] 
)

