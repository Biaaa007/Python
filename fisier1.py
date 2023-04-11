def validate_cnp(cnp):
    if len(cnp) != 13 or not cnp.isdigit():
        return False

    sex_century = int(cnp[0])
    year = int(cnp[1:3])
    month = int(cnp[3:5])
    day = int(cnp[5:7])
    county = int(cnp[7:9])
    order = int(cnp[9:12])
    control = int(cnp[12])

    # validate sex and century
    if sex_century not in (1, 2, 3, 4, 5, 6, 7, 8, 9):
        return False
    if sex_century in (7, 8, 9):
        year += 1900
    else:
        if sex_century in (3, 4):
            year += 1800
        else:
            year += 2000
    if sex_century % 2 == 0:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month < 1 or month > 12 or day < 1 or day > days_in_month[month - 1]:
            return False
    else:
        if month < 1 or month > 12 or day < 1 or day > 31:
            return False

    # validate county
    if county < 1 or (county > 46 and county != 51 and county != 52):
        return False

    # validate order
    if order < 1 or order > 999:
        return False

    # validate control digit
    factors = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]
    checksum = sum([int(cnp[i]) * factors[i] for i in range(12)]) % 11
    expected_control = 1 if checksum == 10 else checksum
    if control != expected_control:
        return False

    return True
