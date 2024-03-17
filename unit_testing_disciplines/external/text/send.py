from dataclasses import dataclass
import requests


@dataclass(frozen=True)
class SendResult:
    id: str  # The ID for the message
    status: str  # The status of the message (e.g. sent, queued, failed).


def send(
    bearer_token: str, protocol: str, to: str, from_: str, message: str
) -> SendResult:
    result = requests.post(
        "https://t-e-x-t.example.com/send",
        headers={"Authorization": f"Bearer {bearer_token}"},
        data={
            "protocol": protocol,
            "to": to,
            "from": from_,
            "message": message,
        },
    )
    result.raise_for_status()
    response = result.json()
    return SendResult(
        id=response["id"],
        status=response["status"],
    )