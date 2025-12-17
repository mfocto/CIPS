class PipelineRegistry:
    def __init__(self, pipelines: dict):
        self._pipelines = pipelines

    def get(self, pipline_id:str):
        return self._pipelines.get(pipline_id)

    def count(self) -> int:
        return len(self._pipelines)
