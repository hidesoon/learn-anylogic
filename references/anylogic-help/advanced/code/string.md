*来源 (Source): <https://anylogic.help/advanced/code/string.html>*

---

# String expressions

Strings in Java can be concatenated by using the + operator. For example:

> "Any" + "Logic" results in "AnyLogic"

Moreover, this way you can compose strings from objects of different types. The non-string objects will be converted to strings and then all strings will be concatenated into one. This is widely used in AnyLogic models to display the textual information on variable values. For example, in the dynamic property field **Text** of the [**Text**](https://anylogic.help/anylogic/presentation/text.html) element you can write:

> "x = " + x

And then at runtime the **Text** element will display the current value of x in the textual form, for example:

> x = 14.387

You can use an empty string in such expressions as well: "" + x will simply convert x to a string.

Another example. Consider the following string expression:

> "Number of destinations: " + destinations.size() + "; the first one is " + destinations.get(0)

When evaluated, it will produce a string like this:

> Number of destinations: 18; the first one is London

To compare strings, use the equals() function, not the == operator!
