from ..potential._typing import Numeric

class df:
    """Top-level class for DF classes"""
    def __init__(self, ro: Numeric | None = None, vo: Numeric | None = None) -> None:
        """
        Initialize a DF object.

        Parameters
        ----------
        ro : float or Quantity, optional
            Distance scale for translation into internal units (default from configuration file).
        vo : float or Quantity, optional
            Velocity scale for translation into internal units (default from configuration file).

        Notes
        -----
        - 2016-02-28 - Written - Bovy (UofT)

        """
        ...

    def turn_physical_off(self) -> None:
        """
        Turn off automatic returning of outputs in physical units.

        Notes
        -----
        - 2017-06-05 - Written - Bovy (UofT)

        """
        ...

    def turn_physical_on(
        self, ro: Numeric | bool | None = None, vo: Numeric | bool | None = None
    ) -> None:
        """
        Turn on automatic returning of outputs in physical units.

        Parameters
        ----------
        ro : float or Quantity, optional
            Reference distance (kpc). If False, don't turn it on.
        vo : float or Quantity, optional
            Reference velocity (km/s). If False, don't turn it on.

        Notes
        -----
        - 2016-06-05 - Written - Bovy (UofT)
        - 2020-04-22 - Don't turn on a parameter when it is False - Bovy (UofT)

        """
        ...
