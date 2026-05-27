*来源 (Source): <https://anylogic.help/advanced/functions/math-arrays.html>*

---

# Functions working with arrays (type[])

AnyLogic provides a set of functions aimed for working with Java arrays (storing values of primitive type: int[], double[], or instances of some Java class: Object[]).

| Function | Description |
| --- | --- |
| boolean arrayContains(double[] array, double value) | Returns true if the array contains the given value.   array — the array to scan  value — the value to search for |
| boolean arrayContains(int[] array, int value) | Returns true if the array contains the given value.   array — the array to scan  value — the value to search for |
| boolean arrayContains(Object[] array, Object object) | Returns true if the array contains the given object. Objects are compared using .equals() function. Arrays of any object type are supported. For example, the following code will print out 'true':  ``` String[] s = new String[]{"a", "b", "c"}; traceln(contains(s, "b")); ```    array — the array to scan  object — the object to search for |
| int indexOf(double[] array, double value) | Returns the index of the first occurrence of the given value in the array. Returns -1 if value not found or if passed array is null or empty.   array — the array to scan  value — the value to search for |
| int indexOf(int[] array, int value) | Returns the index of the first occurrence of the given value in the array. Returns -1 if value not found or if passed array is null or empty.   array — the array to scan  value — the value to search for |
| int indexOf(Object[] array, Object object) | Returns the index of the first occurrence of the given object in the array. Objects are compared using .equals() function. Returns -1 if value not found or if passed array is null or empty. Arrays of any object type are supported. For example, the following code will print out '1':  ``` String[] s = new String[]{"a", "b", "c"}; traceln(indexOf(s, "b")); ```    array — the array to scan  object — the object to search for, may be null - in this case the function will try to find the index of null in the given array |
| int indexOf(int[] array, IntPredicate test) | Returns the index of the first occurrence of the matching value in the array. Returns -1 if no matching value is found or if passed array is null or empty.   array — the array to scan  test — the test expression, e.g. v -> v > 10 |
| int indexOf(double[] array, DoublePredicate test) | Returns the index of the first occurrence of the matching value in the array. Returns -1 if no matching value is found or if passed array is null or empty.   array — the array to scan  test — the test expression, e.g. v -> v > 10 |
| int indexOf(T[] array, Predicate<? super T> test) | Returns the index of the first occurrence of the matching object in the array. Returns -1 if value not found or if passed array is null or empty. Arrays of any object type are supported. For example, the following code will print out '1':  ``` String[] s = new String[]{ "a", "ab", "abc" }; traceln(indexOf(s, s -> s.length() > 1)); ```    array — the array to scan  test — the test expression. If null is passed instead of predicate, the function will try to find the index of null in the given array. |
| int indexOfMax(double[] array) | Returns the index of the maximum value from the given array.   array — the array to scan |
| int indexOfMax(int[] array) | Returns the index of the maximum value from the given array.   array — the array to scan |
| int indexOfMin(double[] array) | Returns the index of the minimum value from the given array.   array — the array to scan |
| int indexOfMin(int[] array) | Returns the index of the minimum value from the given array.   array — the array to scan |
| double max(double[] array) | Returns the maximum value from the given array. Returns Double.NaN if array contains only Double.NaN values. Throws error if passed array is null or empty.   array — the array to scan |
| int max(int[] array) | Returns the maximum value from the given array. Throws error if passed array is null or empty.   array — the array to scan |
| double min(double[] array) | Returns the minimum value from the given array. Returns Double.NaN if array contains only Double.NaN values. Throws error if passed array is null or empty.   array — the array to scan |
| int min(int[] array) | Returns the minimum value from the given array. Throws error if passed array is null or empty.   array — the array to scan |
