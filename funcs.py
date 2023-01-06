import sqlite3


class SQL:
  '''
  Класс для создания соединения с базой данных 'SurveyBot.db'.
  Используется с помощью контекстного менеджера with.
  Создает курсор (cursor) и позволяет взаимодействовать с базой данных.
  '''

  def __init__(self):
    self.database_name = 'school.db'

  def __enter__(self):
    self.connection = sqlite3.connect(self.database_name)
    self.cursor = self.connection.cursor()
    return self.cursor

  def __exit__(self, exception_type, exception_value, exception_traceback):
    self.connection.commit()
    self.cursor.close()
    self.connection.close()
    if exception_value:
      raise
