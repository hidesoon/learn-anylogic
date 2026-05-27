*来源 (Source): <https://anylogic.help/advanced/code/collections.html>*

---

# Collections

* [Array list](#array-list)
  + [Functions](#functions)
  + [Examples](#examples)
* [Linked list](#linked-list)
  + [Functions](#functions-2)
  + [Example](#example)
* [Declaring collections](#declaring-collections)
* [Selecting a collection type](#selecting-a-collection-type)
* [Agent populations are collections too](#agent-populations-are-collections-too)

Collections are Java classes designed to efficiently store multiple elements of a particular type. Unlike Java arrays, collections can store any number of elements.

## Array list

The array list (the ArrayList object) is the simplest collection in AnyLogic, which you can treat as a resizable array.

The following line of code creates an initially empty array list of objects of the Person class:

> ArrayList<Person> friends = new ArrayList<Person>();

The type of the collection includes the element type in angle brackets. This “tunes” the collection to work with the specific element type, so that, for example, the get() function on friends will return an object of type Person.

### Functions

The array list provides the functions listed below. For a complete description of the API, see the [AnyLogic Class reference](elements-api.md).

Some of the functions below are relevant to the example above, which has Person objects as the elements that make up the array list. To use them in your own array lists, specify the appropriate object type.

| Function | Description |
| --- | --- |
| int size() | Returns the number of elements in the list. |
| boolean isEmpty() | Tests if this list is empty. |
| Person get(int index) | Returns the element at the specified position in this list.   index — The position of the element to retrieve. |
| boolean add(Person p) | Appends the specified element to the end of the list.   p — The element to add. |
| Person remove(int index) | Removes the element at the specified position in this list.   index — The position from which to remove the element. |
| boolean contains( Person p ) | Returns true if this list contains the specified element.   p — The element to test for. |
| void clear() | Removes all elements from the list. |

### Examples

* The following code fragment tests whether the friends list contains the person victor, and if it does not, adds victor to the list:

  ```
  if(!friends.contains(victor))
    friends.add(victor);
  ```
* All collection types support iteration over elements. The easiest way to iterate is to use a for loop.
  Suppose the Person class has an income field. The following loop prints all friends with income greater than 100000 to the model log:

  ```
  for(Person p : friends) {
    if(p.income > 100000)
      traceln(p);
  }
  ```

## Linked list

The linked list (the LinkedList object) is an another popular collection type.

Linked lists are used to model stack or queue structures, which are sequential stores where elements are primarily added and removed from one or both ends.

Consider a model of a distributor that maintains a backlog of orders from retailers. Let’s say there is an Order class with the amount field. The backlog (essentially a FIFO queue) can be created with the following code:

> LinkedList<Order> backlog = new LinkedList<Order>();

### Functions

The LinkedList object supports functions common to all collections (such as size() or isEmpty()), and also provides its own API.

The functions below are relevant to the example above, which has Order objects as the elements that make up the linked list. To use them in your own linked lists, specify the appropriate object type.

| Function | Description |
| --- | --- |
| Order getFirst() | Returns the first element in the list. |
| Order getLast() | Returns the last element in the list. |
| addFirst(Order o) | Inserts the specified element at the beginning of the list.   o — The element to insert. |
| addLast(Order o) | Appends the specified element to the end of the list.   o — The element to append. |
| Order removeFirst() | Removes the first element from the list and returns it. |
| Order removeLast() | Removes the last element from the list and returns it. |

### Example

Suppose that when a new order is received by the distributor, it is placed at the end of the backlog:

> backlog.addLast(order);

Each time the inventory is replenished, the distributor tries to ship the orders starting at the top of the backlog. If the amount in an order is greater than the remaining inventory, the order processing stops. Order processing may look like this:

```
while(!backlog.isEmpty()) { // repeat the following code while the backlog is not empty
  Order order = backlog.getFirst(); // pick the first order in the backlog
  if(order.amount <= inventory) { // if there is enough inventory to fulfill this order
    ship(order); // ship
    inventory -= order.amount; // reduce available inventory
    backlog.removeFirst(); // remove the order from the backlog
  } else { // not enough inventory to ship
    break; // stop processing the order backlog
  }
}
```

## Declaring collections

We recommend that you declare collections graphically in agents and experiments. The **Collection** object is located in the **Agent** palette. All you need to do is to drop it on the canvas and select the collection and the element types. At runtime, you can view view the contents of the collection by clicking its icon.

![](https://anylogic.help/advanced/code/images/collections.png)Graphically declaring a Java collection

## Selecting a collection type

Different collection types have different **time complexity** of operations. For example, checking whether a collection of 10,000,000 objects contains a given object may take 80 milliseconds for ArrayList, 100 milliseconds for LinkedList, and less than 1 millisecond for HashSet and TreeSet. To ensure maximum efficiency of the model execution, you should analyze which operations are most frequent and choose the collection type accordingly. The table below shows the time complexity of the most common operations for four collection types.

| Operation | ArrayList | LinkedList | HashSet | TreeSet |
| --- | --- | --- | --- | --- |
| Obtain size | Constant | Constant | Constant | Constant |
| Add element | Constant | Constant | Constant | Logarithmic |
| Remove given element | Linear | Linear | Constant | Logarithmic |
| Remove by index | Linear | Linear | — | — |
| Get element by index | Constant | Linear | — | — |
| Find out if contains | Linear | Linear | Constant | Logarithmic |

The terms Constant, Linear, and Logarithmic complexity have the following meanings:

* **Linear** complexity means that the worst case time required to complete the operation grows linearly with the size of the collection.
* **Constant** means that the time to complete the operation does not depend on the size of the collection at all.
* **Logarithmic** means that the time to complete the operation grows as the logarithm of the size.

You should not treat the constant complexity as the unconditionally best choice. Depending on the size, different collection types may behave better than others.

Consider the image below. For a relatively small number of elements, the linear complexity collection may perform better than the constant complexity collection.

![](https://anylogic.help/advanced/code/images/collection_comparison.png)Depending on their size, some collection types may behave better than others

A few additional things to keep in mind when selecting a collection type:

* HashSet and TreeSet do not support element indices, so it is not possible to get an element at position 32, for example.
* TreeSet is a naturally sorted collection: elements are stored in a particular order, defined by a natural or user-specified comparator.

## Agent populations are collections too

When you create an agent population, AnyLogic creates a special type of collection to store the individual agents. You have two options:

* AgentArrayList — Select this collection type if the set of agents is more or less constant or if you need to frequently access individual objects by index.
* AgentLinkedHashSet — Select this collection type if you plan to add new agents and remove existing ones frequently. For example, if you are modeling the population of a city over a relatively long period of time, so that people are born, die, move out of the city, and new people arrive.

The options for the type of collection appear in the **Advanced** section of the properties of an agent population: see the image below.

![](https://anylogic.help/advanced/code/images/people.png)Options for the collection type of an agent population

Both types of agent collections support functions like size(), isEmpty(), get(int index), contains(Object o), and iteration. If the index of the element is not specifically needed during iteration, it is always better to use the enhanced form of the for loop:

```
for(Person p : people) {
  …
}
```
