def is_int(input: str) -> bool:
    try:
        casted_value = int(input)
        return True
    except Exception as e:
        return False