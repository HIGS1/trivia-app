class NoResusltsFoundError(Exception):
    """No Results Could not return results. The API doesn't have enough questions for your query. 
    (Ex. Asking for 50 Questions in a Category that only has 20.)
    """
    pass


class InvalidParameterValueError(Exception):
    """ Invalid Parameter Contains an invalid parameter. 
    Arguements passed in aren't valid. (Ex. Amount = Five)
    """
    pass


class RateLimitExceededError(Exception):
    """Rate Limit Too many requests have occurred.
    Each IP can only access the API once every 5 seconds.
    """
    pass


class NoResusltsFoundError(Exception):
    """No Results Could not return results. The API doesn't have
    enough questions for your query. 
    (Ex. Asking for 50 Questions in a Category that only has 20.)
    """
    pass
