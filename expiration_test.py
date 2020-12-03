from datetime import date


def check_validity(expiration_date):
    today = str(date.today())

    month = today[5:7]
    year = today[2:4]

    exp_date = expiration_date.split("-")

    exp_month = exp_date[0]
    exp_year = exp_date[1]


    valid = False

    if int(exp_year) == int(year):

        if int(exp_month) > int(month):
            valid = True

        else:
            valid = False

    else:
        valid = True


    return valid


