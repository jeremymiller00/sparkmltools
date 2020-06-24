from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

with open('requirements.txt', 'r') as f:
    required = f.read().splitlines()

setup(name='sparkmltools',
      version='0.1.0',
      description='Pyspark Package for Model Evaluation and Diagnosis.',
      author='Jeremy Miller; some functionality borrowed from pytalite by Jinghao Jia, Lun Yu',
      author_email='jeremy.miller@clarivate.com',
      license="MIT",
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/AudaxHealthInc/pytalite/',
      install_requires=required,
      keywords='sparkmltools',
      packages=find_packages(include=['sparkmltools', 'sparkmltools.*']),
      )
