import numpy as np
from decimal import Decimal, getcontext, ROUND_HALF_UP

getcontext().prec = 6
getcontext().rounding = ROUND_HALF_UP

def format_decimal(val):
    val = Decimal(val).quantize(Decimal("0.01"))
    return f"({val})" if val < 0 else f"{val}"

def jacobi_verbose(coeff_matrix, const_vector, initial_guess, max_iter=2):
    print("Sistem Persamaan Awal:")
    var_names = ['a0', 'a1', 'a2']
    for i in range(len(const_vector)):
        terms = []
        for j in range(len(coeff_matrix[i])):
            coef = coeff_matrix[i][j]
            sign = '+' if coef > 0 and j != 0 else ''
            term = f"{sign}{coef}*{var_names[j]}"
            terms.append(term)
        equation = " ".join(terms)
        print(f"  {equation} = {const_vector[i]}")

    print("\nPersamaan Jacobi:")
    for i in range(len(const_vector)):
        terms = []
        for j in range(len(coeff_matrix[i])):
            if i != j:
                coef = -coeff_matrix[i][j]
                sign = '+' if coef >= 0 else '-'
                term = f" {sign} {abs(coef)}*{var_names[j]}"
                terms.append(term)
        rhs = f"({const_vector[i]}" + "".join(terms) + f") / {coeff_matrix[i][i]}"
        print(f"  {var_names[i]} = {rhs}")

    x_old = [Decimal(str(val)).quantize(Decimal('0.01')) for val in initial_guess]
    const_vector = [Decimal(str(val)) for val in const_vector]
    coeff_matrix = [[Decimal(str(val)) for val in row] for row in coeff_matrix]

    print(f"\nIterasi 0")
    print(f"a0 = {x_old[0]}, a1 = {x_old[1]}, a2 = {x_old[2]}")

    for itr in range(1, max_iter + 1):
        print(f"\nIterasi {itr}")
        x_new = [Decimal('0.00')]*3

        # Hitung a0
        a1, a2 = x_old[1], x_old[2]
        term1 = f"{format_decimal(coeff_matrix[0][1])}*{format_decimal(a1)}"
        term2 = f"{format_decimal(coeff_matrix[0][2])}*{format_decimal(a2)}"
        expr = f"({format_decimal(const_vector[0])} - {term1} - {term2}) / {format_decimal(coeff_matrix[0][0])}"
        a0_new = (const_vector[0] - coeff_matrix[0][1]*a1 - coeff_matrix[0][2]*a2) / coeff_matrix[0][0]
        x_new[0] = a0_new.quantize(Decimal('0.01'))
        print(f"a0 = {expr} = {x_new[0]}")

        # Hitung a1
        a0, a2 = x_old[0], x_old[2]
        term1 = f"{format_decimal(coeff_matrix[1][0])}*{format_decimal(a0)}"
        term2 = f"{format_decimal(coeff_matrix[1][2])}*{format_decimal(a2)}"
        expr = f"({format_decimal(const_vector[1])} - {term1} - {term2}) / {format_decimal(coeff_matrix[1][1])}"
        a1_new = (const_vector[1] - coeff_matrix[1][0]*a0 - coeff_matrix[1][2]*a2) / coeff_matrix[1][1]
        x_new[1] = a1_new.quantize(Decimal('0.01'))
        print(f"a1 = {expr} = {x_new[1]}")

        # Hitung a2
        a0, a1 = x_old[0], x_old[1]
        term1 = f"{format_decimal(coeff_matrix[2][0])}*{format_decimal(a0)}"
        term2 = f"{format_decimal(coeff_matrix[2][1])}*{format_decimal(a1)}"
        expr = f"({format_decimal(const_vector[2])} - {term1} - {term2}) / {format_decimal(coeff_matrix[2][2])}"
        a2_new = (const_vector[2] - coeff_matrix[2][0]*a0 - coeff_matrix[2][1]*a1) / coeff_matrix[2][2]
        x_new[2] = a2_new.quantize(Decimal('0.01'))
        print(f"a2 = {expr} = {x_new[2]}")

        x_old = x_new

A = np.array([
    [2, -3, -4],
    [-3, 9, -2],
    [-5, -1, 3]
], dtype=float)

b = np.array([-44, 78, 21], dtype=float)

initial = [0, 0, 0]

jacobi_verbose(A, b, initial, max_iter=2)