# FINAL PROJECT PROGRAM KOMPUTASI NUMERIK


### **Anggota kelompok :**

*   Safa Mashita                  (5025241022)
*   Devina Balqis Aurora          (5025241034)
*   Acquirell Kriswanto           (5025241035)
*   Muhammad Quthbi Danish Abqori (5025241036)
*   Via Hana Nurma Putri          (5025241048)
  
### Soal :

Carilah nilai ao, a1, dan a2 dengan menggunakan metoda Jacobi
2𝑎0− 3𝑎1− 4𝑎2=−44
−3𝑎0+ 9𝑎1−2𝑎2=78
−5𝑎0−1𝑎1+3𝑎2=21
[Lakukan iterasi hingga iterasi ke-2. Print semua nilai a0, a1, a2 tiap iterasinya]

### Kode :
```
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
```


# Penjelasan
### Library numpy
```
import numpy as np
from decimal import Decimal, getcontext, ROUND_HALF_UP
```
### Mengatur presisi desimal dan metode pembulatan

```
getcontext().prec = 6
getcontext().rounding = ROUND_HALF_UP
```



### Fungsi untuk memformat angka desimal ke dua digit dengan tanda kurung jika negatif
```
def format_decimal(val):
    val = Decimal(val).quantize(Decimal("0.01"))
    return f"({val})" if val < 0 else f"{val}"
```
### Fungsi utama untuk menjalankan metode Jacobi dengan output rinci
```
def jacobi_verbose(coeff_matrix, const_vector, initial_guess, max_iter=2):
    print("Sistem Persamaan Awal:")
    var_names = ['a0', 'a1', 'a2']
    
    # Menampilkan sistem persamaan awal
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
    # Menampilkan bentuk persamaan Jacobi
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

    # Mengubah semua nilai menjadi Decimal untuk presisi
    x_old = [Decimal(str(val)).quantize(Decimal('0.01')) for val in initial_guess]
    const_vector = [Decimal(str(val)) for val in const_vector]
    coeff_matrix = [[Decimal(str(val)) for val in row] for row in coeff_matrix]

    # Menampilkan nilai awal iterasi
    print(f"\nIterasi 0")
    print(f"a0 = {x_old[0]}, a1 = {x_old[1]}, a2 = {x_old[2]}")

    # Melakukan iterasi Jacobi
    for itr in range(1, max_iter + 1):
        print(f"\nIterasi {itr}")
        x_new = [Decimal('0.00')]*3

        # Menghitung nilai a0
        a1, a2 = x_old[1], x_old[2]
        term1 = f"{format_decimal(coeff_matrix[0][1])}*{format_decimal(a1)}"
        term2 = f"{format_decimal(coeff_matrix[0][2])}*{format_decimal(a2)}"
        expr = f"({format_decimal(const_vector[0])} - {term1} - {term2}) / {format_decimal(coeff_matrix[0][0])}"
        a0_new = (const_vector[0] - coeff_matrix[0][1]*a1 - coeff_matrix[0][2]*a2) / coeff_matrix[0][0]
        x_new[0] = a0_new.quantize(Decimal('0.01'))
        print(f"a0 = {expr} = {x_new[0]}")

        # Menghitung nilai a1
        a0, a2 = x_old[0], x_old[2]
        term1 = f"{format_decimal(coeff_matrix[1][0])}*{format_decimal(a0)}"
        term2 = f"{format_decimal(coeff_matrix[1][2])}*{format_decimal(a2)}"
        expr = f"({format_decimal(const_vector[1])} - {term1} - {term2}) / {format_decimal(coeff_matrix[1][1])}"
        a1_new = (const_vector[1] - coeff_matrix[1][0]*a0 - coeff_matrix[1][2]*a2) / coeff_matrix[1][1]
        x_new[1] = a1_new.quantize(Decimal('0.01'))
        print(f"a1 = {expr} = {x_new[1]}")

        # Menghitung nilai a2
        a0, a1 = x_old[0], x_old[1]
        term1 = f"{format_decimal(coeff_matrix[2][0])}*{format_decimal(a0)}"
        term2 = f"{format_decimal(coeff_matrix[2][1])}*{format_decimal(a1)}"
        expr = f"({format_decimal(const_vector[2])} - {term1} - {term2}) / {format_decimal(coeff_matrix[2][2])}"
        a2_new = (const_vector[2] - coeff_matrix[2][0]*a0 - coeff_matrix[2][1]*a1) / coeff_matrix[2][2]
        x_new[2] = a2_new.quantize(Decimal('0.01'))
        print(f"a2 = {expr} = {x_new[2]}")

        # Update nilai lama untuk iterasi berikutnya
        x_old = x_new
```
### Contoh input: matriks A, vektor b, dan tebakan awal
```
A = np.array([
    [2, -3, -4],
    [-3, 9, -2],
    [-5, -1, 3]
], dtype=float)

b = np.array([-44, 78, 21], dtype=float)

initial = [0, 0, 0]
```
### Menjalankan fungsi Jacobi dengan 2 iterasi
```
jacobi_verbose(A, b, initial, max_iter=2)
```

### Output
```
Sistem Persamaan Awal:
  2.0*a0 -3.0*a1 -4.0*a2 = -44.0
  -3.0*a0 +9.0*a1 -2.0*a2 = 78.0
  -5.0*a0 -1.0*a1 +3.0*a2 = 21.0

Persamaan Jacobi:
  a0 = (-44.0 + 3.0*a1 + 4.0*a2) / 2.0
  a1 = (78.0 + 3.0*a0 + 2.0*a2) / 9.0
  a2 = (21.0 + 5.0*a0 + 1.0*a1) / 3.0

Iterasi 0
a0 = 0.00, a1 = 0.00, a2 = 0.00

Iterasi 1
a0 = ((-44.00) - (-3.00)*0.00 - (-4.00)*0.00) / 2.00 = -22.00
a1 = (78.00 - (-3.00)*0.00 - (-2.00)*0.00) / 9.00 = 8.67
a2 = (21.00 - (-5.00)*0.00 - (-1.00)*0.00) / 3.00 = 7.00

Iterasi 2
a0 = ((-44.00) - (-3.00)*8.67 - (-4.00)*7.00) / 2.00 = 5.01
a1 = (78.00 - (-3.00)*(-22.00) - (-2.00)*7.00) / 9.00 = 2.89
a2 = (21.00 - (-5.00)*(-22.00) - (-1.00)*8.67) / 3.00 = -26.78
```
