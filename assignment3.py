def add_dict(hours_worked):

    return_dict = {'Mon': 0, 'Tue': 0, 'Wed': 0, 'Thu': 0, 'Fri': 0, 'Sat': 0, 'Sun': 0}

    for a, b in hours_worked.items():
        for c, d in b.items():
            if c is 'Mon':
                return_dict['Mon'] += d
            elif c is 'Tue':
                return_dict['Tue'] += d
            elif c is 'Wed':
                return_dict['Wed'] += d
            elif c is 'Thu':
                return_dict['Thu'] += d
            elif c is 'Fri':
                return_dict['Fri'] += d
            elif c is 'Sat':
                return_dict['Sat'] += d
            elif c is 'Sun':
                return_dict['Sun'] += d

    return return_dict






