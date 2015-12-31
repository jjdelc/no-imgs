from setuptools import setup

setup(
    name="No Images",
    version="0.1",
    install_requirements=[
        'Flask==0.10.1',
        'Pillow==3.0.0'
    ],
    entry_points={
        'console_scripts': [
            'noimgs=noimgs.main:start'
        ]
    }
)
