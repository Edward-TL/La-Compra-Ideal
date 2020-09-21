def ordered_dict(dictionary, reverse=True):
    import operator
    ordered_dict = dict(sorted(dictionary.items(), key=operator.itemgetter(1),reverse=True))

    return ordered_dict