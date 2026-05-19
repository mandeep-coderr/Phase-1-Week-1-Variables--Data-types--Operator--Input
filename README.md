# Phase 1 — Week 1: Variables, Data Types, Operators, Input

Учебный репозиторий с практическими заданиями по основам Python.

## Содержание проекта

| № | Папка | Описание |
|---|-------|----------|
| 7 | `7. API Rate Limit Calculator` | Калькулятор лимита запросов API |

---

## 7. API Rate Limit Calculator

**Файл:** `7. API Rate Limit Calculator/Rate_limit_calculator.py`

### Описание

Скрипт рассчитывает дневной лимит запросов к API на основе месячного лимита и количества дней в текущем месяце.

### Входные данные

| Переменная | Тип | Описание |
|------------|-----|----------|
| `API_limit` | `int` | Месячный лимит запросов API |
| `API_days_limit` | `int` | Количество дней в текущем месяце |
| `safety_threshold` | `int` | Порог безопасности (по умолчанию: `100`) |

### Вычисления

- `daily_limit` — дневной лимит запросов (`//` целочисленное деление).
- `leftover_requests` — остаток запросов (`%` остаток от деления).
- `safe_zone` — флаг безопасного режима (`daily_limit >= safety_threshold`).

### Пример запуска

```bash
python "7. API Rate Limit Calculator/Rate_limit_calculator.py"
```

```
Monthly Rate Limit of API ? 3000
Days in Current Month ? 30

    ====== API RATE LIMIT REPORT ======
Monthly Rate Limit of API: 3000
Days in Current Month: 30
