from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()
setup(
    name='demoscripting',
    version='0.0.1',
    description='demo how to create custon pakage ',
    long_description=readme(),
    long_description_content_type='text/markdowm',
    classifiers=[
        'License :: OSI Approved :: MIT Licenese',
        'Programing Language :: Python :: 3',
        'Operating System :: OS Indipendent'
    ],
    url='https://github.com/manisantoshthaddi/scriptdemo',
    author="Manisantosh Thaddi",
    author_email="mani.thaddi@infor.com",
    license="MIT",
    py_modules=["demoscripting"],
    package_dir={"":"src"},
)