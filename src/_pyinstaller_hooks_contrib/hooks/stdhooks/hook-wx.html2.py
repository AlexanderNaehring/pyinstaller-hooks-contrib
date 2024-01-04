# ------------------------------------------------------------------
# Copyright (c) 2024 PyInstaller Development Team.
#
# This file is distributed under the terms of the GNU General Public
# License (version 2.0 or later).
#
# The full license is available in LICENSE.GPL.txt, distributed with
# this software.
#
# SPDX-License-Identifier: GPL-2.0-or-later
# ------------------------------------------------------------------
from PyInstaller.compat import is_win
from PyInstaller.utils.hooks import collect_dynamic_libs

if is_win:
    binaries = collect_dynamic_libs("wx", destdir=".", search_patterns="WebView2Loader.dll")
