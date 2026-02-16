#начни тут создавать приложение с умными заметками
from PyQt5.QtCore import Qt
import json
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QListWidget, QGridLayout, QInputDialog, QMessageBox
app = QApplication([])
main_win = QWidget()
main_win.resize(1200, 600)
free_field = QTextEdit()
note_list = QListWidget()
tag_list= QListWidget()
notes_label = QLabel('Список заметок')
teg_label = QLabel('Список тегов')
create_note = QPushButton('Создать заметку')
delete_note = QPushButton('Удалить заметку')
upload_note = QPushButton('Сохранить заметку')
add_for_note = QPushButton('Добавить к  заметке')
unpin_for_note = QPushButton('Открепить от заметки')
find_f_note = QPushButton('Искать заметки по тегу')
finder_notes = QLineEdit()
finder_notes.setPlaceholderText('Введите тег')
grid_layout = QGridLayout()
grid_layout.addWidget(free_field, 0,0,9,1)
grid_layout.addWidget(notes_label, 0, 1, 1, 1)
grid_layout.addWidget(note_list,1,1,1,2)
grid_layout.addWidget(create_note, 2, 1)
grid_layout.addWidget(delete_note, 2, 2)
grid_layout.addWidget(upload_note, 3, 1, 1, 2)
grid_layout.addWidget(teg_label,4,1,1,1)
grid_layout.addWidget(tag_list,5, 1, 1, 2)
grid_layout.addWidget(finder_notes,6,1,1,2)
grid_layout.addWidget(add_for_note, 7, 1)
grid_layout.addWidget(unpin_for_note, 7, 2)
grid_layout.addWidget(find_f_note, 8, 1, 1, 2)

grid_layout.setColumnStretch(0,3)
grid_layout.setColumnStretch(1,1)
grid_layout.setColumnStretch(2,1)
grid_layout.setSpacing(17)

main_win.setLayout(grid_layout)

main_win.show()
def save_to_fail():
    with open('data.json', 'w', encoding = 'utf-8') as file:
        json.dump(notes, file,ensure_ascii=False)


with open('data.json','r',encoding = 'utf-8') as file:
    notes = json.load(file)
    note_list.addItems(notes)
def show_note():
    name = note_list.selectedItems()[0].text()
    free_field.setText(notes[name]['текст'])
    tag_list.clear()
    tag_list.addItems(notes[name]['теги'])
note_list.itemClicked.connect(show_note)
notes_win = QInputDialog()
#написисать  def add_note()
def add_note():
    note_name, result = QInputDialog.getText(notes_win, 'Создать заметку', 'Название заметки:')
    if (note_name != '' or note_name != ' ') and result == True:
        notes[note_name] = {'текст':'','теги':[]}
        note_list.addItem(note_name)
    else:
        return

def warning(text,title='Ошибка'):
    error = QMessageBox()
    error.setWindowTitle(title)
    error.setText(text)
    error.setIcon(QMessageBox.Warning)
    error.exec_()



def del_note():
    if len(note_list.selectedItems()) > 0:
        name = note_list.selectedItems()[0].text()
        del notes[name]
        save_to_fail()
        tag_list.clear()
        note_list.clear()
        note_list.addItems(notes)
        free_field.clear()
    else:
        warning('Вы не выбрали элемент, который хотите удалить!')

def save_note():
    if len(note_list.selectedItems()) > 0:
        name = note_list.selectedItems()[0].text()
        notes[name]['текст'] = free_field.toPlainText()
        save_to_fail()
    else:
        return

def add_tag():
    if len(note_list.selectedItems()) > 0:
        new_tag = finder_notes.text()
        name = note_list.selectedItems()[0].text()
        if not new_tag in notes[name]['теги']:
            tag_list.addItem(new_tag)
            notes[name]['теги'].append(new_tag)
            finder_notes.clear()
            save_to_fail()
        else:
            warning('Этот тэг уже существует.')
#попробовать дописать остальные функции

def del_tag():
    if len(note_list.selectedItems()) > 0:
        name = note_list.selectedItems()[0].text()
        sel_tag = tag_list.selectedItems()[0].text()
        notes[name]['теги'].remove(sel_tag)
        tag_list.clear()
        tag_list.addItems(notes[name]['теги'])
        save_to_fail()

def search_note():
    if find_f_note.text() == 'Искать заметки по тегу' and len(finder_notes.text()) > 0:
        find_f_note.setText('Сбросить поиск')
        filter_list = {}
        for i in notes:
            if finder_notes.text() in notes[i]['теги']:
                filter_list[i] = notes[i]
        note_list.clear()
        note_list.addItems(filter_list)
        free_field.clear()
        tag_list.clear()
    elif find_f_note.text() == 'Сбросить поиск':
        find_f_note.setText('Искать заметки по тегу')
        finder_notes.clear()
        note_list.clear()
        note_list.addItems(notes)
        free_field.clear()
        tag_list.clear()
    else:
        return
    










add_for_note.clicked.connect(add_tag)
delete_note.clicked.connect(del_note)
create_note.clicked.connect(add_note)      
upload_note.clicked.connect(save_note)
unpin_for_note.clicked.connect(del_tag)
find_f_note.clicked.connect(search_note)
app.exec_()