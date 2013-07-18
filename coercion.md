
# Coercion

## Sequences

In `x + y`, if *x* is a sequence that implements sequence concatenation, sequence concatenation is invoked.

```python
>>> [1, 2, 3] + [1, 2, 3]
[1, 2, 3, 1, 2, 3]
>>> (1, 2, 3) + (1, 2, 3)
(1, 2, 3, 1, 2, 3)
>>> '123' + '123'
'123123'
```

In `x * y`, if one operator is a sequence that implements sequence repetition, and the other is an integer, sequence repetition is invoked.

```python
>>> [1, 2, 3] * 2
[1, 2, 3, 1, 2, 3]
>>> (1, 2, 3) * 2
(1, 2, 3, 1, 2, 3)
>>> '123' * 2
'123123'
```

NOTE: The order of operands is irrelevant.

```python
>>> 2 * [1, 2, 3] == [1, 2, 3] * 2
True
```

## Booleans

NOTE: Booleans are considered integers. Therefore, multiplication by booleans is permissible.

```python
>>> assert True == 1
>>> [1, 2, 3] * True
[1, 2, 3]
```

Multiplying by 0 or False gives empty sequences

```python
>>> [1, 2, 3] * False
[]
>>> [1, 2, 3] * -1
[]
```

## Glyphs

Rich comparisons (implemented by method `__eq__()` and so on) never use coercion.

```python
>>> {} == []
False
>>> bool({}) == bool([])
True
```

Backticks coerces things to `repr`. (this is deprecated; use `repr`)

```python
>>> `[1, 2, 3]` == repr([1, 2, 3])
True
```

## Casting

Strings ints are converted to numbers

```python
>>> int('10')
10
```

String booleans are treated as regular strings

```python
>>> bool('False')
True
```
