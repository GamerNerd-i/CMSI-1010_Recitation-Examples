# Expressions vs. Statements

To help you speak programming language a bit more fluently, here's a little
vocabulary for you: expressions and statements.

## Statements are standalone actions that change the program

Statements execute something for the program. They have an identifiable impact that follows through the remaining code. Some examples follow.

> This is a `print` statement -- you'll be using these a lot!

```python
print("Hello world!")
```

> This statement initializes (creates) a variable called `x`, and gives it the value `4`.  

```python
x = 4
```

In both cases, you can verify that something happened. The `print` statement will show up in the console, and you can check elsewhere that `x = 4`.

## Expressions are lesser actions that don't change the program on their own

Expressions might still execute an action, but that result isn't necessarily saved. They need to be placed in a statement to do something meaningful and become a "full" action.

None of the following examples are *incorrect* -- they just don't do anything meaningful. If you run them, Python might give you an output, but don't mistake that for the expression "doing something!"

> Individual values are expressions. Python will usually echo these back to you.

```python
"this is a string!"
4
True
```

> Operations on individual values are expressions. These evaluate to a normal value anyway -- try running them in Python and you'll see that they're actually identical to the example above!

```python
"this " + "is " + "a " + "string!"
2 ** 2
not False
```

## Statements make up the program, but expressions make up those statements

Python is a programming language - but it's still a language! Think of it like a spoken language:

* **Statements** are like sentences. Even a short sentence like "Hello!" or "Run!" expresses a full thought.
* **Expressions** are like individual words that make up a sentence. Words like "Python", "type", or "a" don't express a full idea on their own. That's why you put them together and form a sentence!
