from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'sciroad1'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(),
    
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/sciroad1']),
        ('share/sciroad1', ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yj',
    maintainer_email='yjyj37623@gmail.com',
    description='Turntable control',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            # 这三个全部注册齐全！！！
            'turntable_control_node = sciroad1.turntable_control_node:main',
            'turntable_control_yaw_node = sciroad1.turntable_control_yaw_node:main',
            'test_node = sciroad1.test_node:main',
        ],
    },
)

