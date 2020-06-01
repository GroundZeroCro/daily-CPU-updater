from src.utils.EnvironmentType import EnvironmentType


def constant(f):
    def temp_set(self, value):
        raise TypeError

    def temp_get(self):
        return f(self)

    return property(temp_get, temp_set)


class _ConstStaging:
    @constant
    def THOUGHT_COLLECTION_HR(self):
        return "hr-thoughts-staging"

    @constant
    def THOUGHT_COLLECTION_EN(self):
        return "en-thoughts-staging"


class _ConstProduction:
    @constant
    def THOUGHT_COLLECTION_HR(self):
        return "hr-thoughts"

    @constant
    def THOUGHT_COLLECTION_EN(self):
        return "en-thoughts"


class Environment(object):
    environment_type = EnvironmentType.STAGING

    @classmethod
    def set_environment(cls, environment_type):
        cls.environment_type = environment_type

    @classmethod
    def get(cls):
        if cls.environment_type == EnvironmentType.STAGING:
            return _ConstStaging()
        else:
            return _ConstProduction()
