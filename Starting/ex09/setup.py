from setuptools import setup, find_packages

setup(
    name='ft_package',
    version='0.0.1',
    packages=find_packages(),
    description='A sample test package',
    url='https://github.com/krastykovyaz/python_4_DS\
/tree/master/Starting/ex09/ft_package',
    author='lnoisome',
    author_email='lnoisome@42.fr',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'console_scripts': [
            'count_in_list=ft_package.module:count_in_list',
        ],
    },
)
