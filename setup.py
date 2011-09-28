from setuptools import setup, find_packages

version = '0.1'

setup(name='openstack.paste',
      version=version,
      description="Paste template and command for Openstack",
      long_description="""\
Paste template and command for Openstack
""",
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: Apache Software License',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python :: 2.6',
          'Environment :: No Input/Output (Daemon)',
          ],
      keywords='openstack',
      author='OpenStack',
      author_email='openstack@lists.launchpad.net',
      url='http://www.openstack.org/',
      license='Apache Software License',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=['PasteDeploy',
                        'PasteScript',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [paste.global_paster_command]
      openstack = openstack.paste.commands:OpenstackCommand
      [paste.paster_create_template]
      openstack = openstack.paste.templates:OpenstackTemplate
      """,
      )
