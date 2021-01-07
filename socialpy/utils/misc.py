def list_to_dict(values):
    if not isinstance(values, list):
        return {}
    result = {}
    for raw in values:
        key, value = raw.split('=')
        result[key] = value
    return result
