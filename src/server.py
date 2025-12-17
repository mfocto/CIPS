import grpc
from concurrent import futures

from generated import vision_pb2_grpc
from src.config.defaults import default_config
from src.config.config_store import ConfigStore
from src.core.registry import PipelineRegistry
from src.services.admin_service import AdminService
from src.services.vision_service import VisionService

def serve(host: str = '[::]', port: int = 50051)-> None :

    config_store = ConfigStore(default_config())

    pipe_registry = PipelineRegistry(pipelines={})

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    vision_pb2_grpc.add_AdminServiceServicer_to_server(
        AdminService(config_store, pipe_registry), server
    )
    vision_pb2_grpc.add_VisionServiceServicer_to_server(
        VisionService(config_store, pipe_registry), server
    )

    bind_addr = f'{host}:{port}'
    server.add_insecure_port(bind_addr)
    server.start()
    print(f"[OK] gRPC server started at {bind_addr}")

    server.wait_for_termination()

if __name__ == "__main__":
    serve()