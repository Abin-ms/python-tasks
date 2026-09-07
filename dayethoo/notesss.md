`sort()` is a **method**, while `sorted()` is a **function**.

### `sort()` → Method

It belongs to the **list object**, so you call it using `.`:

```python
numbers = [30, 10, 20]

numbers.sort()

print(numbers)
```

Here, `sort()` is a **list method**.

### `sorted()` → Function

It is a **built-in Python function**:

```python
numbers = [30, 10, 20]

result = sorted(numbers)

print(result)
```

### 🧠 Easy rule

If you see:

```python
object.method()
```

it's a **method**.

If you see:

```python
function(object)
```

it's a **function**.

So:

```text
numbers.sort()       → method ✅
sorted(numbers)      → function ✅
```

This distinction is important when learning Python's **lists, strings, dictionaries, and built-in functions**.
