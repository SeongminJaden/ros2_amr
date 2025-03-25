from setuptools import setup

package_name = 'sendbooster_amr'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    py_modules=[],  # You can add Python modules here if needed
    install_requires=['setuptools'],
    zip_safe=True,
    author='Your Name',
    author_email='your_email@example.com',
    description='Description of your package',
    license='License',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # Add your executable scripts here if you have any
        ],
    },
)

