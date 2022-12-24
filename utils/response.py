def prepare_create_success_response(message):
    """ prepare success response for all serializer """
    response = {
        'status': True,
        'message': message
    }
    return response


def prepare_success_response(message):
    """ prepare success response for all serializer """
    response = {
        'status': True,
        'message': message
    }
    return response


def prepare_success_list_response(message, data):
    """ prepare success response for all serializer """
    response = {
        'status': True,
        'message': message,
        'data': data
    }
    return response


def prepare_error_response(serializer_error):
    """ prepare error response for all serializer """
    response = {
        'status': False,
        'message': serializer_error,
    }
    return response


def prepare_generic_error(error_code, details):
    """
    method for build generic error
    @param error_code: error_code should be provided by this param
    @param details: error message
    :return:
    """
    response = {
        'status': False,
        "message": details,
        "data": None
    }
    return response
