BASE_BS_YEAR = 1975
BASE_BS_MONTH = 1
BASE_BS_DATE = 1

BASE_AD_YEAR_FOR_BS = 1918
BASE_AD_MONTH_FOR_BS = 4
BASE_AD_DATE_FOR_BS = 13

BASE_AD_OFFSET_FOR_BS = 102

BS_MONTHS = ["Baisakh", "Jestha", "Ashad", "Shrawan", "Bhadra", "Ashwin", "Kartik", "Mangsir", "Poush", "Magh",
             "Falgun", "Chaitra"]

from base import is_leap_year, arabic_number_to_nepali
from ns_to_bs import BS_CALENDAR_DATA, BS_MONTHS_NEP
from ns_to_ad import LEAP_DAYS_LIST, DAYS_LIST


def verify_bs_date(year, month, date):
    """
    Verify given Nepali date
    :param year:
    :param month:
    :param date:
    :return:
    """
    try:
        max_date = BS_CALENDAR_DATA[year][month - 1]
    except IndexError:
        return False

    if date <= max_date:
        return True
    return False


def convert_bs_to_ad(bs_year, bs_month, bs_date, message):
    """
    This function converts BS date to AD
    :param bs_year:
    :param bs_month:
    :param bs_date:
    :param message:
    :return:
    """

    is_valid_date = verify_bs_date(bs_year, bs_month, bs_date)
    if not is_valid_date:
        if message == "":
            print(f"{arabic_number_to_nepali(bs_year)} {BS_MONTHS_NEP[bs_month - 1]} मा {arabic_number_to_nepali(bs_date)} दिन छैन")
        else:
            print("BS Range Invalid. Valid Range: [1975 - 2100]")
        return

    total_bs_days = 0
    year = BASE_BS_YEAR

    # Using num of days in given year (last element of value in BS_CALENDAR_DATA)
    while year < bs_year:
        total_bs_days += BS_CALENDAR_DATA[year][12]
        year += 1

    for month in range(bs_month - 1):
        total_bs_days += BS_CALENDAR_DATA[year][month]

    total_bs_days += bs_date - 1

    res_ad_year = BASE_AD_YEAR_FOR_BS
    res_ad_month = BASE_AD_MONTH_FOR_BS
    res_ad_date = BASE_AD_DATE_FOR_BS

    while total_bs_days > 0:
        if is_leap_year(res_ad_year):
            if res_ad_date < LEAP_DAYS_LIST[res_ad_month - 1]:
                res_ad_date += 1
                total_bs_days -= 1
            else:
                res_ad_month += 1
                res_ad_date = 0
                if res_ad_month > 12:
                    res_ad_year += 1
                    res_ad_month = 1
        else:
            if res_ad_date < DAYS_LIST[res_ad_month - 1]:
                res_ad_date += 1
                total_bs_days -= 1
            else:
                res_ad_month += 1
                res_ad_date = 0
                if res_ad_month > 12:
                    res_ad_year += 1
                    res_ad_month = 1

    return res_ad_year, res_ad_month, res_ad_date


def convert_ad_to_bs(ad_year, ad_month, ad_date):
    """
    This function converts AD date to BS
    :param ad_year:
    :param ad_month:
    :param ad_date:
    :return:
    """
    if (
        ad_year < BASE_AD_YEAR_FOR_BS
        or ad_year == BASE_AD_YEAR_FOR_BS and ad_month < BASE_AD_MONTH_FOR_BS
        or ad_year == BASE_AD_YEAR_FOR_BS and ad_month == BASE_AD_MONTH_FOR_BS and ad_date < BASE_AD_DATE_FOR_BS
    ):
        print(f"Supported date range {BASE_AD_YEAR_FOR_BS}-{BASE_AD_MONTH_FOR_BS}-{BASE_AD_DATE_FOR_BS} to 2044-4-15")
        return

    if (
        ad_year > 2044
        or ad_year == 2044 and ad_month > 4
        or ad_year == 2044 and ad_month == 4 and ad_date > 15
    ):
        print(f"Supported date range {BASE_AD_YEAR_FOR_BS}-{BASE_AD_MONTH_FOR_BS}-{BASE_AD_DATE_FOR_BS} to 2044-4-15")
        return

    total_ad_days = 0

    for year in range(BASE_AD_YEAR_FOR_BS, ad_year):
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
    total_ad_days -= BASE_AD_OFFSET_FOR_BS

    res_bs_year = BASE_BS_YEAR
    res_bs_month = BASE_BS_MONTH
    res_bs_date = BASE_BS_DATE

    while total_ad_days > 0:
        if res_bs_date < BS_CALENDAR_DATA[res_bs_year][res_bs_month - 1]:
            res_bs_date += 1
            total_ad_days -= 1
        else:
            res_bs_month += 1
            res_bs_date = 0
            if res_bs_month > 12:
                res_bs_year += 1
                res_bs_month = 1

    return res_bs_year, res_bs_month, res_bs_date

