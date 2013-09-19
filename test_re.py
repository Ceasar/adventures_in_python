import re
import sre_constants

from helpers import assert_raises


assert_raises(sre_constants.error, re.sub, "(a)|b", "\\1", "b")
