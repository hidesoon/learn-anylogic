*来源 (Source): <https://anylogic.help/advanced/code/access.html>*

---

# Accessing model elements from code

In AnyLogic, you do not write the complete code of Java classes from start to finish. Instead, you enter snippets of code and expressions into numerous small edit boxes in the properties of various model elements. Therefore, it is important to always understand where exactly you are writing the code (what class and method it belongs to) and how you can access other model elements from there.

![](https://anylogic.help/advanced/code/images/232.png)

Most of the code you write when you develop models is the code of an agent type, more precisely it is the code of one of the agent type methods. No matter whether you are defining an action of an event, setting parameter of an embedded object, or writing a startup code — you can assume you are writing the code of the current agent type. Therefore the following rules apply (see the figure above):

* The model elements of the same agent type are accessed simply by their names (because they are the fields of the same class). Say, you are in the **Action** field of the event endOfFY of agent type Company. To access the embedded object queue you simply write queue. To increase the revenue variable you write revenue = amount. And to restart the endOfFY event from its own action you should write endOfFY.restart( year() ).
* To access an element of an embedded object you should put dot . after the embedded object name and then write the element name. For example, to obtain the size of the queue object you write queue.size(). If the embedded object is replicated, its name is the name of a collection of objects and you should specify which one exactly you want to access. To call the performance() function of the employee number 247 among employees of the company you should write: employees( 246 ).performance().
* To access the container of the current object (the object where this object is embedded) you call class of the container object. For example, if an object of the Company type is embedded into Main, you should write main. to get to Main from within Company. Consequently, to call the announceSale() function of Main you write main.announceSale(). There is a function getOwner() that also returns the container object, but its return type is Agent — the base class of Main, Company, etc. You will need to cast it to Main before accessing the Main-specific things. getOwner() is useful when we do not know where exactly the current object is embedded.
* To access a “peer” object (the object that shares the container with the current one) you should first get up to the container object and then get down to another embedded object. To access a customer’s loyalty from a company in the Figure, we need first to get to Main and then to Customer (with particular index): main.customers(i).loyalty.
* These rules naturally extend to the whole hierarchical structure of AnyLogic model. You can access anything from anywhere. We however recommend to develop your models in a modular way as much as possible so that the objects know minimum internals of other objects and setup and communication is done through parameters, ports, message passing, and calls of “public” functions.
