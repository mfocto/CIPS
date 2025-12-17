from generated import vision_pb2, vision_pb2_grpc

class VisionService(vision_pb2_grpc.VisionServiceServicer):
    def __init__(self, config_store, pipeline_registry):
        self.config_store = config_store
        self.pipeline_registry = pipeline_registry

    def AnalyzeImage(self, request, context):
        # TODO: decoder/preprocessor/pipeline.run 붙이기
        return vision_pb2.AnalizeImageResponse (
            result = vision_pb2.AnalyzeResult(
                detections=[],
                metrics={},
                processing_ms=0
            )
        )

    def StreamAnalyze(self, request_iterator, context):
        for req in request_iterator:
            yield vision_pb2.StreamAnalyzeResponse(
                result=vision_pb2.AnalyzeResult(
                    detections=[],
                    metrics={},
                    processing_ms=0
                )
            )