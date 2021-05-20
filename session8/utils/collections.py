def filter_by(collection, key, value):
    return filter(lambda x: x[key] == value, collection)


def unique_keys(collection, key):
    
    keys = []

    for item in collection:
        if not item[key] in keys:   
            keys.append(item[key])
    return keys

    # map(lambda x: keys.append(x[key]), collection)

    # item[key] in keys ? pass : keys.append(x[key])