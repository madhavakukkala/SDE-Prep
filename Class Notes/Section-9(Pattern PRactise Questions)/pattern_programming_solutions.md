# Pattern Programming Solutions

## 1. Square of side N

```python
n = int(input())

for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()
```

---

## 2. Hollow Square of side N

```python
n = int(input())

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
```

---

## 3. Rectangle Pattern

```python
rows = int(input())
cols = int(input())

for i in range(rows):
    for j in range(cols):
        print("*", end=" ")
    print()
```

---

## 4. Right Angled Triangle

```python
n = int(input())

for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")
    print()
```

---

## 5. Inverted Right Angled Triangle

```python
n = int(input())

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
```

---

## 6. Pyramid Pattern

```python
n = int(input())

for i in range(1, n+1):
    print(" " * (n-i), end="")

    for j in range(i):
        print("* ", end="")

    print()
```

---

## 7. Inverted Pyramid Pattern

```python
n = int(input())

for i in range(n, 0, -1):
    print(" " * (n-i), end="")

    for j in range(i):
        print("* ", end="")

    print()
```

---

## 8. Right Angled Triangle with Numbers

```python
n = int(input())

for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
```

---

## 9. Floyd’s Triangle

```python
n = int(input())

num = 1

for i in range(1, n+1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
```

---

## 10. Diamond Pattern

```python
n = int(input())

# Upper part
for i in range(1, n+1):
    print(" " * (n-i), end="")

    for j in range(i):
        print("* ", end="")

    print()

# Lower part
for i in range(n-1, 0, -1):
    print(" " * (n-i), end="")

    for j in range(i):
        print("* ", end="")

    print()
```

---

## 11. Right Angled Triangle II

```python
n = int(input())

for i in range(1, n+1):
    print(" " * (n-i), end="")

    for j in range(i):
        print("*", end=" ")

    print()
```

---

## 12. Sandglass Pattern

```python
n = int(input())

# Upper part
for i in range(n, 0, -1):
    print(" " * (n-i), end="")

    for j in range(i):
        print("* ", end="")

    print()

# Lower part
for i in range(2, n+1):
    print(" " * (n-i), end="")

    for j in range(i):
        print("* ", end="")

    print()
```

---

## 13. Hollow Right Triangle

```python
n = int(input())

for i in range(1, n+1):
    for j in range(1, i+1):

        if j == 1 or j == i or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()
```

---

## 14. Hollow Inverted Right Triangle

```python
n = int(input())

for i in range(n, 0, -1):
    for j in range(1, i+1):

        if j == 1 or j == i or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()
```

---

## 15. Number Pyramid Pattern

```python
n = int(input())

for i in range(1, n+1):
    print(" " * (n-i), end="")

    for j in range(1, i+1):
        print(j, end=" ")

    print()
```
