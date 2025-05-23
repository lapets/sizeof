======
sizeof
======

Simple function for determining the memory usage of common Python values and objects.

|pypi| |readthedocs| |actions| |coveralls|

.. |pypi| image:: https://badge.fury.io/py/sizeof.svg#
   :target: https://badge.fury.io/py/sizeof
   :alt: PyPI version and link.

.. |readthedocs| image:: https://readthedocs.org/projects/sizeof/badge/?version=latest
   :target: https://sizeof.readthedocs.io/en/latest/?badge=latest
   :alt: Read the Docs documentation status.

.. |actions| image:: https://github.com/lapets/sizeof/workflows/lint-test-cover-docs/badge.svg#
   :target: https://github.com/lapets/sizeof/actions/workflows/lint-test-cover-docs.yml
   :alt: GitHub Actions status.

.. |coveralls| image:: https://coveralls.io/repos/github/lapets/sizeof/badge.svg?branch=main
   :target: https://coveralls.io/github/lapets/sizeof?branch=main
   :alt: Coveralls test coverage summary.

Installation and Usage
----------------------
This library is available as a `package on PyPI <https://pypi.org/project/sizeof>`__:

.. code-block:: bash

    python -m pip install sizeof

The library can be imported in the usual ways:

.. code-block:: bash

    import sizeof
    from sizeof import sizeof

Examples
^^^^^^^^

.. |sizeof| replace:: ``sizeof``
.. _sizeof: https://sizeof.readthedocs.io/en/1.0.0/_source/sizeof.html#sizeof.sizeof.sizeof

The |sizeof|_ function can be applied to any value or object. By default, the function returns the memory consumed by that value or object (and **not** by any of the objects to which it may contain references):

.. code-block:: python

    >>> from sizeof import sizeof
    >>> sizeof(123.0123)
    16

.. |arch| replace:: ``arch``
.. _arch: https://sizeof.readthedocs.io/en/1.0.0/_source/sizeof.html#sizeof.sizeof.arch

The amount of memory consumed for any given value or object is in part determined by the host architecture and the version of Python being used. The |arch|_ function can be used to determine whether the architecture is 32-bit or 64-bit:

.. code-block:: python

    >>> from sizeof import arch
    >>> arch()
    32

The optional ``deep`` argument of the |sizeof|_ function makes it possible to calculate the memory consumed by an object and all of it descendants by reference:

.. code-block:: python

    >>> sizeof([]) # Size of an empty list.
    28
    >>> sizeof([1]), sizeof([1, 2]) # Size of reference is 4.
    (32, 36)
    >>> sizeof(3) # Size of an integer.
    14
    >>> sizeof([1, 2, 3]) == 28 + (3 * 4)
    True
    >>> sizeof([1, 2, 3], deep=True) == 28 + (3 * (4 + 14))
    True

Note that all of the examples above may return different results on your system and in your environment.

Development
-----------
All installation and development dependencies are fully specified in ``pyproject.toml``. The ``project.optional-dependencies`` object is used to `specify optional requirements <https://peps.python.org/pep-0621>`__ for various development tasks. This makes it possible to specify additional options (such as ``docs``, ``lint``, and so on) when performing installation using `pip <https://pypi.org/project/pip>`__:

.. code-block:: bash

    python -m pip install ".[docs,lint]"

Documentation
^^^^^^^^^^^^^
The documentation can be generated automatically from the source files using `Sphinx <https://www.sphinx-doc.org>`__:

.. code-block:: bash

    python -m pip install ".[docs]"
    cd docs
    sphinx-apidoc -f -E --templatedir=_templates -o _source .. && make html

Testing and Conventions
^^^^^^^^^^^^^^^^^^^^^^^
All unit tests are executed and their coverage is measured when using `pytest <https://docs.pytest.org>`__ (see the ``pyproject.toml`` file for configuration details):

.. code-block:: bash

    python -m pip install ".[test]"
    python -m pytest

Alternatively, all unit tests are included in the module itself and can be executed using `doctest <https://docs.python.org/3/library/doctest.html>`__:

.. code-block:: bash

    python src/sizeof/sizeof.py -v

Style conventions are enforced using `Pylint <https://pylint.readthedocs.io>`__:

.. code-block:: bash

    python -m pip install ".[lint]"
    python -m pylint src/sizeof

Contributions
^^^^^^^^^^^^^
In order to contribute to the source code, open an issue or submit a pull request on the `GitHub page <https://github.com/lapets/sizeof>`__ for this library.

Versioning
^^^^^^^^^^
The version number format for this library and the changes to the library associated with version number increments conform with `Semantic Versioning 2.0.0 <https://semver.org/#semantic-versioning-200>`__.

Publishing
^^^^^^^^^^
This library can be published as a `package on PyPI <https://pypi.org/project/sizeof>`__ via the GitHub Actions workflow found in ``.github/workflows/build-publish-sign-release.yml`` that follows the `recommendations found in the Python Packaging User Guide <https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/>`__.

Ensure that the correct version number appears in ``pyproject.toml``, and that any links in this README document to the Read the Docs documentation of this package (or its dependencies) have appropriate version numbers. Also ensure that the Read the Docs project for this library has an `automation rule <https://docs.readthedocs.io/en/stable/automation-rules.html>`__ that activates and sets as the default all tagged versions.

To publish the package, create and push a tag for the version being published (replacing ``?.?.?`` with the version number):

.. code-block:: bash

    git tag ?.?.?
    git push origin ?.?.?
