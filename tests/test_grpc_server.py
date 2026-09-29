import grpc
import synapse_hft_pb2 as pb2
import synapse_hft_pb2_grpc as pb2_grpc
from src.infrastructure.grpc_server import GrpcServer
from src.application.hft_service import HFTService
from tests.conftest import InMemoryLogger

def test_grpc_server_lifecycle_and_call(telemetry_state):
    logger = InMemoryLogger()
    service = HFTService(logger=logger, telemetry=telemetry_state)

    # Ephemeral port (0 lets OS select a free port)
    server = GrpcServer(
        servicer=service,
        address="127.0.0.1:0",
        logger=logger
    )

    # Start gRPC server
    server.start()
    assert server._is_running is True

    # Idempotency test (calling start again does not fail)
    server.start()

    # Get actual assigned port
    # Since the port was bound to server._server, a real gRPC call can be made
    # Stop the server
    server.stop(grace_period=0.0)
    assert server._is_running is False

    # Idempotency test on stop
    server.stop(grace_period=0.0)

def test_grpc_server_ping_integration(telemetry_state):
    logger = InMemoryLogger()
    service = HFTService(logger=logger, telemetry=telemetry_state)

    # Instantiate server directly to test gRPC communication
    server = GrpcServer(
        servicer=service,
        address="127.0.0.1:54321",
        logger=logger
    )
    server.start()

    try:
        channel = grpc.insecure_channel("127.0.0.1:54321")
        stub = pb2_grpc.HFTLinkStub(channel)

        response = stub.Ping(pb2.Empty(), timeout=2.0)
        assert response.active is True
        assert response.state == "IDLE"
        channel.close()
    finally:
        server.stop(grace_period=0.0)
