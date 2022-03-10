# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2022 Scott Shawcroft for Adafruit Industries
#
# SPDX-License-Identifier: MIT
"""
`adafruit_tt21100`
================================================================================

Basic driver for TT21100 touchscreen drivers


* Author(s): Scott Shawcroft

Implementation Notes
--------------------

**Hardware:**

.. todo:: Add links to any specific hardware product page(s), or category page(s).
  Use unordered list & hyperlink rST inline format: "* `Link Text <url>`_"

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://circuitpython.org/downloads

.. todo:: Uncomment or remove the Bus Device and/or the Register library dependencies
  based on the library's use of either.

# * Adafruit's Bus Device library: https://github.com/adafruit/Adafruit_CircuitPython_BusDevice
# * Adafruit's Register library: https://github.com/adafruit/Adafruit_CircuitPython_Register
"""

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_TT21100.git"

import array
import struct
import time

from adafruit_bus_device.i2c_device import I2CDevice

try:
    from typing import List
except ImportError:
    pass

# This is based on: https://github.com/espressif/esp-box/blob/master/components/i2c_devices/touch_panel/tt21100.c

class TT21100:
    """
    A driver for the FocalTech capacitive touch sensor.
    """

    def __init__(self, i2c, address=0x24, irq_pin=None):
        self._i2c = I2CDevice(i2c, address)
        self._irq_pin = irq_pin

        self._bytes = bytearray(28)
        self._data_len = array.array("H", [0])

        # Poll for start up.
        with self._i2c as i2c:
          while self._data_len[0] != 0x0000:
            i2c.readinto(self._data_len)
            time.sleep(0.02)

    @property
    def touched(self) -> int:
        """ Returns the number of touches currently detected """
        with self._i2c as i2c:
          i2c.readinto(self._data_len)
          # Throw away packets that are header only because they don't actually
          # have any touches
          if self._data_len[0] == 7:
            i2c.readinto(self._bytes, end=7)

        if self._data_len[0] == 0:
          return 0
        if self._data_len[0] % 10 == 7:
          return self._data_len[0] // 10

    # pylint: disable=unused-variable
    @property
    def touches(self) -> List[dict]:
        """
        Returns a list of touchpoint dicts, with 'x' and 'y' containing the
        touch coordinates, and 'id' as the touch # for multitouch tracking
        """
        touchpoints = []
        self._bytes[2] = 0
        while self._bytes[2] != 1:
          with self._i2c as i2c:
            i2c.readinto(self._data_len)
            # Empty queue
            if self._data_len[0] == 2:
              return []
            i2c.readinto(self._bytes, end=self._data_len[0])


        ts = struct.unpack_from("xxxHxx", self._bytes)[0]
        for t in range(self._data_len[0] // 10):
            touch_type, touch_id, x, y, pressure = struct.unpack_from("BBHHBxxx", self._bytes, offset=10 * t + 7)
            touch_id = touch_id & 0x1f
            point = {"x": x, "y": y, "id": touch_id}
        # The data is one header called the report followed by touch records.

            # point = {"x": x, "y": y, "id": touch_id}
            # if self._debug:
            #     print("id: {}, x: {}, y: {}".format(touch_id, x, y))
            touchpoints.append(point)
        return touchpoints
