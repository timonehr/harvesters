# ----------------------------------------------------------------------------
#
# Copyright 2018 EMVA
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# ----------------------------------------------------------------------------


# Standard library imports
import platform
import re

# Related third party imports

# Local application/library specific imports


def is_running_on_macos():
    """
    Returns a truth value for a proposition: "the program is running on a
    macOS machine".

    :rtype: bool
    """
    pattern = re.compile('darwin', re.IGNORECASE)
    return False if not pattern.search(platform.platform()) else True


def is_running_on_windows():
    """
    Returns a truth value for a proposition: "the program is running on a
    Windows machine".

    :rtype: bool
    """
    pattern = re.compile('windows', re.IGNORECASE)
    return False if not pattern.search(platform.platform()) else True