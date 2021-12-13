# def validate(name):
#     if len(name) < 10:
#         raise ValueError

# validate('Joe')


class BaseValidationError(ValueError):
    pass


class NameTooShortError(BaseValidationError):
    pass


class NameTooLongError(BaseValidationError):
    pass


class NameTooCuteError(BaseValidationError):
    pass


def validate(name):
    if len(name) < 10:
        raise NameTooShortError(name)


validate('jon')
# try:
#     validate('jon')
# except BaseValidationError as ex:
#     handle_validation_error(ex)
