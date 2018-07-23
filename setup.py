from setuptools import setup

__VERSION__ = '0.0.1'

setup(
    name='garuda',
    version=__VERSION__,
    description=(
        'Automagically Exposing Djagno ORM over gRPC for microservices'
        ' written in any other languages'),
    long_description='''
Microservices are fun. But what would make them even more fun to work with,
 is if we can avoid duplicating the data layer across your micro-services.
 Django ORM is amazing. Let's share the joy of Django ORM with other languages.
 I have written a tool to automatically expose Django ORM to other languages
 and which can also generate respective client libraries in other languages.
 I heavily rely on Protobuf and gRPC and a lot of AST parsing.
    ''',
    url='https://github.com/dhilipsiva/garuda',
    author='dhilipsiva',
    author_email='dhilipsiva@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Database',
        'Topic :: Database :: Database Engines/Servers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    keywords='django orm grpc protobuf microservice database rpc garuda',
    packages=['garuda'],
    entry_points='',
    install_requires=[
        "django>=2.0",
        "inflect==0.3.1",
        "orm-choices==1.0.0",
        "grpcio==1.13.0",
        "grpcio-tools==1.13.0",
    ],
)
