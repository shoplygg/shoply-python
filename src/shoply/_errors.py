from typing import Any, Dict, Optional


class ShoplyError(Exception):
    """A request Shoply refused, or one that never got an answer.

    `status` is the HTTP status (0 when nothing answered), `code` the word that does not change
    (`not_found`, `missing_scope`, `validation_failed`, `rate_limited`... and `connection_error`
    or `timeout` when nothing answered), `errors` what is wrong with each field for
    `validation_failed`, `request_id` what to quote to Shoply about it, `retry_after` the seconds
    to wait when told to slow down, and `body` the whole answer.
    """

    def __init__(
        self,
        message: str,
        *,
        status: int = 0,
        code: Optional[str] = None,
        errors: Optional[Dict[str, str]] = None,
        request_id: Optional[str] = None,
        retry_after: Optional[int] = None,
        body: Any = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.status = status
        self.code = code
        self.errors = errors
        self.request_id = request_id
        self.retry_after = retry_after
        self.body = body
