from typing import Any, List, Optional

import pydicom


class TreatmentToleranceViolationAttributeSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def SelectorAttribute(self) -> Optional[int]:
        if "SelectorAttribute" in self._dataset:
            return self._dataset.SelectorAttribute
        return None

    @SelectorAttribute.setter
    def SelectorAttribute(self, value: Optional[int]):
        if value is None:
            if "SelectorAttribute" in self._dataset:
                del self._dataset.SelectorAttribute
        else:
            self._dataset.SelectorAttribute = value

    @property
    def SelectorValueNumber(self) -> Optional[int]:
        if "SelectorValueNumber" in self._dataset:
            return self._dataset.SelectorValueNumber
        return None

    @SelectorValueNumber.setter
    def SelectorValueNumber(self, value: Optional[int]):
        if value is None:
            if "SelectorValueNumber" in self._dataset:
                del self._dataset.SelectorValueNumber
        else:
            self._dataset.SelectorValueNumber = value

    @property
    def SelectorAttributeVR(self) -> Optional[str]:
        if "SelectorAttributeVR" in self._dataset:
            return self._dataset.SelectorAttributeVR
        return None

    @SelectorAttributeVR.setter
    def SelectorAttributeVR(self, value: Optional[str]):
        if value is None:
            if "SelectorAttributeVR" in self._dataset:
                del self._dataset.SelectorAttributeVR
        else:
            self._dataset.SelectorAttributeVR = value

    @property
    def SelectorSequencePointer(self) -> Optional[List[int]]:
        if "SelectorSequencePointer" in self._dataset:
            return self._dataset.SelectorSequencePointer
        return None

    @SelectorSequencePointer.setter
    def SelectorSequencePointer(self, value: Optional[List[int]]):
        if value is None:
            if "SelectorSequencePointer" in self._dataset:
                del self._dataset.SelectorSequencePointer
        else:
            self._dataset.SelectorSequencePointer = value

    @property
    def SelectorSequencePointerPrivateCreator(self) -> Optional[List[str]]:
        if "SelectorSequencePointerPrivateCreator" in self._dataset:
            return self._dataset.SelectorSequencePointerPrivateCreator
        return None

    @SelectorSequencePointerPrivateCreator.setter
    def SelectorSequencePointerPrivateCreator(self, value: Optional[List[str]]):
        if value is None:
            if "SelectorSequencePointerPrivateCreator" in self._dataset:
                del self._dataset.SelectorSequencePointerPrivateCreator
        else:
            self._dataset.SelectorSequencePointerPrivateCreator = value

    @property
    def SelectorAttributePrivateCreator(self) -> Optional[str]:
        if "SelectorAttributePrivateCreator" in self._dataset:
            return self._dataset.SelectorAttributePrivateCreator
        return None

    @SelectorAttributePrivateCreator.setter
    def SelectorAttributePrivateCreator(self, value: Optional[str]):
        if value is None:
            if "SelectorAttributePrivateCreator" in self._dataset:
                del self._dataset.SelectorAttributePrivateCreator
        else:
            self._dataset.SelectorAttributePrivateCreator = value

    @property
    def SelectorSequencePointerItems(self) -> Optional[List[int]]:
        if "SelectorSequencePointerItems" in self._dataset:
            return self._dataset.SelectorSequencePointerItems
        return None

    @SelectorSequencePointerItems.setter
    def SelectorSequencePointerItems(self, value: Optional[List[int]]):
        if value is None:
            if "SelectorSequencePointerItems" in self._dataset:
                del self._dataset.SelectorSequencePointerItems
        else:
            self._dataset.SelectorSequencePointerItems = value

    @property
    def SelectorAttributeName(self) -> Optional[str]:
        if "SelectorAttributeName" in self._dataset:
            return self._dataset.SelectorAttributeName
        return None

    @SelectorAttributeName.setter
    def SelectorAttributeName(self, value: Optional[str]):
        if value is None:
            if "SelectorAttributeName" in self._dataset:
                del self._dataset.SelectorAttributeName
        else:
            self._dataset.SelectorAttributeName = value

    @property
    def SelectorAttributeKeyword(self) -> Optional[str]:
        if "SelectorAttributeKeyword" in self._dataset:
            return self._dataset.SelectorAttributeKeyword
        return None

    @SelectorAttributeKeyword.setter
    def SelectorAttributeKeyword(self, value: Optional[str]):
        if value is None:
            if "SelectorAttributeKeyword" in self._dataset:
                del self._dataset.SelectorAttributeKeyword
        else:
            self._dataset.SelectorAttributeKeyword = value
