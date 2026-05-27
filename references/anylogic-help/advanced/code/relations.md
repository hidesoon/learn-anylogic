*来源 (Source): <https://anylogic.help/advanced/code/relations.html>*

---

# Relations and equality

Relations between two numeric expressions are determined using the following operators:

|  |  |
| --- | --- |
| > | greater than |
| >= | greater than or equal to |
| < | less than |
| <= | less than or equal to |

You can test if two operands (primitive or objects) are equal using the following two operators:

|  |  |
| --- | --- |
| == | equal to |
| != | not equal to |

For non-primitive objects (that is, those that are not numeric or boolean) the operators == and != test if the two operands are the same object rather than two objects with equal contents. To compare the contents of two objects, for example, two strings, you should use the function equals().

For example, to test if the string message msg equals "Wake up!" you should write:

msg.equals( "Wake up!" )

Do not confuse the equality operator == with the assignment operator =!

a = 5 means assign value of 5 to the variable a, whereas
a == 5 is true if a equals 5 and false otherwise

The result of all comparison operations is of boolean type (true or false).
