from setuptools import setup, find_packages

setup(
    name='ros2_serial_bridge',
    version='0.0.0',
    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/ros2_serial_bridge']),
        ('share/ros2_serial_bridge', ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='your_name',
    maintainer_email='your_email@example.com',
    description='ROS2 Serial Bridge',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'serial_bridge_node = ros2_serial_bridge.ros2_serial_bridge:main',
            'serial_bridge_yaw_node = ros2_serial_bridge.serial_bridge_yaw_node:main',  # 新增
        ],
    },
)
