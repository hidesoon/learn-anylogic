*来源 (Source): <https://anylogic.help/advanced/code/jni-jna.html>*

---

# Native code in AnyLogic: JNI and JNA

* [JNI framework in AnyLogic models](#jni)
* [Using the JNA library](#jna)
* [Exporting models containing native method calls to AnyLogic Cloud](#exporting-models-containing-native-method-calls-to-anylogic-cloud)

Being basically Java applications, AnyLogic models are able to interact with the **native** libraries, written in C or C++, for example, those provided by the operating system. This means you have the option to enrich your models with C/C++-based functions and capabilities.

In this article, you will learn how to call methods of native libraries in Java. We will focus on the [Java Native Integration](https://en.wikipedia.org/wiki/Java_Native_Interface) (JNI) framework available in Java and the third-party JNA library — but of course, there are other ways to call native methods from Java code, so you can choose whatever is more convenient for you.

Addressing native applications and libraries from within Java code is a complex topic that requires an understanding of basic Java principles and naming conventions. Consider [reading about Java in AnyLogic in general](general.md) before proceeding.

If you want to learn how to integrate external Java libraries into your models, see [Adding External Java Classes](../libraries/adding-external-jar-files-and-java-classes.md).

### JNI framework in AnyLogic models

The JNI framework allows for accessing native functions of DLL, SO, and DYLIB/JNILIB libraries by using the native keyword. This may be useful in various cases:

* When you need to employ hardware capabilities
* If a native-code solution performs better in a process that requires high computing power
* Your company owns a custom-built library and there is no need to rewrite it in Java

The JNI framework addresses these problems by introducing a bridge between the code implemented in Java and native code. This may be used to your advantage in the context of AnyLogic models.

To implement JNI methods in your model

1. Make sure to address the [preliminary requirements](#jni-requirements).
2. Prepare the [native methods](#jni-native-code) for JNI.
3. Load the [native library](#jni-load) into your Java code.
4. Call the native methods [from the model](#jni-address).

#### JNI: Preliminary requirements

If you are familiar with JNI, you know that the JNI-ready library files (DLL, SO, DYLIB/JNILIB) are built with naming conventions in mind — that is, all classes and methods within these files are named in accordance with strict rules which are determined in the header files.

That being said, using JNI to address DLL files requires that the name of the model Java package, as well as the names of custom interfaces, classes, and methods declared within your model, **should be identical** to the name of the Java package, interfaces, classes, and methods specified in the DLL file.

To work around these restrictions, consider using the [JNA library](#jna).

To use native methods within your AnyLogic models, make sure to prepare these methods first.

To implement usable methods in native code

1. Compose C/C++ source files that will build a DLL, SO, or DYLIB/JNILIB file (depending on the platform you use)
2. Make sure that the compiler you want to use for these source files has access to the JNI headers, which are located within the Java installation directory on your machine
3. Write the Java method signatures for the native methods you plan to use
4. Run the javac tool with the -h flag to compile Java files and create C header files, or
   Run the standalone javah tool available in older versions of Java — this tool is designed specifically for generating header files
5. Provide your C/C++ source files with access to newly created header files
6. Within your C/C++ source files, write the native implementations of the methods you want to use
7. Compile C/C++ source files into a DLL, SO, or DYLIB/JNILIB file

After performing these steps, you will have the library file ready for use in AnyLogic models.

If you are interested to learn more about the process of building JNI-ready library files, consider visiting one of these websites: [Baeldung](https://www.baeldung.com/jni); [Nanyang Technological University of Singapore](https://www3.ntu.edu.sg/home/ehchua/programming/java/JavaNativeInterface.html). The development of such libraries is described there thoroughly. Also, check the [technical specification](https://docs.oracle.com/javase/8/docs/technotes/guides/jni/) available on the Oracle website.

To load the library in the model

The simplest way to address the library file is to create a [custom class](classes.md) either from code, or the [AnyLogic GUI](adding-java-class.md).

After creating a class, you need to define a library that you would use in your model.

For example, a custom library named MultiplierLibrary contains a method named multiply(), which returns an integer value and accepts two parameters of the same int type. To address this library from AnyLogic, we would use the following code:

```
public class Multiplier {
  static{
    System.loadLibrary("MultiplierLibrary");
  }
}
```

This method loads the native library MultiplierLibrary.dll (in Windows) / libMultiplierLibrary.so (in \*nix systems) / MultiplierLibrary.jnilib (in macOS) during the model runtime. For this to work properly, the library should reside within the model directory — otherwise, you will have to specify the absolute path.

After loading the library, you need to declare a native method which you will use in your model. This should be done within the context of the same class:

native int multiply(int a, int b);

That’s it — all the necessary work for addressing the multiply() native method has been completed.

The image below demonstrates a custom class that implements the method via JNI, created from the AnyLogic GUI:

![JNI: The custom class in the AnyLogic GUI](https://anylogic.help/advanced/code/images/jni-jna-class.png)

You can specify more methods from the library associated with this class using the same procedure. For now, let’s stick with the one we have chosen.

Now that you have declared the class that uses native methods, you can use these methods anywhere in your model.

To address the native methods from the model

1. Declare an instance of your custom class, for example:

   Multiplier myMultiplier = new Multiplier();
2. Call the method of the native class and pass the necessary parameters if applicable. AnyLogic will call the method and return the result of the call, which you can then assign, for example, to a variable:

   ```
   int a = 0;
   a = myMultiplier.multiply(3, 4);
   ```

Using this procedure, you can address the native library anywhere in your model, retrieve the requested result, and then use them in calculations.

![JNI: Using the JNI method from an event](https://anylogic.help/advanced/code/images/jni-jna-event.png)

On the image above, you can see how the method we are using has been applied to an event and used to multiply values of the a and b variables.

### Using the JNA library

JNA (stands for **Java Native Access**) is a library developed by the Java community that provides Java applications with an easy way to access native libraries, omitting the need for repeating code in multiple languages and segments of code serving the only purpose of ensuring the proper work of the interface (so-called “glue code”).

JNA enables native access with its Native class — it can access libraries from the directories specified in the library’s jna.boot.library.path property and from the system library paths.

You can download the JNA library from its [GitHub repository](https://github.com/java-native-access/jna).

To learn more about development specifics, consider checking the [JNA documentation](https://java-native-access.github.io/jna/4.2.1/overview-summary.html).

To implement JNA methods in your model

1. Add the JNA library to [model dependencies](#jna-dependency).
2. Create the [Java interface](#jna-interface).
3. Call the native methods [from the model](#jna-address).

To list a library as a model dependency

1. Select the model in the **Projects** view.
2. Expand the **Dependencies** section.
3. In the **Dependencies** section, click **Add** to the right of the **Jar files and class folders required to build the model** table.
4. In the dialog box that appears, select **Java Archive File (\*.jar, \*.zip)** as **Type**, then specify the location of the jna.jar archive file in the **File** edit box. You can refer to the files using either absolute or relative paths.
   You can also click **Browse** and navigate to the package manually in the subsequent dialog.
5. To import jna.jar to the model folder, select the **Import to model folder** option. By importing the Java archive file to the model folder, you make this model easily portable — to deliver the model to someone else, you just need to copy the whole model folder.
   In case you have multiple models accessing **jna.jar**, consider the **Access file(s) from original location** option. In this case, the JAR file will not be copied to the model folder, and the model will access the file from its specified location.
6. Click **Finish**. Once the operation completes, the jna.jar file will appear in the model’s **Resource** folder in the **Projects** view.

![JNA: The list of model dependencies](https://anylogic.help/advanced/code/images/jni-jna-dependencies.png)

Now that the necessary Java archive is attached to your model, you need to refer to it to access its methods. To do that, you need to implement the interface that will be used to address these libraries.

To create an interface for the JNA library

1. In the **Projects** view, right-click (macOS: Ctrl + click) the model item you are currently working with, and choose **New > Java Interface** from the popup menu.
2. The **New Java Interface** dialog box opens up.
3. Specify the name of the new Java interface in the **Name** field and click **Finish** to complete the process.
4. The Java editor opens up. Use it to write Java code for the interface you have just defined.
5. Before entering the interface code, specify the following:

   ```
   import com.sun.jna.Library;
       import com.sun.jna.Native;
   ```

   With this code, you import the needed packages from jna.jar. After that, you can refer to the classes and methods you wish to call by simply addressing their names.
6. Your interface will extend the Library interface provided by JNA — and subsequently, map Java methods to C/C++ methods. To implement this, use the following code:

   ```
   public interface MyInterface extends Library {
       MyInterface INSTANCE = (MyInterface) Native.loadLibrary("<library>", MyInterface.class);
       }
   ```

   In the example above, MyInterface is a custom name of the interface. You can replace it with the one of your choosing.

   The Native.loadLibrary() method addresses the Native Java package of JNA and calls its loadLibrary() method to point out the C/C++ library file you want to access. The string you are passing to this method is the name of the C/C++ library file.
7. Next, within the interface, you need to declare the following explicitly:
   * Which methods of the C/C++ library you want to use
   * Which types do these methods’ parameters have
   * Which types do values, returned by these methods, have

Say, we have a C++ library randomint. It has an implementation of the randomNumber() method, which accepts an integer as a parameter, and then generates a random number between 0 and the integer passed as the parameter.

The source code of the method in C++ would look as follows:

```
int randomNumber(int bound) {
return rand() % bound;
}
```

Depending on the operating system, the compiled library will have one of the following names:

* randomint.dll (Windows)
* librandomint.so (Linux)
* randomint.dylib (macOS).

Regardless of which operating system you use, the interface that interacts with this library will look something like the following:

```
public interface MyInterface extends Library {
  MyInterface INSTANCE = (MyInterface) Native.loadLibrary("randomint", MyInterface.class);
  int randomNumber(int bound);
  }
```

Your interface is ready.

![JNA: Import statements and the implementation of the interface](https://anylogic.help/advanced/code/images/jni-jna-import.png)

You can now address the methods you have declared within it and refer to them from your code.

To address the native methods from your model

1. For example, let’s declare an integer:

   int a = 0;
2. To use the method from the library file, simply call this method after referring to the instance of the interface you declared in the previous step. Don’t forget to pass an integer as a parameter.
   The integer you receive with the method call is a regular integer, so you can assign it to a variable:

   a = MyInterface.INSTANCE.randomNumber(5);
3. Then, you can print it in the **Console** view:

   traceln(a);

   ![JNA: Calling a native method with JNA](https://anylogic.help/advanced/code/images/jni-jna-startup.png)
4. You can now run the model. When the model processes this code in runtime, the random number will be printed in the **Console** view:

   ![JNA: The method call result in the Java console](https://anylogic.help/advanced/code/images/jni-jna-console.png)

### Exporting models containing native method calls to AnyLogic Cloud

Since [AnyLogic Cloud](https://anylogic.help/cloud/cloud-overview.html) is a Linux application, the models that employ method calls to DLL or DYLIB/JNILIB libraries may not work there. Still, using native methods is an option as long as you use the native methods included in \*nix-specific libraries (\*.so files).

This functionality is available for [Private Cloud](https://anylogic.help/cloud/private-cloud.html) instances only.

To use native methods in models you export to AnyLogic Cloud:

* Make sure the required methods reside within SO files
* Attach these SO files to the model as [file resources](https://anylogic.help/anylogic/connectivity/resources.html)
* In file resource properties, make sure the **Resource is referenced from user code** checkbox is selected

If these prerequisites are met, [export the model](https://anylogic.help/cloud/export-cloud.html) to the Private Cloud instance as usual. The model should run in Private Cloud with no issues.

If your model employs the JNA library as a dependency, make sure to upload its JAR, as well.
