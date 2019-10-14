# -*- coding: utf-8 -*-
"""
Monkey-patching functions
"""
import typing as tp


def patch_pydantic() -> None:
    """Monkey-patch Pydantic package

    In order to use field aliases in Pydantic models with FastAPI we
    need to monkey-patch the 0.32.x version of Pydantic to include the
    ``getter_dict`` configuration option (included in versions 1.0 and
    up).
    """
    import pydantic.main
    import pydantic.version

    if pydantic.version.VERSION.version[0] >= 1:
        return

    @classmethod
    def _decompose_class(
        cls: tp.Type['Model'],
        obj: tp.Any
    ) -> pydantic.main.GetterDict:
        return cls.__config__.getter_dict(obj)

    pydantic.main.BaseConfig.getter_dict = pydantic.main.GetterDict
    pydantic.main.BaseModel._decompose_class = _decompose_class
    return
