from typing import Any, List, Optional

import pydicom


class PertinentResourcesSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ResourceDescription(self) -> Optional[str]:
        if "ResourceDescription" in self._dataset:
            return self._dataset.ResourceDescription
        return None

    @ResourceDescription.setter
    def ResourceDescription(self, value: Optional[str]):
        if value is None:
            if "ResourceDescription" in self._dataset:
                del self._dataset.ResourceDescription
        else:
            self._dataset.ResourceDescription = value

    @property
    def RetrieveURI(self) -> Optional[str]:
        if "RetrieveURI" in self._dataset:
            return self._dataset.RetrieveURI
        return None

    @RetrieveURI.setter
    def RetrieveURI(self, value: Optional[str]):
        if value is None:
            if "RetrieveURI" in self._dataset:
                del self._dataset.RetrieveURI
        else:
            self._dataset.RetrieveURI = value
