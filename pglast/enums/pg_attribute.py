# -*- coding: utf-8 -*-
# :Project:   pglast -- DO NOT EDIT: automatically extracted from pg_attribute.h @ 14-3.0.0-0-g397cbb9
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017-2023 Lele Gaifax
#

from enum import Enum, IntEnum, IntFlag, auto

try:
    from enum import StrEnum
except ImportError:  # pragma: no cover
    # Python < 3.10
    class StrEnum(str, Enum):
        pass



# #define-ed constants

AttributeRelidNameIndexId = 2658

AttributeRelidNumIndexId = 2659

ATTRIBUTE_IDENTITY_ALWAYS = 'a'

ATTRIBUTE_IDENTITY_BY_DEFAULT = 'd'

ATTRIBUTE_GENERATED_STORED = 's'
