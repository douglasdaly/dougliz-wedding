# -*- coding: utf-8 -*-
"""
Application custom exception classes.
"""
import typing as tp


class APIError(Exception):
    """
    Common API Exception base class.
    """
    pass


class ObjectNotFoundError(APIError):
    """
    Error thrown when an object could not be found.

    Parameters
    ----------
    cls : Union[Type, str]
        The type of object which doesn't exist.
    field_name : str, optional
        The specific field name which generated this error.
    field_value : str, optional
        The specific value of the given `field_name` which doesn't
        exist.

    """

    def __init__(
        self,
        cls: tp.Union[tp.Type, str],
        field_name: tp.Optional[str] = None,
        field_value: tp.Optional[str] = None
    ) -> None:
        cls_name = cls if isinstance(cls, str) else cls.__name__
        msg = f"The requested {cls_name} "
        if field_name:
            if field_value:
                msg += f"with {field_name}={field_value} "
            else:
                msg += f"with the given {field_name} "
        msg += "could not be found."
        return super().__init__(msg)


class ObjectExistsError(APIError):
    """
    Error thrown when an object already exists.

    Parameters
    ----------
    cls : Union[Type, str]
        The type of object which already exists.
    field_name : str, optional
        The specific field name which generated this error.
    field_value : str, optional
        The specific value of the given `field_name` which exists.

    """

    def __init__(
        self,
        cls: tp.Union[tp.Type, str],
        field_name: tp.Optional[str] = None,
        field_value: tp.Optional[str] = None
    ) -> None:
        if not isinstance(cls, str):
            cls = cls.__name__
        msg = f"A {cls} object "
        if field_name:
            msg += "with "
            if field_value:
                msg += f"{field_name}={field_value} "
            else:
                msg += f"the given {field_name} "
        msg += "already exists."
        return super().__init__(msg)


class PrivilegeError(APIError):
    """
    Error thrown when a user doesn't have sufficient privileges.

    Parameters
    ----------
    msg : str, optional
        The error message to display.

    """

    def __init__(self, msg: tp.Optional[str] = None) -> None:
        msg = msg or "Insufficient privileges"
        return super().__init__(msg)
