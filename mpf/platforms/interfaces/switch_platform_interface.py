"""Interface for switches."""
import abc
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:   # pragma: no cover
    from mpf.core.platform import SwitchConfig


class SwitchPlatformInterface(metaclass=abc.ABCMeta):

    """Interface for switches in hardware platforms.

    SwitchPlatformInterface is an abstract base class that should be overridden for all
    switches interface classes on supported platforms.  This class ensures the proper required
    methods are implemented to support switch operations in MPF.
    """

    def __init__(self, config: "SwitchConfig", number: Any) -> None:
        """Initialise default attributes for switches."""
        self.config = config
        self.number = number
