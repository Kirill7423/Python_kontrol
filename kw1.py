# Необходимо написать проект, содержащий функционал работы с заметками. 
# Программа должна уметь:
 
# сохранять данные в файл, 
# читать данные из файла, 
# делать выборку по дате, 
# выводить на экран выбранную запись, 
# выводить на экран весь список записок, 
# добавлять запись, 
# редактировать запись 
# удалять запись

import csv
from datetime import datetime
class Note:
    def __init__(self, id, title, body, created):
        self.id = id
        self.title = title
        self.body = body
        self.created = created
    def save_to_csv(self):
        with open('notes.csv', 'a', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow([self.id, self.title, self.body, self.created])

    @staticmethod
    def load_from_csv():
        notes = []
        with open('notes.csv', 'r') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                id, title, body, created = row
                note = Note(id, title, body, created)
                notes.append(note)
        return notes
    
    def update(note_id, new_title, new_body):
        notes = []
        with open('notes.csv', 'r') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                notes.append(row)
        with open('notes.csv', 'w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            for row in notes:
                if row[0] == note_id:
                    row[1] = new_title
                    row[2] = new_body
                    row[3] = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
                    writer.writerow(row)
                else: 
                    writer.writerow(row)

    @staticmethod
    def delete_from_csv(note_id):
        notes = []
        with open('notes.csv', 'r') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                notes.append(row)
        with open('notes.csv', 'w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            for row in notes:
                if row[0] != note_id:
                    writer.writerow(row)

def main():

    while True:

        print("\nМеню:")
        print("1 - Выборка заметок по дате")
        print("2 - Вывести весь список заметок")
        print("3 - Вывести заметку по ID")
        print("4 - Добавить заметку")
        print("5 - Редактировать заметку")
        print("6 - Удалить заметку")
        print("7 - Выход")
        command = input("Выберите номер команды: ")

        if command == '1':
            list_1 = []
            notes = []
            with open('notes.csv', 'r') as file:
                reader = csv.reader(file, delimiter=';')
                for row in reader:
                    notes.append(row)
            data_find = input('Введите дату  в формате дд-мм-гггг: ')
            for row in notes:
                list_1 = row[3].split(' ')
                if list_1[0] == data_find:
                    print(f"ID: {row[0]}; Заголовок: {row[1]}; Текст: {row[2]}")
           
        elif command == '2':
            notes = Note.load_from_csv()
            print("Список всех заметок")
            for note in notes:
                print(f"ID: {note.id}; Заголовок: {note.title}; Текст: {note.body}; Дата создания/изменения: {note.created}")

        elif command =='3':
            notes = Note.load_from_csv()
            print("Список всех заметок")
            for note in notes:
                print(f"ID: {note.id}; Заголовок: {note.title}; Дата создания/изменения: {note.created}")
            note_id = input("Выберите ID заметки для подробного просмотра: ")
            for note in notes:
                if note.id == note_id:
                    print(f"Заголовок: {note.title}; Текст: {note.body}; Дата создания/изменения: {note.created}")
                    break

        elif command == '4':
            new_id = input("Введите уникальный ID заметки: ")
            new_title = input("Введите заголовок: ")
            new_body = input("Введите текст заметки: ")
            new_note = Note(new_id, new_title, new_body, datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
            new_note.save_to_csv()
        
        elif command == '5':
            notes = Note.load_from_csv()
            note_id = input("Выберите ID заметки для редактирования: ")
            for note in notes:
                if note.id == note_id:
                    new_title = input("Введите новый заголовок: ")
                    new_body = input("Введите новый текст: ")
                    Note.update(note_id, new_title, new_body)

        elif command == '6':
            notes = Note.load_from_csv()
            print("Список всех заметок")
            for note in notes:
                print(f"ID: {note.id}; Заголовок: {note.title}; Дата создания/изменения: {note.created}")
            note_id = input("Выберите ID заметки для удаления: ")
            Note.delete_from_csv(note_id)

        elif command == '7':
            break

        else:
            print("Введите еще раз номер команды")

if __name__ == "__main__":
    main()