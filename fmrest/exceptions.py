class FMRestException(Exception):
    """The base fmrest Exception."""

class RequestException(FMRestException):
    """Exception for http request errors

    Re-raised after requests module exception
    """

    def __init__(self, original_exception, request_args, request_kwargs):
        """Parameters
        ----------
        original_exception
            The original exception raised by requests module
        request_args
            Args to the request function
        request_kwargs
            Keyword args to the request function
        """

        self.original_exception = original_exception
        self.request_args = request_args
        self.request_kwargs = request_kwargs
        super().__init__('Request error: {}'.format(original_exception))

class ResponseException(FMRestException):
    """Exception for http response errors

    Re-raised after requests module exception
    """

    def __init__(self, original_exception, response):
        """Parameters
        ----------
        original_exception
            The original exception raised by requests module
        response:
            Response object of requests module
        """
        self.response = response
        super().__init__(
            '{}, {} http response, content-type: {}'.format(
                original_exception,
                response.status_code,
                response.headers.get('content-type', None))
        )

class BadJSON(ResponseException):
    """Invalid json response"""

class FileMakerError(FMRestException):
    """Error raised by FileMaker Data API"""

    def __init__(self, error_code, error_message):
        super().__init__('FileMaker Server returned error {}, {}'.format(error_code, error_message))
