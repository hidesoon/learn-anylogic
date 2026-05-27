*来源 (Source): <https://anylogic.help/advanced/code/block.html>*

---

# Block {…} and indentation

A **block** is a sequence of statements enclosed in braces {…}. There can be one, several, or even no statements inside a block. The block tells Java that the sequence of statements should be treated as one single statement, and therefore blocks are used with if, for, while, and so on.

Java code conventions recommend to place the braces on separate lines from the enclosed statements and use **indentation** to visualize the nesting level of the block contents:

![](https://anylogic.help/advanced/code/images/indentation.png)

If the block is a part of a decision or loop statement, the braces can be placed on the same line with if, else, for, or while:

```
if( … ) {
  <statements>
} else {
  <statements>
}

while( … ) {
  <statements>
}
```

In a switch statement, it is recommended to not indent the lines with case:

```
switch( … ) {
case …:
  <statements>
  break;
case …:
  <statements>
  break;
…
}
```
