NS_MONTHS_ENG = ["Kachhalā", "Thinlā", "Ponhelā", "Sillā", "Chillā", "Chaulā", "Bachhalā", "Tachhalā", "Dillā", "Gunlā", "Yanlā", "Kaulā"]

NS_MONTHS_NEP = ["कछला", "थिंला", "प्वँहेला", "सिल्ला", "चिल्ला", "चौला", "बछला", "तछला", "दिल्ला", "गुँला", "ञला", "कौला"]

NS_MONTHS_NEP_SHORT = ["क.", "थिं.", "प्वँ.", "सि.", "चि.", "चौ.", "ब.", "त.", "दि.", "गुँ.", "ञ.", "कौ."]

NS_DAYS_IN_MONTH = [30, 30, 30, 30, 30, 29, 31, 31, 31, 31, 31, 31]

NS_DAYS_IN_MONTH_LEAP = [30, 30, 30, 30, 30, 30, 31, 31, 31, 31, 31, 31]

NS_DAYS = ["आइतबाः", "सोमबाः", "मङ्लबाः", "बुधबाः", "बिहिबाः", "सुक्रबाः", "सनिबाः"]

NS_AD_OFFSET = 880

NEPALI_DIGITS = ['०', '१', '२', '३', '४', '५', '६', '७', '८', '९']


def is_leap_year(year):
    """
    :param year:
    :return:
    checks whether the given AD year is a leap year or not
    """
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def verify_ns_date(year, month, date):
    """
    verify the given NS date
   :param year: 
   :param month: 
   :param date: 
   :return: 
   """
    try:
        if is_leap_year(year + NS_AD_OFFSET):
            max_date = NS_DAYS_IN_MONTH_LEAP[month - 1]
        else:
            max_date = NS_DAYS_IN_MONTH[month - 1]
    except IndexError:
        return False

    if date <= max_date:
        return True
    return False


def get_last_date_ns(ns_year, ns_month):
    """
    returns last date for given NS year and month
    :param ns_year:
    :param ns_month:
    :return:
    """
    if is_leap_year(ns_year + NS_AD_OFFSET):
        return NS_DAYS_IN_MONTH_LEAP[ns_month - 1]
    else:
        return NS_DAYS_IN_MONTH[ns_month - 1]


def get_total_days_in_ns_month(ns_month, ns_year):
    """
    check how many days in a month
    :param ns_month:
    :param ns_year:
    :return:
    """
    if_year_leap = is_leap_year(ns_year + NS_AD_OFFSET)
    if if_year_leap:
        return NS_DAYS_IN_MONTH_LEAP[ns_month - 1]
    else:
        return NS_DAYS_IN_MONTH[ns_month - 1]


def arabic_number_to_nepali(number):
    """
    :param number:
    :return:
    """
    nepali_number = ""
    for digit in str(number):
        nepali_number += NEPALI_DIGITS[int(digit)]
    return nepali_number
