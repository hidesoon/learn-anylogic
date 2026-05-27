*来源 (Source): <https://anylogic.help/advanced/code/variable-declaration.html>*

---

# Variable declaration

Variable declarations are discussed in the [Variables](variables.md) section. There are two forms of syntax:

```
<type> <variable name>;
<type> <variable name> = <initial value>;
```

Examples:

```
double x;
Person customer = null;
ArrayList<Person> colleagues = new ArrayList<Person>();
```

Keep in mind that:

* A local variable must be declared before it is used first.
* A local variable declared within a block {…} or a function body exists only while this block is being executed.
* If the name of a variable declared in a block or function body is the same as the name of the variable declared in an enclosing (higher level) block or of the current class variable, the lower level local variable is meant by default when the name is used. We however strongly recommend to avoid duplicate names.

The image below illustrates the code areas where local variables exist and can be used.

![](https://anylogic.help/advanced/code/images/code_areas.png)Code areas where local variables exist and can be used
