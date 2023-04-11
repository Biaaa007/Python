def validate_cnp(cnp):
    # Verifica daca sirul are 13 caractere
    if not cnp.isdigit() or len(cnp) != 13:
        return False

    # Sexul si secolul (S)
    gender = int(cnp[0])
    century = int(cnp[0]) // 2

    # Anul nasterii, luna si ziua
    birth_year = int(cnp[1:3])
    birth_month = int(cnp[3:5])
    birth_day = int(cnp[5:7])

    # Anul nasterii pentru rezidenti si straini
    if century in [1, 2, 5, 6]:
        birth_year += century * 100
    else:
        birth_year += (century - 1) * 100

    # Verific daca data de nastere e valida
    if not (1 <= birth_month <= 12):
        return False

    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if birth_year % 4 == 0 and (birth_year % 100 != 0 or birth_year % 400 == 0):
        days_in_month[1] = 29

    if not (1 <= birth_day <= days_in_month[birth_month - 1]):
        return False

    # Verific codul de judet
    county_code = int(cnp[7:9])
    if not (1 <= county_code <= 52 or 41 <= county_code <= 46):
        return False

    # Verific cifra de control
    control_sum = sum(int(cnp[i]) * int('279146358279'[i]) for i in range(12))
    control_digit = (control_sum % 11) % 10
    if control_digit != int(cnp[12]):
        return False

    # Daca toate cele de mai sus sunt bifate, CNP-ul este valid
    return True

cnp_list = ['1001221122119', '6000430297288']

for cnp in cnp_list:
    if validate_cnp(cnp):
        print(f'CNP-ul {cnp} este valid.')
    else:
        print(f'CNP-ul {cnp} nu este valid.')