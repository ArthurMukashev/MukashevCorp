from datetime import datetime


def currentYear(request):
    return {
        'lastLastYear': datetime.now().year - 2,
        'lastYear': datetime.now().year - 1,
        'currentYear': datetime.now().year,
        'nextYear': datetime.now().year + 1,
        'nextNextYear': datetime.now().year + 2
    }
