*来源 (Source): <https://anylogic.help/advanced/code/conditional.html>*

---

# Conditional operator ? :

Conditional operator is helpful when you need to use one of the two different values in an expression depending on a condition. It is a ternary operator, meaning it has three operands:

<condition> ? <value if true> : <value if false>

It can be applied to values of any type: numeric, boolean, string, any class. The following expression evaluates to 0 if the backlog contains no orders, otherwise it evaluates to the amount of the first order in the backlog queue:

backlog.isEmpty() ? 0 : backlog.getFirst().amount

Conditional operators can be nested. For example, the following code line prints the level of income of a person (High, Medium, or Low) depending on the value of the variable income:

traceln( "Income: " ( income > 10000 ? "High" : ( income < 1500 ? "Low" : "Medium" ) ) );

This single code line is equivalent to the following combination of "if" statements:

```
trace( "Income: " );
if( income > 10000 ) {
  traceln( "High" );
} else if( income < 1500 ) {
  traceln( "Low" );
} else {
  traceln( "Medium" );
}
```
