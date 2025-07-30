# My nifty title

Some **text**!

{doc}`README`

$$
z=\sqrt{x^3+y^3}
$$

```{math}
z=\sqrt{x^4+y^4}
```

```{code-block} python
:caption: This is a caption
:emphasize-lines: 2,3
:lineno-start: 1

a = 1
b = 2
c = 3
```

> Hallo

```{image} images/bar.png
:alt: fishy
:class: bg-primary
:width: 320px
:align: center
```

:::{tip}
Let's give readers a helpful hint!
:::

:::{note}
Let's give readers a helpful hint!
:::

:::{note}
:class: margin
This note will be in the margin!
:::

````{margin} Code blocks in margins
```python
print("here is some python")
```
````

```{code-block} python
:caption: python.py

print("A code block with a caption.")
```

Here's my sentence and a marginnote[^mn1].

[^mn1]: {-} And here's my marginnote content.

For example, here is a sidenote[^ex].

[^ex]: Here's my sidenote text!

```{margin} **Here is my margin content**
It is pretty cool!
```

:::{seealso}
Sidenotes and marginnotes are inline content - you cannot use block-level content inside of these notes.
:::

````{sidebar} **My sidebar title**
```{note}
Here is my sidebar content, it is pretty cool!
```
![](./images/bar.png)
````

```{role} python(code)
:language: python
```

In Python you can {python}`import sphinx`.

