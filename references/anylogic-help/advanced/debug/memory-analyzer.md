*来源 (Source): <https://anylogic.help/advanced/debug/memory-analyzer.html>*

---

# Memory analyzer

* [Using the memory analyzer](#example-use)
* [Memory overview](#memory-overview)
* [Additional tools](#additional-tools)
  + [Actions](#actions)
  + [Reports](#reports)
  + [Step by step](#step-by-step)
  + [Query browser](#query)

[Runtime errors](runtime-errors.md)[Stepping through the execution of a model](stepping-execution.md)[Keeping track of a simulation](keeping-track-of-a-simulation.md)

Since AnyLogic model is essentially a Java application, it is useful to take a programming-like approach when designing a model. For example, if your model uses more memory than it should, it may slow down or even crash; this can happen due to memory leaks, where unneeded memory is not properly freed.

To identify such problems, AnyLogic includes the built-in model memory analyzer, which allows you to find memory leaks in your model and reduce memory consumption. It can be started during the model execution. Upon receiving the command to open the memory analyzer, AnyLogic gets the ID of the running model process, dumps it, and opens the editor to display it.

The memory analyzer is not available in AnyLogic PLE.

To open the memory analyzer

1. Run the model.
2. In the [AnyLogic menu](https://anylogic.help/anylogic/ui/menu.html), select **Model** > **Memory dump**.

This will open the new tab in the editor that contains the memory snapshot of the running model.

![AnyLogic: The memory analyzer tab](https://anylogic.help/advanced/debug/images/memory-analyzer.png)

Opening the memory analyzer does not stop the model process, so you can open it multiple times for a single model run.

## Using the memory analyzer

How and when do you use the memory analyzer? You can try to open a model (not necessarily one with problems) and try to identify which objects are using the most memory. You may encounter abstract and obfuscated AnyLogic class names that are difficult to understand. You may feel if you cannot find your agents, shapes, and other objects, and you may struggle to understand how to use this information.

It is important to remember that many of the objects in the model are part of AnyLogic’s internal structure, and no matter how large these objects may be, they are part of AnyLogic’s internal workings, and there is nothing you can do to change them.

The easiest way to identify the really problematic elements of the model is as follows:

1. Before running the model, go to the properties of the model by clicking on its name in the **Projects** view.
2. In the **Advanced** section of the properties, check the model’s Java package name in the **Package** edit box. Remember it.
3. Run the model.
4. While the model is running, create a memory heap dump by selecting **Model** > **Memory dump**.
5. After a short time, a dump is generated and opened. From there, you can navigate to more specific results. Click **Histogram** either from the view’s toolbar, or from the options below the view.
6. The histogram is generated immediately, but we need to narrow down the results so that we don’t get confused by standard Java objects and AnyLogic internal elements.
   To filter the histogram results, type the name of the model’s Java package in the top cell of the **Class Name** column. Although it says Regex, you don’t need to build the actual regular expression: just the package name will work fine.
7. Then, you will see the filtered results. For example, here’s what it looks like for one of the sample models, **Job Shop**:

   ![AnyLogic: Memory analyzer: The Job Shop model memory dump](https://anylogic.help/advanced/debug/images/memory-analyzer-dump.png)

   As you can see, the histogram contains:
   * The total number of instances of a particular object.
   * The **shallow heap** is th e memory consumed by a single object of that type at the moment the dump was created.
     This is the amount of memory that is consumed by an object, which is its footprint in the Java machine memory. It is determined by the size of the data types it uses.
   * The **retained heap** is the total memory that is freed when an object is garbage collected. It includes the memory of the object itself (its shallow heap) plus the memory of any other objects that are only accessible through that object and would also be removed when the object is garbage collected. In other words, it is the sum of the shallow sizes of all objects that the object keeps alive in the memory.By understanding and analyzing these aspects of your model’s memory usage, you can make informed decisions about optimizing and fine-tuning your objects. This can lead to significant reductions in memory consumption, improving the efficiency and performance of your model.

## Memory overview

After running the memory analyzer, you will see the overview page.

The right side of the page shows the size of the memory dump, as well as the number of classes, objects, and class loaders. If the total size of the dump is much smaller than the size of the model JAR file, it is possible that the heap dump contained many garbage objects that would be discarded at the next garbage collection.

The chart shows the largest objects in the dump. Move your mouse over a slice to see the details of the objects. Click ![AnyLogic: Icon: Query browser](https://anylogic.help/advanced/debug/images/memory-query.gif) to open the [query browser](#query) to drill down and get more specific results.

## Additional tools

There are a number of additional tools available for the memory analyzer: both from the overview toolbar and in the panes below.

### Actions

* **Histogram** — Lists the number of instances per class, their flat size (the memory consumed by each object), and the retained size (the memory consumed after the Java garbage collector performs the cleanup).
  While viewing the histogram, you can also get more specific details about each object from the context menu.
  In addition, the histogram allows you to group objects by class, class loader, package, or superclass.
* **Dominator tree** — Displays the largest objects in the heap dump, including references to their dependent objects. The dependent objects are those that will be removed by the Java garbage collector if you remove references to them from their parent objects.
* **Top consumers** — Displays which classes, class loaders, and packages consume the most memory.

### Reports

* **Leak suspect report** — Identifies potential memory leaks. It starts with a dominator tree, where the largest items are examined first. If an item uses more than 10% of memory (where 10% is a default value), it could be a leak source. Sometimes, many small objects of the same type take up a lot of memory together, forming another type of leak. Each suspect is then analyzed further.
  If the suspect is a thread, the report shows its call stack and relevant frames. If it’s a class loader or a class, the report marks it as a part of the model worth investigating.
* **Leak suspect report by snapshot comparison** — Similar to the leak suspect report, but allows you to select an outer snapshot to act as a baseline. The two snapshots are then compared, and the potential leak source is highlighted.

From the toolbar, you can also open the reports saved on your hard drive by selecting **Open report** from the ![AnyLogic: Icon: Memory report](https://anylogic.help/advanced/debug/images/memory-report.gif) drop-down list.

### Step by step

* **Component Report** — Provides an overview of each component’s characteristics, details about its size, the number of classes, objects, and different class loaders. The report also highlights the largest objects, classes, class loaders, and packages held by the component, providing insight into what the component is keeping active.

### Query browser

The query browser is a tool available either from the toolbar (the ![AnyLogic: Icon: Query browser ](https://anylogic.help/advanced/debug/images/memory-query.gif) drop-down list) or from the context menu of each summary pie chart segment.

It offers a number of options, all of which provide insights into different aspects of the memory snapshot:

* **List Objects** and **Show Objects by Class** provide organized view of the model elements.
* **Path To GC Roots** and **Merge Shortest Paths to GC Roots** are related to memory management and garbage collection.
* **Java Basics** and **Java Collections** provide means to manage Java-based objects.
* **Leak Identification** provides access to various utilities for identifying the memory leak, including but not limited to those described above.
