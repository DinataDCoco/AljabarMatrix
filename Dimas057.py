def transpose_vector():
    print("========== Transpose Vector ==========")
    vector = []
    t_vector = []
    vector_tambah = []

    jumlah_nilai = int(input("\nIngin memasukkan berapa nilai? "))
    for i in range(jumlah_nilai):
        input_vector = int(input(f"\nInput nilai ke-{i + 1}: "))
        vector.append(input_vector)
        vector_tambah.append(input_vector)
        t_vector.append(vector_tambah)
        vector_tambah = []

    print("\n========== Hasil ==========")
    print(f"\nvektor awal = {vector}")
    print(f"\nSetelah transpose = {t_vector}")

def transpose_matrix():
    print("========== Transpose Matrix ==========")
    matrix = []
    matrix_transpose = []
    matrix_simpan = []

    baris = int(input("\nmasukkan jumlah baris: "))
    kolom = int(input("masukkan jumlah kolom: "))

    for i in range(baris):
        print("")
        for n in range(kolom):
            nilai_baris = int(input(f"\nnilai baris ke-{i+1}, kolom ke-{n+1}: "))
            matrix_simpan.append(nilai_baris)
        matrix.append(matrix_simpan)
        matrix_simpan = []

    for i in range(baris):
        for n in range(kolom):
            pindah = matrix[n][i]
            matrix_simpan.append(pindah)
        matrix_transpose.append(matrix_simpan)
        matrix_simpan = []
    print("\n========== Hasil ==========")
    print(f"\nMatrix awal = {matrix}")
    print(f"\nSetelah Transpose = {matrix_transpose}")

def tambah_matrix():
    print("========== Penjumlahan Matrix ==========")
    matrix1 = []
    matrix2 = []
    matrix_simpan = []
    matrix_tambah = []

    baris = int(input("\nmasukkan jumlah baris: "))
    kolom = int(input("masukkan jumlah kolom: "))

    for i in range(baris):
        print("")
        print("Matrix ke-1:")
        for n in range(kolom):
            nilai_baris = int(input(f"nilai baris ke-{i+1}, kolom ke-{n+1}: "))
            matrix_simpan.append(nilai_baris)
        matrix1.append(matrix_simpan)
        matrix_simpan = []

    for i in range(baris):
        print("")
        print("Matrix ke-2:")
        for n in range(kolom):
            nilai_baris = int(input(f"nilai baris ke-{i+1}, kolom ke-{n+1}: "))
            matrix_simpan.append(nilai_baris)
        matrix2.append(matrix_simpan)
        matrix_simpan = []

    for i in range(baris):
        for n in range(kolom):
            tambah_matrix = matrix1[i][n] + matrix2[i][n]
            matrix_simpan.append(tambah_matrix)
        matrix_tambah.append(matrix_simpan)
        matrix_simpan = []
    print("\n========== Hasil ==========")
    print(f"\nMatriks ke-1 = {matrix1}")
    print(f"Matriks ke-2 = {matrix2}")
    print(f"\nHasil penjumlaan = {matrix_tambah}")

def kurang_matrix():
    print("========== Pengurangan Matrix ==========")
    matrix1 = []
    matrix2 = []
    matrix_simpan = []
    matrix_tambah = []

    baris = int(input("\nmasukkan jumlah baris: "))
    kolom = int(input("masukkan jumlah kolom: "))

    for i in range(baris):
        print("")
        print("Matrix ke-1:")
        for n in range(kolom):
            nilai_baris = int(input(f"nilai baris ke-{i+1}, kolom ke-{n+1}: "))
            matrix_simpan.append(nilai_baris)
        matrix1.append(matrix_simpan)
        matrix_simpan = []

    for i in range(baris):
        print("")
        print("Matrix ke-2:")
        for n in range(kolom):
            nilai_baris = int(input(f"nilai baris ke-{i+1}, kolom ke-{n+1}: "))
            matrix_simpan.append(nilai_baris)
        matrix2.append(matrix_simpan)
        matrix_simpan = []

    for i in range(baris):
        for n in range(kolom):
            tambah_matrix = matrix1[i][n] - matrix2[i][n]
            matrix_simpan.append(tambah_matrix)
        matrix_tambah.append(matrix_simpan)
        matrix_simpan = []

    print(f"\nMatriks ke-1 = {matrix1}")
    print(f"Matriks ke-2 = {matrix2}")
    print(f"\nHasil penjumlaan = {matrix_tambah}")

def kali_matrix():
    print("========== Perkalian Matrix ==========")
    matrix1 = []
    matrix2 = []
    matrix_simpan = []
    matrix_kali_simpan = []

    baris = int(input("\n Masukkan Jumlah Baris : "))
    kolom = int(input("Masukkan Jumlah Kolom : "))

    for i in range(baris):
            print("")
            print("Matrix ke-1:")
            for n in range(kolom):
                nilai_baris = int(input(f"nilai baris ke-{i+1}, kolom ke-{n+1}: "))
                matrix_simpan.append(nilai_baris)
            matrix1.append(matrix_simpan)
            matrix_simpan = []

    for i in range(baris):
        print("")
        print("Matrix ke-2:")
        for n in range(kolom):
            nilai_baris = int(input(f"nilai baris ke-{i+1}, kolom ke-{n+1}: "))
            matrix_simpan.append(nilai_baris)
        matrix2.append(matrix_simpan)
        matrix_simpan = []
    print(f"\nmatriks 1 : {matrix1}")
    print(f"matriks 2 : {matrix2}")

    for i in range(baris):
        for j in range(kolom):
            total = 0
            for k in range(kolom): 
                total += matrix1[i][k] * matrix2[k][j]
            matrix_simpan.append(total)
        matrix_kali_simpan.append(matrix_simpan)
        matrix_simpan = [] 
    print("\n========== Hasil ==========")
    print(f"\nHasil Perkalian Matriks: {matrix_kali_simpan}")