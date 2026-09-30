from setuptools import find_packages, setup

package_name = 'physics_operations'

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
    maintainer='host',
    maintainer_email='fabriciocampos@usp.br',
    description='Service em python',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'vector_distance_server_node = physics_operations.vector_distance_server_node:main',
            'vector_distance_client_node = physics_operations.vector_distance_client_node:main',
        ],
    },
)
