from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='tn.brokerbundle',
      version=version,
      description="",
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='TN Tecnologia e Negocios',
      author_email='ed@tecnologiaenegocios.com.br',
      url='http://www.tecnologiaenegocios.com.br',
      license='GPL',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['tn'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'plone.app.theming',
          'Products.Carousel',
          'Products.Collage',
          'Products.ContentWellPortlets',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
