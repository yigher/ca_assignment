# Copyright: (c) 2018 CorticAI Pty Ltd, Eugene Tan (eugene@corticai.com)
# All Rights Reserved.
# This file is subject to the terms and conditions defined in
# file 'LICENSE.md', which is part of this source code package.
from setuptools import setup

setup(name='culture_amp_assignment',
      version='0.1',
      description='Culture Amp assignment',
      url='',
      author='eugene',
      author_email='eugene',
      license='',
      packages=['camp_utils', 'camp_data_parser', 'camp_models'],
      install_requires=['keras>=2.3.1', 'numpy>=1.16.2', 'sklearn>=0.0', 'nltk>=3.4.3', 'gensim>=3.7.3'],
      zip_safe=False)