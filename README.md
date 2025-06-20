# 🔍 Simple Log Parser

A beginner-friendly Python script that reads a `.log` file, counts the number of `ERROR` lines, and generates a summary report in both `.txt` and `.csv` formats.

---

## 📌 Features

- ✅ Parses `.log` files line by line
- ✅ Counts total lines and `ERROR` lines
- ✅ Saves a clean summary report to:
  - `summary.txt`
  - `summary.csv`
- ✅ Extracts all error messages to `error_lines.txt`

---

## 📁 Sample Log (`app.log`)

```log
2025-06-20 10:01:23 INFO  - Application started
2025-06-20 10:01:35 ERROR - Failed to connect to database
2025-06-20 10:01:50 ERROR - Connection timeout
2025-06-20 10:03:00 ERROR - Unexpected null value in user data
