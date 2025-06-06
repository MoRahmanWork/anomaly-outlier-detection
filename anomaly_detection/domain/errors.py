class KatsError(Exception):
    pass


class DataError(KatsError):
    pass


class DataIrregularGranularityError(DataError):
    pass


class DataInsufficientError(DataError):
    pass


class ParameterError(KatsError):
    pass


class InternalError(KatsError):
    pass