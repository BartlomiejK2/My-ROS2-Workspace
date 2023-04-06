from setuptools import setup

package_name = 'py_1_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='bartek',
    maintainer_email='bartek@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
         "py_node = py_1_pkg.my_first_node:main",
         "robot_news_station = py_1_pkg.robot_news_station:main",
         "robot_news_receiver = py_1_pkg.robot_news_receiver:main",
         "number_publisher = py_1_pkg.number_publisher:main",
         "number_counter = py_1_pkg.number_counter:main",
         "add_two_ints_server = py_1_pkg.add_two_int_server:main",
         "add_two_ints_client = py_1_pkg.add_two_int_client:main",
         "led_panel_node = py_1_pkg.led_panel_node:main",
         "battery_node = py_1_pkg.battery_node:main"

        ],
    },
)
