*来源 (Source): <https://anylogic.help/advanced/code/arrays-collections.html>*

---

# Java arrays and collections

Java offers two types of constructs where you can store multiple values or objects of the same type: arrays and collections (for System Dynamics models AnyLogic also offers HyperArray, also known as “subscripts”, — a special type of collection for dynamic variables).

**Array or Collection**? Arrays are simple constructs with linear storage of fixed size, and therefore they can only hold a given number of elements. Arrays are built into the core of the Java language, and array-related Java syntax is very simple and straightforward, for example, the nth element of the array can be obtained as array[n-1]. Collections are more complex and flexible. First of all, they are resizable: you can add any number of elements to a collection. A collection will automatically handle deleting an element from any position. There are several types of collections with different internal storage structure (linear, list, hash set, tree, and so on) and you can choose a collection type that best suits your problem so that your most common operations will be convenient and efficient. Collections are Java classes and the syntax for getting, for example, the n-th element of a collection of type ArrayList is collection.get(n).

![](https://anylogic.help/advanced/code/images/arrays_collections.png)Java arrays and collections

Indices in Java arrays and collections start with 0, not 1! In an array or collection of size 10, the index of the first element is 0, and the index of the last element is 9.
