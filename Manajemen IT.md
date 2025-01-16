class Project:
    def __init__(self, name, description, status):
        self.name = name
        self.description = description
        self.status = status

    def __str__(self):
        return f"Nama Proyek: {self.name}, Deskripsi: {self.description}, Status: {self.status}"


class ProjectManagementSystem:
    def __init__(self):
        self.projects = []

    def add_project(self, name, description, status):
        new_project = Project(name, description, status)
        self.projects.append(new_project)
        print(f"Proyek '{name}' berhasil ditambahkan.")

    def display_projects(self):
        if not self.projects:
            print("Tidak ada proyek yang tersedia.")
            return
        for index, project in enumerate(self.projects):
            print(f"{index + 1}. {project}")

    def update_project_status(self, project_index, new_status):
        if 0 <= project_index < len(self.projects):
            self.projects[project_index].status = new_status
            print(f"Status proyek '{self.projects[project_index].name}' berhasil diupdate menjadi '{new_status}'.")
        else:
            print("Indeks proyek tidak valid.")


def main():
    pms = ProjectManagementSystem()

    while True:
        print("\nSistem Manajemen Proyek IT")
        print("1. Tambah Proyek")
        print("2. Tampilkan Proyek")
        print("3. Update Status Proyek")
        print("4. Keluar")

        choice = input("Pilih opsi (1-4): ")

        if choice == '1':
            name = input("Masukkan nama proyek: ")
            description = input("Masukkan deskripsi proyek: ")
            status = input("Masukkan status proyek (Aktif/Selesai): ")
            pms.add_project(name, description, status)

        elif choice == '2':
            pms.display_projects()

        elif choice == '3':
            pms.display_projects()
            project_index = int(input("Masukkan nomor proyek yang ingin diupdate: ")) - 1
            new_status = input("Masukkan status baru (Aktif/Selesai): ")
            pms.update_project_status(project_index, new_status)

        elif choice == '4':
            print("Keluar dari sistem.")
            break

        else:
            print("Opsi tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()
