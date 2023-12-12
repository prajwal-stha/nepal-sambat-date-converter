BASE_NS_YEAR = 1
BASE_NS_MONTH = 1
BASE_NS_DATE = 1

BASE_AD_YEAR = 880
BASE_AD_MONTH = 10
BASE_AD_DATE = 20

BASE_AD_OFFSET = 293

LEAP_DAYS_LIST = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
DAYS_LIST = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

AD_MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
AD_MONTHS_SHORT = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

NEPALI_DIGITS = ['०', '१', '२', '३', '४', '५', '६', '७', '८', '९']

NEPALI_DAYS = ["आइतबार", "सोमबार", "मंगलबार", "बुधबार", "बिहिबार", "शुक्रबार", "शनिबार"]
ENGLISH_DAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
ENGLISH_DAYS_SHORT = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

from base import arabic_number_to_nepali, NS_MONTHS_NEP, NS_DAYS_IN_MONTH, NS_DAYS_IN_MONTH_LEAP, NS_AD_OFFSET


def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def verify_ns_date(ns_year, ns_month, ns_date):
    if ns_month < 1 or ns_month > 12 or ns_date < 1 or ns_date > 32:
        return False
    if is_leap_year(ns_year):
        return ns_date <= LEAP_DAYS_LIST[ns_month - 1]
    else:
        return ns_date <= DAYS_LIST[ns_month - 1]


def convert_ns_to_ad(ns_year, ns_month, ns_date):
    if not verify_ns_date(ns_year, ns_month, ns_date):
        print("सौ. ने. सं. " + arabic_number_to_nepali(ns_year) + " " + NS_MONTHS_NEP[ns_month - 1] + " मा " + arabic_number_to_nepali(ns_date) + " दिन छैन")
        return

    total_ns_days = 0

    for year in range(BASE_NS_YEAR, ns_year):
        if is_leap_year(year + NS_AD_OFFSET):
            total_ns_days += 366
        else:
            total_ns_days += 365

    for month in range(ns_month - 1):
        if is_leap_year(ns_year + NS_AD_OFFSET):
            total_ns_days += NS_DAYS_IN_MONTH_LEAP[month]
        else:
            total_ns_days += NS_DAYS_IN_MONTH[month]

    total_ns_days += ns_date - 1

    res_ad_year = BASE_AD_YEAR
    res_ad_month = BASE_AD_MONTH
    res_ad_date = BASE_AD_DATE

    while total_ns_days > 0:
        if is_leap_year(res_ad_year):
            if res_ad_date < LEAP_DAYS_LIST[res_ad_month - 1]:
                res_ad_date += 1
                total_ns_days -= 1
            else:
                res_ad_month += 1
                res_ad_date = 0
                if res_ad_month > 12:
                    res_ad_year += 1
                    res_ad_month = 1
        else:
            if res_ad_date < DAYS_LIST[res_ad_month - 1]:
                res_ad_date += 1
                total_ns_days -= 1
            else:
                res_ad_month += 1
                res_ad_date = 0
                if res_ad_month > 12:
                    res_ad_year += 1
                    res_ad_month = 1

    return f"{res_ad_year} {res_ad_month} {res_ad_date}"


def convert_ad_to_ns(ad_year, ad_month, ad_date):
    if ad_year < BASE_AD_YEAR or (ad_year == BASE_AD_YEAR and ad_month < BASE_AD_MONTH) or (ad_year == BASE_AD_YEAR and ad_month == BASE_AD_MONTH and ad_date < BASE_AD_DATE):
        print(f"Supported date range {BASE_AD_YEAR}-{BASE_AD_MONTH}-{BASE_AD_DATE} to 2044-4-15")
        return

    if ad_year > 2044 or (ad_year == 2044 and ad_month > 4) or (ad_year == 2044 and ad_month == 4 and ad_date > 15):
        print(f"Supported date range {BASE_AD_YEAR}-{BASE_AD_MONTH}-{BASE_AD_DATE} to 2044-4-15")
        return

    total_ad_days = 0

    for year in range(BASE_AD_YEAR, ad_year):
        if is_leap_year(year):
            total_ad_days += 366
        else:
            total_ad_days += 365

    for month in range(ad_month - 1):
        if is_leap_year(ad_year):
            total_ad_days += LEAP_DAYS_LIST[month]
        else:
            total_ad_days += DAYS_LIST[month]

    total_ad_days += ad_date - 1
    total_ad_days -= BASE_AD_OFFSET

    res_ns_year = BASE_NS_YEAR
    res_ns_month = BASE_NS_MONTH
    res_ns_date = BASE_NS_DATE

    while total_ad_days > 0:
        if is_leap_year(res_ns_year + NS_AD_OFFSET):
            if res_ns_date < NS_DAYS_IN_MONTH_LEAP[res_ns_month - 1]:
                res_ns_date += 1
                total_ad_days -= 1
            else:
                res_ns_month += 1
                res_ns_date = 0
                if res_ns_month > 12:
                    res_ns_year += 1
                    res_ns_month = 1
        else:
            if res_ns_date < NS_DAYS_IN_MONTH[res_ns_month - 1]:
                res_ns_date += 1
                total_ad_days -= 1
            else:
                res_ns_month += 1
                res_ns_date = 0
                if res_ns_month > 12:
                    res_ns_year += 1
                    res_ns_month = 1

    return f"{res_ns_year} {res_ns_month} {res_ns_date}"