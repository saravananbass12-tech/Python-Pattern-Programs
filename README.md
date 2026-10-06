# 🐍 Python Pattern Programs 

<div align="center">

<img src="https://img.shields.io/badge/Python-2026-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/Pattern%20Programs-2026-6C63FF?style=for-the-badge">
<img src="https://img.shields.io/badge/Python%20Practice-00C853?style=for-the-badge">

</div>

---

## 📌 About This Repository

This repository contains **Python pattern programs** created to practice:

* `for` loops
* Nested `for` loops
* `range()`
* Conditional statements
* `if-else`
* Pattern logic
* Console-based output

These programs are useful for **Python beginners, logical thinking, coding practice, and interview preparation**.

---

# ⭐ Pattern Programs

## 1️⃣ Decrement Pattern / Inverted Half Pyramid

### Python Code

```python
for i in range(1, 6):
    for j in range(i, 6):
        print("*", end="  ")
    print()
```

### Output

```text
*  *  *  *  *
*  *  *  *
*  *  *
*  *
*
```

---

## 2️⃣ Increment Pattern / Half Pyramid

### Python Code

```python
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()
```

### Output

```text
*
* *
* * *
* * * *
* * * * *
```

---

# 3️⃣ Full Pyramid

### Python Code

```python
for i in range(6):
    for j in range(i, 6):
        print(" ", end=" ")

    for j in range(i + 1):
        print("*", end=" ")

    for j in range(i):
        print("*", end=" ")

    print()
```

### Output

```text
          *
        * * *
      * * * * *
    * * * * * * *
  * * * * * * * * *
* * * * * * * * * * *
```

---

# 4️⃣ Inverted Full Pyramid

### Python Code

```python
for i in range(6):
    for j in range(i + 1):
        print(" ", end=" ")

    for j in range(i, 6):
        print("*", end=" ")

    for j in range(i, 6 - 1):
        print("*", end=" ")

    print()
```

### Output

```text
* * * * * * * * * * *
  * * * * * * * * *
    * * * * * * *
      * * * * *
        * * *
          *
```

---

# ❤️ 5️⃣ Heart Pattern

### Python Code

```python
for i in range(6):
    for j in range(7):
        if (i == 0 and j % 3 != 0) or \
           (i == 1 and j % 3 == 0) or \
           (i - j == 2) or \
           (i + j == 8):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
```

### Output

```text
  * *   * *
*       *       *
  *           *
    *       *
      *   *
        *
```

---

# 📚 Concepts Covered

| Concept           | Usage                       |
| ----------------- | --------------------------- |
| `for` loop        | Repeating statements        |
| Nested loop       | Creating rows and columns   |
| `range()`         | Controlling loop iterations |
| `print()`         | Displaying patterns         |
| `end`             | Controlling output spacing  |
| `if`              | Pattern conditions          |
| `else`            | Printing spaces             |
| Logical operators | Creating the heart pattern  |

---

# 🎯 Learning Objectives

* Understand nested loops
* Improve logical thinking
* Learn pattern generation
* Practice Python syntax
* Understand row and column logic
* Develop problem-solving skills
* Prepare for basic coding interviews

---

# 🛠️ Technology

<div align="center">

<img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white">

</div>

---

# 📂 Pattern List

```text
Python Pattern Programs
│
├── ⭐ Decrement Pattern
├── ⭐ Increment Pattern
├── 🔺 Full Pyramid
├── 🔻 Inverted Full Pyramid
└── ❤️ Heart Pattern
```

---

# 👨‍💻 Author

<div align="center">

## SARAVANAN D

**Power BI | Data Analytics | AI & Technology**

📧 **[saravananbass12@gmail.com](mailto:saravananbass12@gmail.com)**

📍 **Tamil Nadu, India**

💻 **GitHub**

https://github.com/saravananbass12-tech

</div>

---

<div align="center">

### ⭐ Python Pattern Programs 

**Learn • Practice • Code • Improve**

</div>
