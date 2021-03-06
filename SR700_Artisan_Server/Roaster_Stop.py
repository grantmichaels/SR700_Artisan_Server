#!/usr/bin/env python
# -*- coding: utf-8 -*-
# SR700-Artisan-PDServer, released under GPLv3
# Roaster Run Recipe

import Pyro4


def main():
    roast_control = Pyro4.Proxy("PYRONAME:roaster.sr700")
    roast_control.disable_temp_manual_mode()
    roast_control.disable_fan_manual_mode()
    roast_control.stop()

if __name__ == '__main__':
    main()
