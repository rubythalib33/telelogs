from setuptools import setup, find_packages

setup(name="telelogs",
    version="0.1.0",
    description="telelogs is a package to send log message on you telegram if \
        something happened on a server, e.g your training is done, update CI/CD and manymore",
    author="Ruby Abdullah",
    author_email='rubyabdullah14@gmail.com',
    url="https://github.com/rubythalib33/telelogs",
    install_requires=[
        'python-dotenv'],
    packages={
        'telelogs': "telelogs",
    },
    python_requires=">=3.8",
    classifiers=[
        'Development Status :: 3 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
    ],)