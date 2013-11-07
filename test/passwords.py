# -*- coding: utf-8 -*-
##
# Copyright 2013 Ghent University
#
# This file is part of vsc-passwords,
# originally created by the HPC team of Ghent University (http://ugent.be/hpc/en),
# with support of Ghent University (http://ugent.be/hpc),
# the Flemish Supercomputer Centre (VSC) (https://vscentrum.be/nl/en),
# the Hercules foundation (http://www.herculesstichting.be/in_English)
# and the Department of Economy, Science and Innovation (EWI) (http://www.ewi-vlaanderen.be/en).
#
# http://github.com/hpcugent/vsc-passwords
#
# vsc-passwords is free software: you can redistribute it and/or modify
# it under the terms of the GNU Library General Public License as
# published by the Free Software Foundation, either version 2 of
# the License, or (at your option) any later version.
#
# vsc-password is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU Library General Public License
# along with vsc-password. If not, see <http://www.gnu.org/licenses/>.
##
"""
Unit tests for vsc-password.

@author: Jens Timmerman (Ghent University)
"""
from unittest import TestCase, TestLoader, main

from vsc.utils import fancylogger


class PasswordTest(TestCase):
    """Tests for passwords"""

    def test_password(self):
        """"Empty Test

        Currently there is only one bin file which is only a couple of lines,
        nothing much to test.
        """
        pass


def suite():
    """ returns all the testcases in this module """
    return TestLoader().loadTestsFromTestCase(PasswordTest)

if __name__ == '__main__':
    """Use this __main__ block to help write and test unittests"""
    main()
