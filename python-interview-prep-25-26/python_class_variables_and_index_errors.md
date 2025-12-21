# Python Interview Notes – Class Variables, Inheritance & Index Errors

This document summarizes key **Python interview concepts** discussed, with examples, outputs, and explanation. Suitable for quick revision and GitHub reference.

---

## 1. Class Variables and Inheritance

### Question 1: What is a class variable?

A **class variable** is shared across the class and all its subclasses unless explicitly overridden.

```python
class Parent:
    x = 1
```

* `x` belongs to the **class**, not instances
* Accessible as `Parent.x`

---

## 2. Inheriting Class Variables

```python
class Child1(Parent):
    pass

class Child2(Parent):
    pass
```

### Question: What is the output?

```python
print(Parent.x, Child1.x, Child2.x)
```

✅ Output:

```
1 1 1
```

### Explanation:

* `Child1` and `Child2` **inherit** `x` from `Parent`
* Python looks up the attribute via the inheritance chain

---

## 3. Overriding a Class Variable in Child

```python
Child1.x = 2
print(Parent.x, Child1.x, Child2.x)
```

✅ Output:

```
1 2 1
```

### Key Interview Point ⭐

* Assigning `Child1.x = 2` **creates a new class variable only in Child1**
* It does NOT modify `Parent.x`

---

## 4. Modifying the Parent Class Variable

```python
Parent.x = 3
print(Parent.x, Child1.x, Child2.x)
```

✅ Output:

```
3 2 3
```

### Explanation:

* `Child2` still inherits from `Parent`, so it sees `3`
* `Child1` already has its own `x`, so it remains `2`

---

## 5. Full Execution Output

```text
1 1 1
1 2 1
3 2 3
```

---

## 6. Key Interview Takeaways (Must Remember)

* Reading a class variable → Python searches parent classes
* Writing to a class variable → creates it in the **current class only**
* Child classes inherit changes from parent **only if not overridden**

---

## 7. List Index Error (Common Interview Trap)

### Question: What happens here?

```python
lista = ['a', 'b', 'c', 'd', 'e']
print(lista[10])
```

❌ Output:

```
IndexError: list index out of range
```

### Explanation:

* List length = 5
* Valid indexes = `0 to 4`
* Accessing index `10` is invalid

---

## 8. How to Avoid IndexError

### Option 1: Length Check

```python
if len(lista) > 10:
    print(lista[10])
```

### Option 2: try/except

```python
try:
    print(lista[10])
except IndexError:
    print("Invalid index")
```

---

## 9. One-Line Interview Summary

> Class variables are shared through inheritance, but assigning to a child creates a separate copy, and Python strictly enforces list index bounds using `IndexError`.

---

## 10. Suggested GitHub File Name

```
python_class_variables_and_index_errors.md
```

---

✔ Ready to be added to GitHub as interview prep notes.
