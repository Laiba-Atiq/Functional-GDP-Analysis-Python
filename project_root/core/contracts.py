from typing import Protocol, Any, runtime_checkable, List

@runtime_checkable
class PipelineService(Protocol):
    def execute(self, data: List[Any]) -> None:
        ...    #Ellipsis(the function has no implementation)

@runtime_checkable
class DataSink(Protocol):
    def write(self, records: List[dict]) -> None:
        ...