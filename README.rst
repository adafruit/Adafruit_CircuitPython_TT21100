Introduction
============


.. image:: https://readthedocs.org/projects/adafruit-circuitpython-tt21100/badge/?version=latest
    :target: https://docs.circuitpython.org/projects/tt21100/en/latest/
    :alt: Documentation Status


.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord


.. image:: https://github.com/adafruit/Adafruit_CircuitPython_TT21100/workflows/Build%20CI/badge.svg
    :target: https://github.com/adafruit/Adafruit_CircuitPython_TT21100/actions
    :alt: Build Status


.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

Basic driver for TT21100 touchscreen drivers. The ESP32-S3 Box dev board uses it.


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Bus Device <https://github.com/adafruit/Adafruit_CircuitPython_BusDevice>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_
or individual libraries can be installed using
`circup <https://github.com/adafruit/circup>`_.


Installing from PyPI
=====================

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-tt21100/>`_.
To install for current user:

.. code-block:: shell

    pip3 install adafruit-circuitpython-tt21100

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install adafruit-circuitpython-tt21100

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install adafruit-circuitpython-tt21100



Installing to a Connected CircuitPython Device with Circup
==========================================================

Make sure that you have ``circup`` installed in your Python environment.
Install it with the following command if necessary:

.. code-block:: shell

    pip3 install circup

With ``circup`` installed and your CircuitPython device connected use the
following command to install:

.. code-block:: shell

    circup install tt21100

Or the following command to update an existing version:

.. code-block:: shell

    circup update

Usage Example
=============

.. code-block:: python

    import time
    import busio
    import board
    import adafruit_tt21100

    # Create library object (named "tt") using a Bus I2C port
    i2c = busio.I2C(board.SCL, board.SDA)

    tt = adafruit_tt21100.TT21100(i2c)

    while True:
        # if the screen is being touched print the touches
        if tt.touched:
            print(tt.touches)

        time.sleep(0.15)

Documentation
=============
API documentation for this library can be found on `Read the Docs <https://docs.circuitpython.org/projects/tt21100/en/latest/>`_.

For information on building library documentation, please check out
`this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_TT21100/blob/HEAD/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.
