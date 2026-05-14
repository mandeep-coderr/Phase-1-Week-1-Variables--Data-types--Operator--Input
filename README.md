# Phase 1 — Week 1: Переменные, Типы данных, Операторы, Ввод

Учебный репозиторий по основам Python.

---

## 📁 Структура проекта

```
.
└── 1. Variables and Data Types/
    ├── variables_datatypes.py          # Теория: переменные и типы данных
    └── practice_task_variables_datatypes.py  # Практические задания
```

---

## 1. Переменные и типы данных

### `variables_datatypes.py` — теоретический файл

Демонстрирует базовые концепции:

- **Типы данных:** `int`, `str`, `float`, `bool`
- **Функция `type()`** — проверка типа переменной
- **Соглашение об именовании:** `snake_case`, нельзя начинать с цифры
- **Множественное присваивание:**
  ```python
  score, player_name, is_alive = 25, "Mandeep", True
  ```

**Примеры переменных:**

| Переменная            | Тип     | Значение        |
|-----------------------|---------|-----------------|
| `house_number`        | `int`   | `42`            |
| `street_name`         | `str`   | `"Park Avenue"` |
| `my_height`           | `float` | `1.75`          |
| `is_learning`         | `bool`  | `True`          |
| `bank_account_balance`| `float` | `500.50`        |

---

### `practice_task_variables_datatypes.py` — практические задания

Закрепление навыков на практике:

- Объявление переменных разных типов (`str`, `int`, `float`, `bool`)
- Применение `type()` к каждой переменной
- **Множественное присваивание:**
  ```python
  item_1, item_2 = "Banana", "Apple"
  ```
- **Обмен значений двух переменных (swap):**
  ```python
  product_1, shopping_5 = shopping_5, product_1
  ```
- **Хранение адреса по частям и вывод одной строкой:**
  ```python
  print(house_no, street, city, state)
