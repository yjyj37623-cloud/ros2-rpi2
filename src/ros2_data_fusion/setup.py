from setuptools import setup, find_packages

setup(
    name='ros2_data_fusion',
    version='0.0.0',
    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/ros2_data_fusion']),
        ('share/ros2_data_fusion', ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='your_name',
    maintainer_email='your_email@example.com',
    description='ROS2 Data Fusion',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'data_fusion_node = ros2_data_fusion.data_fusion_node:main',
            'data_fusion_yaw_node = ros2_data_fusion.data_fusion_yaw_node:main',  # 新增
        ],
    },
)