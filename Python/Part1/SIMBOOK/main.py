# Sistem Manajemen Buku dengan Fitur Tambahan
books = []  # List untuk menyimpan data buku
stack = []  # Stack untuk implementasi LIFO
queue = []  # Queue untuk implementasi FIFO

# Fungsi Menambahkan Buku
def add_book():
    """
    Fungsi untuk menambahkan buku baru ke dalam daftar buku, stack, dan queue.

    Pengguna diminta untuk memasukkan ID, Judul, Pengarang, dan Tahun Terbit buku.
    Buku yang baru ditambahkan akan disimpan dalam daftar buku, stack (LIFO), dan queue (FIFO).
    """
    book_id = input("Masukkan ID Buku: ")
    title = input("Masukkan Judul Buku: ")
    author = input("Masukkan Nama Pengarang: ")
    year = input("Masukkan Tahun Terbit: ")
    book = {"ID": book_id, "Title": title, "Author": author, "Year": int(year)}
    
    # Menambahkan buku ke dalam daftar, stack, dan queue
    books.append(book)
    stack.append(book)
    queue.append(book)
    
    print("Buku berhasil ditambahkan.\n")

# Fungsi Menampilkan Semua Buku
def display_books():
    """
    Fungsi untuk menampilkan daftar semua buku yang ada.

    Buku ditampilkan dalam format tabel dengan kolom ID, Judul, Pengarang, dan Tahun.
    Jika tidak ada buku, maka akan muncul pesan bahwa daftar buku kosong.
    """
    if not books:
        print("Tidak ada buku dalam daftar.\n")
        return
    print("\nDaftar Buku:")
    print(f"{'ID':<10} {'Judul':<30} {'Pengarang':<20} {'Tahun':<5}")
    print("-" * 70)
    for book in books:
        print(f"{book['ID']:<10} {book['Title']:<30} {book['Author']:<20} {book['Year']:<5}")
    print()

# Fungsi Menghapus Buku
def delete_book():
    """
    Fungsi untuk menghapus buku berdasarkan ID yang dimasukkan pengguna.

    Pengguna diminta untuk memasukkan ID buku yang ingin dihapus.
    Buku yang dihapus akan dihilangkan dari daftar buku, stack, dan queue.
    """
    book_id = input("Masukkan ID Buku yang ingin dihapus: ")
    global books
    for book in books:
        if book['ID'] == book_id:
            books.remove(book)
            if book in stack:
                stack.remove(book)
            if book in queue:
                queue.remove(book)
            print("Buku berhasil dihapus.\n")
            return
    print("Buku tidak ditemukan.\n")

# Fungsi Mengupdate Buku
def update_book():
    """
    Fungsi untuk memperbarui data buku berdasarkan ID yang dimasukkan pengguna.

    Pengguna diminta untuk memasukkan ID buku yang ingin diupdate, dan kemudian memasukkan 
    data baru untuk Judul, Pengarang, dan Tahun Terbit.
    """
    book_id = input("Masukkan ID Buku yang ingin diupdate: ")
    for book in books:
        if book['ID'] == book_id:
            new_title = input("Masukkan Judul Baru: ")
            new_author = input("Masukkan Nama Pengarang Baru: ")
            new_year = input("Masukkan Tahun Terbit Baru: ")
            book['Title'] = new_title
            book['Author'] = new_author
            book['Year'] = int(new_year)
            print("Buku berhasil diupdate.\n")
            return
    print("Buku tidak ditemukan.\n")

# Fungsi Sorting Buku Berdasarkan Tahun (Quick Sort)
def quick_sort(arr):
    """
    Fungsi untuk mengurutkan buku berdasarkan tahun menggunakan metode Quick Sort.

    Proses pengurutan dilakukan dengan membandingkan tahun terbit dari setiap buku.
    Buku yang lebih tua akan diletakkan di bagian depan.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = []
    greater = []
    for book in arr[1:]:
        if book['Year'] <= pivot['Year']:
            less.append(book)
        else:
            greater.append(book)
    return quick_sort(less) + [pivot] + quick_sort(greater)

def sort_books_by_year():
    """
    Fungsi untuk mengurutkan buku berdasarkan tahun terbit.

    Buku akan diurutkan dengan menggunakan metode Quick Sort.
    Setelah pengurutan, daftar buku akan diperbarui dan informasi pengurutan akan ditampilkan.
    """
    global books
    books = quick_sort(books)
    print("Buku telah diurutkan berdasarkan tahun.\n")

# Fungsi Pencarian Rekursif Berdasarkan Judul
def recursive_search(data, target, index=0):
    """
    Fungsi rekursif untuk mencari buku berdasarkan judul.

    Pencarian dilakukan dengan membandingkan setiap judul buku dengan judul yang dicari.
    Jika ditemukan, fungsi akan mengembalikan buku tersebut, jika tidak, akan dilanjutkan pencarian berikutnya.
    """
    if index >= len(data):
        return None
    if target.lower() in data[index]['Title'].lower():
        return data[index]
    return recursive_search(data, target, index + 1)

def search_book_recursive():
    """
    Fungsi untuk mencari buku berdasarkan judul menggunakan metode pencarian rekursif.

    Pengguna diminta untuk memasukkan judul buku yang ingin dicari, dan hasil pencarian akan ditampilkan.
    Jika buku ditemukan, informasi buku akan ditampilkan. Jika tidak ditemukan, akan muncul pesan bahwa buku tidak ditemukan.
    """
    target = input("Masukkan Judul Buku yang ingin dicari: ")
    result = recursive_search(books, target)
    if result:
        print(f"\nBuku Ditemukan: {result}\n")
    else:
        print("Buku tidak ditemukan.\n")

# Fungsi Menampilkan Buku dalam Stack (LIFO)
def display_stack():
    """
    Fungsi untuk menampilkan buku yang ada dalam stack (LIFO - Last In First Out).

    Buku dalam stack akan ditampilkan dari yang terakhir ditambahkan ke yang pertama.
    """
    if not stack:
        print("Stack kosong.\n")
        return
    print("\nBuku dalam Stack (LIFO):")
    for book in reversed(stack):
        print(f"{book['ID']} - {book['Title']} ({book['Year']})")
    print()

# Fungsi Menampilkan Buku dalam Queue (FIFO)
def display_queue():
    """
    Fungsi untuk menampilkan buku yang ada dalam queue (FIFO - First In First Out).

    Buku dalam queue akan ditampilkan dari yang pertama ditambahkan hingga yang terakhir.
    """
    if not queue:
        print("Queue kosong.\n")
        return
    print("\nBuku dalam Queue (FIFO):")
    for book in queue:
        print(f"{book['ID']} - {book['Title']} ({book['Year']})")
    print()

# Menu Utama
def main_menu():
    """
    Fungsi untuk menampilkan menu utama dan menangani input pilihan pengguna.

    Menu utama memungkinkan pengguna untuk memilih operasi yang ingin dilakukan seperti
    menambah, mengupdate, menghapus buku, atau menampilkan daftar buku, stack, dan queue.
    """
    while True:
        print("=== Sistem Manajemen Buku ===")
        print("1. Tambah Buku")
        print("2. Tampilkan Semua Buku")
        print("3. Update Buku")
        print("4. Hapus Buku")
        print("5. Urutkan Buku Berdasarkan Tahun")
        print("6. Cari Buku (Rekursi)")
        print("7. Tampilkan Buku di Stack (LIFO)")
        print("8. Tampilkan Buku di Queue (FIFO)")
        print("9. Keluar")
        choice = input("Pilih menu (1-9): ")
        print()
        if choice == "1":
            add_book()
        elif choice == "2":
            display_books()
        elif choice == "3":
            update_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            sort_books_by_year()
        elif choice == "6":
            search_book_recursive()
        elif choice == "7":
            display_stack()
        elif choice == "8":
            display_queue()
        elif choice == "9":
            print("Terima kasih telah menggunakan Sistem Manajemen Buku!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")

# Jalankan Program
if __name__ == "__main__":
    main_menu()
