from setuptools import find_packages, setup

package_name = 'fleet_monitoring'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='premsundar',
    maintainer_email='spremsundarsalem@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
    'console_scripts': [
        'battery_node = fleet_monitoring.battery_node:main',
        'temperature_node = fleet_monitoring.temperature_node:main',
        'cpu_node = fleet_monitoring.cpu_node:main',
        'fleet_monitor = fleet_monitoring.fleet_monitor:main',
    ],
},
)
