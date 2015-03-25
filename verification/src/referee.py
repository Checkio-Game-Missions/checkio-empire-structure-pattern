from checkio_referee import RefereeBase, representations


import settings_env
from tests import TESTS

cover = """def cover(f, data):
    if len(data) <= 2:
        return f(d[0], str(d[1]))
    else:
        return f(d[0], str(d[1]), d[2])
"""


class Referee(RefereeBase):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "check_structure"
    ENV_COVERCODE = {
        "python_2": cover,
        "python_3": cover,
        "javascript": None
    }
    CALLED_REPRESENTATIONS = {
        "python_2": representations.unwrap_arg_representation,
        "python_3": representations.unwrap_arg_representation,
        "javascript": representations.unwrap_arg_representation,
    }
