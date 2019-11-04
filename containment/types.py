# -*- coding: utf-8 -*-
"""Contains types used by the contain application.

Types:
    ProjectId: A validation type for project identifiers.
"""

import typet.validation


ProjectId = typet.validation.Length[str, 1:]
