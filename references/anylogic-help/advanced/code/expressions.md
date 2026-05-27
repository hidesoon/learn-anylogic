*来源 (Source): <https://anylogic.help/advanced/code/expressions.html>*

---

# Arithmetic expressions

Arithmetic expressions in Java are composed with the usual operators +, -, \*, /, and the remainder operator %. Multiplication and division operations have a higher priority than addition and subtraction. Operations with equal priority are performed from left to right. Parentheses are used to control the order of operation execution.

```
a + b / c ≡ a + ( b / c )
a * b - c ≡ ( a * b ) - c
a / b / c ≡ ( a / b ) / c
```

It is recommended to always use parentheses to explicitly define the order of operations, so you do not have to remember which operation has higher priority.

A thing worth mentioning is **integer division**.

The result of a division in Java depends on the types of the operands. If both operands are integers, the result will also be an integer. The unintended use of integer division can therefore result in a significant loss of precision. For Java to perform a real division (and get a real number as the result), at least one of the operands must be of real type.

For example, 3 / 2 ≡ 1 and 2 / 3 ≡ 0, because this is integer division. However, 3 / 2. ≡ 1.5 and 2.0 / 3 ≡ 0.66666666… because 2. and 2.0 are real numbers.

If k and n are variables of type int, k/n is integer division. To perform a real division over two integer variables or expressions you should force Java to treat at least one of them as real. This is done by **type casting**: you need to write the name of the type you are converting to before the variable in parentheses, for example (double)k/n will be real division with result of type double.

Integer division is often used in conjunction with the remainder operation to obtain the row and column of the item from its sequential index. For example, suppose you have a collection of 600 items, such as seats in a theater, and you want to arrange them in 20 rows, each row containing 30 seats. The expressions for the number of seats in a row and the row would be:

Seat number: index % 30 (remainder of division of index by 30: 0 - 29)
Row number: index / 30 (integer division of index by 30: 0 - 19)

where index is between 0 and 599. For example, the seat with index 247 will be in the row 8 with seat number 7.

The power operation in Java does not have an operand (if you write a^b this will mean bitwise OR and not power). To perform the power operation you need to call the pow() function:

pow( a, b ) ≡ ab

Java supports several useful shortcuts for frequent arithmetic operations over numeric variables. They are:

> i++ ≡ i = i+1 (increment i by 1)
> i-- ≡ i = i-1 (decrement i by 1)
> a += 100.0 ≡ a = a + 100.0 (increase a by 100.0)
> b -= 14 ≡ b = b - 14 (decrease b by 14)

Although these shortcuts can be used in expressions, their evaluation has effect, it changes the value of the operands.
