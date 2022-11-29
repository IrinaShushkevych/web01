from setuptools import setup, find_namespace_packages

setup(name='power9bot',
      description='Console assistant',
      url='https://github.com/HatsulaSeveryn/Goit_PythonCore_Team9',
      author='GOIT TEAM 9',
      author_email='',
      license='MIT',
      packages=find_namespace_packages(),
      include_package_data=True,
      package_data={'data': ['*.bin']},
      entry_points={'console_scripts': ['power9bot = power9bot.main:main']}
      )