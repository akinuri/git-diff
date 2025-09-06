def input2(
        prompt_text,
        allow_empty = False,
        if_empty_text = "Input can't be empty.",
        validate = None,
        invalid_text = "Input is invalid.",
    ):
    value = input(prompt_text)
    if len(value) == 0:
        print("")
        print(if_empty_text)
        print("")
        value = input2(prompt_text, allow_empty, if_empty_text)
    if validate is not None and callable(validate):
        if validate(value) is False:
            print("")
            print(invalid_text)
            print("")
            value = input2(prompt_text, allow_empty, if_empty_text, validate, invalid_text)
    return value