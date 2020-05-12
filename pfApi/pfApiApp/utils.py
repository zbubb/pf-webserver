def getMonthOverviewObject(entrySet):
    returnObj = {}
    returnObj['income'] = 0.0
    returnObj['expenses'] = 0.0
    for monthEntry in entrySet:
        if (monthEntry.isPositive):
            returnObj['income'] += monthEntry.amount
        else:
            returnObj['expenses'] += monthEntry.amount

    returnObj['total'] = returnObj['income'] - returnObj['expenses']
    returnObj['netWorth'] = 0
    return returnObj
