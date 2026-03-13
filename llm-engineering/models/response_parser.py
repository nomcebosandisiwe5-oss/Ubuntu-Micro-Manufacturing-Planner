from dataclasses import dataclass

@dataclass
class Response:
    status: str
    data: dict
    error: str = None


def parse_response(response_data: dict) -> Response:
    ":return Response object based on the structure of the input data"
    status = response_data.get('status', 'error')
    data = response_data.get('data', {})
    error = response_data.get('error', None)
    return Response(status=status, data=data, error=error)
