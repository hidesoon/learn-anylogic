*来源 (Source): <https://anylogic.help/advanced/code/java-types.html>*

---

# Primitive data types

There are eight primitive data types in Java, but in AnyLogic models we typically use these four:

| Type name | Represents | Examples of constants |
| --- | --- | --- |
| int | Integer numbers | 12 10000 -15 0 |
| double | Real numbers | 877.13 12.0 12. 0.153 .153 -11.7 3.6e-5 |
| boolean | Boolean values | true false |
| String | Text strings | "AnyLogic" "X = " "Line\nNew line" "" |

The word **double** means real value with double precision. In the AnyLogic engine, all real values (such as time, coordinates, length, speed, random numbers) are double precision.

The type String is actually a class (a non-primitive type, note that its name starts with a capital letter), but it is a fundamental class, so some operations on strings are built into the core of the Java language.

Consider the **numeric constants**. Depending on the way you write a number, Java will treat it either as real or as integer. Any number with the decimal delimiter . is treated as a real number, even if its fractional part is missing or contains only zeroes (this is important for integer division). If integer or fractional part is zero, it can be skipped, so .153 is the same as 0.153, and 12. is the same as 12.0.

**Boolean constants** in Java are true and false and, unlike in languages like C or C++, they are not interchangeable with numbers, so you cannot treat false as 0, or non-zero number as true.

**String constants** are sequences of characters enclosed between the quote marks. The empty string (the string containing no characters) is denoted as "". Special characters are included in string constants with the help of escape sequences that start with the backslash. For example the end of line is denoted by \n, so the string "Line one\nLine two" will appear as:

```
Line one
Line two
```

If you wish to include the quote character into a string, you need to write \". For example, the string constant "String with \" in the middle" is printed as:

> String with " in the middle

To include a backslash, write it twice: "This is a backslash: \\". This will print as:

> This is a backslash: \
