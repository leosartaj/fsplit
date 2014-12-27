fsplit
******
Split file into small portable chunks.

.. image:: https://travis-ci.org/leosartaj/fsplit.svg
    :target: https://travis-ci.org/leosartaj/fsplit

Installation
============
fsplit can be installed using pip::

    pip install fsplit

Uninstalling
============
fsplit can be uninstalled using pip::

    pip uninstall fsplit

Dependencies
============
fsplit is based on Python 2.7.

Documentation
=============

Splitting files
---------------
fsplit can be used for splitting files::

    fsplit target [options]

Run the following command, for various options::

    fsplit --help 

Joining files split using fsplit
--------------------------------
fsplit provides a utility, **fjoin** for joining files split using fsplit::

    fjoin target [options]

Run the following command, for various options::

    fjoin --help 

Bugs
====
.. |issues| replace:: https://github.com/leosartaj/fsplit/issues

For filing bugs raise an issue at |issues|
