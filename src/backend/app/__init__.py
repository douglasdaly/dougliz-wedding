# -*- coding: utf-8 -*-
# NOTE: Monkey-patching code *must* run first.
import app.monkey_patch as mp
mp.patch_pydantic()
del mp
