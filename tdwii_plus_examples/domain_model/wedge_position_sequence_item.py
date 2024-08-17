from typing import Any, List, Optional  # noqa

import pydicom


class WedgePositionSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def WedgePosition(self) -> Optional[str]:
        if "WedgePosition" in self._dataset:
            return self._dataset.WedgePosition
        return None

    @WedgePosition.setter
    def WedgePosition(self, value: Optional[str]):
        if value is None:
            if "WedgePosition" in self._dataset:
                del self._dataset.WedgePosition
        else:
            self._dataset.WedgePosition = value

    @property
    def ReferencedWedgeNumber(self) -> Optional[int]:
        if "ReferencedWedgeNumber" in self._dataset:
            return self._dataset.ReferencedWedgeNumber
        return None

    @ReferencedWedgeNumber.setter
    def ReferencedWedgeNumber(self, value: Optional[int]):
        if value is None:
            if "ReferencedWedgeNumber" in self._dataset:
                del self._dataset.ReferencedWedgeNumber
        else:
            self._dataset.ReferencedWedgeNumber = value
