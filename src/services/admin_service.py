import grpc
from generated import vision_pb2, vision_pb2_grpc
from src.config.validation import validate_config

class AdminService(vision_pb2_grpc.AdminServiceServicer):
    def __init__(self, config_store, pipeline_registry):
        self._config_store = config_store
        self._pipeline_registry = pipeline_registry

    def HealthCheck(self, request, context):
        # 1. pipeline 존재 확인
        if self._pipline_registry.count() <= 0:
            return vision_pb2.HealthCheckResponse(
                healthy=False,
                message='NOT_READY: no pipelines registered'
            )

        # 2. config 유효성 확인
        cfg = self._config_store.get_snapshot()
        ok, reason = validate_config(cfg)

        if not ok:
            return vision_pb2.HealthCheckResponse(
                healthy=False,
                message=f'NOT_READY: {reason}'
            )

        return vision_pb2.HealthCheckResponse(
            healthy=True,
            message="SERVING"
        )

    def GetConfig(self, request, context):
        cfg = self._config_store.get_snapshot()
        return vision_pb2.GetConfigResponse(config=cfg)

    def UpdateConfig(self, request, context):
        new_cfg = request.config
        ok, reason = validate_config(new_cfg)
        if not ok:
            return vision_pb2.UpdateConfigResponse(success=False)

        self._config_store.set(new_cfg)
        return vision_pb2.UpdateConfigResponse(success=True)
