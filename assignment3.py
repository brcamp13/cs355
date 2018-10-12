def add_dict(hours_worked):

    return_dict = {'Mon': 0, 'Tue': 0, 'Wed': 0, 'Thu': 0, 'Fri': 0, 'Sat': 0, 'Sun': 0}

    for a, b in hours_worked:
        for c, d in b:
            if c is 'Mon':
                return_dict['Mon'] += 1
            elif c is 'Tue':
                return_dict['Tue'] += 1
            elif c is 'Wed':
                return_dict['Wed'] += 1
            elif c is 'Thu':
                return_dict['Thu'] += 1
            elif c is 'Fri':
                return_dict['Fri'] += 1
            elif c is 'Sat':
                return_dict['Sat'] += 1
            elif c is 'Sun':
                return_dict['Sun'] += 1

    return






