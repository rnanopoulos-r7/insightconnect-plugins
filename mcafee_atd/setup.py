# GENERATED BY KOMAND SDK - DO NOT EDIT
from setuptools import setup, find_packages


setup(name="mcafee_atd-rapid7-plugin",
      version="1.5.0",
      description="McAfee Advanced Threat Defense provides an API framework for external applications to access core McAfeeATD functions through the REST protocol",
      author="rapid7",
      author_email="",
      url="",
      packages=find_packages(),
      install_requires=['insightconnect-plugin-runtime'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/icon_mcafee_atd']
      )
