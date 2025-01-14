# Dokumentasi Modul CRUD Sistem Manajemen Buku

## **Pendahuluan**
Modul ini dirancang untuk membantu mahasiswa memahami implementasi CRUD (Create, Read, Update, Delete) dalam konteks pengelolaan data buku sederhana menggunakan bahasa pemrograman Python.

Studi kasus yang digunakan adalah **Manajemen Data Buku**. Selain itu, modul ini juga memperkenalkan konsep dari:

- **Sorting**: Mengurutkan data buku berdasarkan tahun terbit menggunakan algoritma Quick Sort.
- **Rekursi**: Mencari buku berdasarkan judul menggunakan teknik rekursif.
- **Struktur Data Stack dan Queue**: Menggunakan Stack (LIFO: *Last In, First Out*) dan Queue (FIFO: *First In, First Out*) untuk menyimpan buku.

## **Fitur yang Diimplementasikan**
1. **CRUD**:
    - Menambahkan buku (Create).
    - Menampilkan semua buku (Read).
    - Memperbaharui data buku (Update).
    - Menghapus buku dari daftar (Delete).

2. **Sorting**:
    - Buku dapat diurutkan berdasarkan tahun terbit menggunakan **Quick Sort**.

3. **Rekursi**:
    - Pencarian buku berdasarkan judul menggunakan tenik/metode rekursif.

4. **Struktur Data**:
    - **Stack**: Menyimpan/menampilkan buku terakhir yang ditambahkan dengan prinsip LIFO
    - **Queue**: Menyimpan/menampilkan buku sesuai urutan penambahan dengan prinsip FIFO

---

## **Kode dan Penjelasan**

### **1. Struktur Data Utama**
```python
books = [] # List untuk menyimpan data buku
stack = [] # Stack untuk implementasi LIFO
queue = [] # Queue untuk implementasi FIFO
```

- `books`: List utama untuk menyimpan data buku.
- `stack`: Menyimpan buku dengan prinsip **Last In, First Out**.
- `queue`: Menyimpan buku dengan prinsip **First In, First Out**.

### **2. Fungsi Menambahkan Buku**
```python
def add_book():
    book_id = input("Masukkan ID Buku: ")
    title = input("Masukkan Judul Buku: ")
    author = input("Masukkan Nama Pengarang: ")
    year = input("Masukkan Tahun Terbit: ")
    book = {"ID": book_id, "Title": title, "Author": author, "Year": int(year)}
    books.append(book) # Menambahkan buku ke dalam daftar buku
    stack.append(book) # Menambahkan buku ke dalam stack (LIFO)
    queue.append(book) # Menambahkan buku ke dalam queue (FIFO)
    print("Buku berhasil ditambahkan.\n")
```

#### **Penjelasan**:
Fungsi `add_book()` digunakan untuk menambahkan buku baru ke dalam sistem. Fungsi menerima input ID, judul, pengarang, dan tahun terbit buku. Setiap Data buku yang ditambahkan akan dimasukan dan disimpan ke dalam tiga struktur data yang bertipe data dictionary: `books`, `stack`, dan `queue`.

### **3. Fungsi Menampilkan Semua Buku**
```python
def display_books():
    if not books:
        print("Tidak ada buku dalam daftar.\n")
        return
    print("\nDaftar Buku:")
    print(f"{'ID':<10} {'Judul':<30} {'Pengarang':<20} {'Tahun':<5}")
    print("-" * 70)
    for book in books:
        print(f"{book['ID']:<10} {book['Title']:<30} {book['Author']:<20} {book['Year']:<5}")
    print()
```

#### **Penjelasan**:
Fungsi `display_books()` menampilkan daftar semua buku yang ada. Fungsi ini akan mengecek apakah daftar buku kosong?. Jika tidak kosong, buku akan ditampilkan dalam format tabel dan jika `books` kosong, akan menampilkan pesan "Tidak ada buku dalam daftar."

### **4. Fungsi Menghapus Buku**
```python
def delete_book():
    book_id = input("Masukkan ID Buku yang ingin dihapus: ")
    global books
    for book in books:
        if book['ID'] == book_id:
            books.remove(book) # Menghapus dari daftar buku
            if book in stack:
                stack.remove(book) # Menghapus dari stack
            if book in queue:
                queue.remove(book) # Menghapus dari queue
            print("Buku berhasil dihapus.\n")
            return
    print("Buku tidak ditemukan.\n")
```

#### **Penjelasan**:
Fungsi `delete_book()` digunakan untuk menghapus buku berdasarkan ID. Buku yang dihapus akan dikeluarkan dari semua struktur data yang ada (`books`, `stack` dan `queue`).

### **5. Fungsi Mengupdate Buku**
```python
def update_book():
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
```

#### **Penjelasan**:
Fungsi update_book() digunakan untuk mengubah data buku berdasarkan ID. Pengguna dapat memperbarui judul, pengarang, dan tahun terbit buku.

### **6. Fungsi Sorting dengan Quick Sort**
```python
def quick_sort(arr):
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
    global books
    books = quick_sort(books)
    print("Buku telah diurutkan berdasarkan tahun.\n")

```

#### **Penjelasan**:
Fungsi `quick_sort()` adalah implementasi algoritma Quick Sort untuk mengurutkan buku berdasarkan tahun terbit. Fungsi `sort_books_by_year()` memanggil `quick_sort()` untuk mengurutkan daftar buku.

### **7. Fungsi Pencarian Rekursif**
```python
def recursive_search(data, target, index=0):
    if index >= len(data):
        return None
    if target.lower() in data[index]['Title'].lower():
        return data[index]
    return recursive_search(data, target, index + 1)

def search_book_recursive():
    target = input("Masukkan Judul Buku yang ingin dicari: ")
    result = recursive_search(books, target)
    if result:
        print(f"\nBuku Ditemukan: {result}\n")
    else:
        print("Buku tidak ditemukan.\n")
```

#### **Penjelasan**:
Fungsi `recursive_search()` adalah implementasi pencarian rekursif untuk mencari buku berdasarkan judul. Fungsi ini akan memeriksa setiap elemen dalam daftar buku hingga ditemukan atau mencapai akhir daftar.

### **8. Fungsi Menampilkan Stack (LIFO)**
```python
def display_stack():
    if not stack:
        print("Stack kosong.\n")
        return
    print("\nBuku dalam Stack (LIFO):")
    for book in reversed(stack):
        print(f"{book['ID']} - {book['Title']} ({book['Year']})")
    print()
```

#### **Penjelasan**:
Fungsi `display_stack()` akan menampilkan buku yang ada di dalam stack menggunakan prinsip LIFO (Last In, First Out). Dalam hal ini **Stack**: akan menampilkan buku terakhir yang ditambahkan terlebih dahulu (LIFO).

### **9. Fungsi Menampilkan Queue (FIFO)**
```python
def display_queue():
    if not queue:
        print("Queue kosong.\n")
        return
    print("\nBuku dalam Queue (FIFO):")
    for book in queue:
        print(f"{book['ID']} - {book['Title']} ({book['Year']})")
    print()
```
#### **Penjelasan**:
Fungsi `display_queue()` akan menampilkan buku yang ada di dalam queue menggunakan prinsip FIFO (First In, First Out). Dalam hal ini **Queue**: akan menampilkan buku sesuai urutan penambahan (FIFO).

### **10. Menu Utama**
```python
def main_menu():
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

```

#### **Penjelasan**:
Fungsi main_menu() adalah menu utama dari sistem yang memungkinkan pengguna untuk memilih fitur yang diinginkan. Program akan terus berjalan hingga pengguna memilih untuk keluar.

---

## **Cara Menjalankan Program**
1. Gunakan virtual environment
2. Salin kode program ke file Python, misalnya `crud_books.py`.
3. Jalankan program menggunakan terminal atau editor Python:
```bash
   python crud_books.py
```
4. Ikuti menu yang ditampilkan untuk mengakses fitur.

---

## **Kesimpulan**
Modul ini memberikan pengalaman belajar yang komprehensif tentang Sistem Manajemen Buku Sederhana. Sistem ini adalah sebuah aplikasi untuk mengelola data buku dengan berbagai fitur yang memanfaatkan struktur data seperti list, stack, dan queue. Sistem ini mengimplementasikan fitur-fitur penting seperti menambah, menghapus, dan memperbarui buku, serta fitur pencarian dengan rekursi dan algoritma sorting. Dengan ini Mahasiswa diharapkan dapat memahami dan mengembangkan fitur lebih lanjut berdasarkan kebutuhan.
