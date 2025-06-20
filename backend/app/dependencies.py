from .services import DroneService, PlyService, RecordService, StreamService

_record_service = RecordService()
_drone_service: DroneService | None = None
_stream_service: StreamService | None = None
_ply_service = PlyService()

def get_drone_service():
    global _drone_service  # noqa: PLW0603
    if _drone_service is None:
        _drone_service = DroneService(_record_service)
    return _drone_service


def get_stream_service():
    global _stream_service  # noqa: PLW0603
    if _stream_service is None:
        _stream_service = StreamService(get_drone_service(), _record_service)
    return _stream_service
