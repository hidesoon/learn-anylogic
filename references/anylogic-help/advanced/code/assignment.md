*来源 (Source): <https://anylogic.help/advanced/code/assignment.html>*

---

# Assignment

To assign a value to a variable in Java, write:

```
<variable name> = <expression>;
```

Remember that = means assignment action, whereas == means equality relation.

**Examples**:

```
distance = sqrt( dx*dx + dy*dy ); // calculate distance based on dx and dy
k = uniform_discr( 0, 10 ); // set k to a random integer between 0 and 10 inclusive
customer = null; // “forget” customer: reset customer variable to null (“nothing”)
```

The shortcuts for frequently used assignments can be executed as statements as well (see [Arithmetic expressions](expressions.md)), for example:

```
k++ ; // increment k by 1
b *= 2; // b = b * 2
```
