# -*- coding: utf-8 -*-
"""
CRUD repository for configuration settings.
"""
from abc import ABCMeta
from abc import abstractmethod
import typing as tp

from app.crud.base import Repository
from app.crud.base import T
from app.models.config.setting import DataT
from app.models.config.setting import SettingCreate
from app.models.config.setting import SettingUpdate


class SettingRepository(
    Repository[T, SettingCreate, SettingUpdate],
    metaclass=ABCMeta
):
    """
    Configuration setting object repository base class.
    """

    @abstractmethod
    def get_by_name(self, name: str, *, raise_ex: bool = False) -> T:
        """Gets a setting from the name given.

        Parameters
        ----------
        name : str
            The name of the setting to get.
        raise_ex : bool, optional
            Whether or not to raise an exception if the setting is not
            found (default is ``False``).

        Returns
        -------
        T
            The setting object with the `name` given.

        Raises
        ------
        ObjectNotFoundError
            If the setting with the specified `name` couldn't be found
            and `raise_ex` is set to ``True``.

        """
        pass

    def update_value(
        self,
        name: str,
        value: tp.Optional[DataT],
        *,
        raise_ex: bool = True
    ) -> T:
        """Updates a setting from the `name` given.

        Parameters
        ----------
        name : str
            The name of the setting to update.
        value : Optional[DataT]
            The new value to use for the setting.
        raise_ex : bool, optional
            Whether or not to raise an exception if the setting with the
            given `name` is not found (default is ``True``).

        Returns
        -------
        T
            The updated setting object.

        Raises
        ------
        ObjectNotFoundError
            If the setting with the specified `name` couldn't be found
            and `raise_ex` is set to ``True``.

        """
        current = self.get_by_name(name, raise_ex=raise_ex)
        current.value = value
        return current
