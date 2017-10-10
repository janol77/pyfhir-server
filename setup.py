from setuptools import find_packages, setup

setup(name="pyfhir-server",
      version = "0.1",
      description = "Servidor Fhir usando Python y Mongo",
      author = "Alejandro Medina",
      platforms = ["any"],
      license = "GPLv3",
      include_package_data=True,
      packages = find_packages(),
      install_requires = ["Flask==0.12.2",
      					  "Flask-RESTful==0.3.6"],
)
