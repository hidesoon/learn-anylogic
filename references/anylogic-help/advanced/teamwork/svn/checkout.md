*来源 (Source): <https://anylogic.help/advanced/teamwork/svn/checkout.html>*

---

# Checkout from SVN

Checkout is the term used to describe the process of making a copy of a project from a repository into your local workspace.

Having created a working copy of a project being stored in SVN repository, you can work with this project following the [recommended SVN work cycle](work-cycle.md) — update latest changes from SVN, edit the project and commit your changes to the repository so that they become available to other developers.

To checkout a project from SVN repository

1. Choose **File > SVN > ![](https://anylogic.help/advanced/anylogic/ui/images/toolbars/Checkout_edit.gif)Checkout...** from the main menu. You will see the
   **Checkout from SVN** wizard that will help you to check out models from a SVN repository.
2. Before you can begin working with a SVN repository, you must define that repository location in your AnyLogic IDE. The first page of the checkout wizard allows you to specify the repository where the project you want to check out is stored. You can choose an existing repository location or create a new one:

   ![](https://anylogic.help/advanced/teamwork/svn/images/checkout_1b.png)
3. If you have already defined the required SVN repository in AnyLogic IDE, you can just choose the **Use existing repository location**
   option, then choose the required repository URL from the list below and finally click **Next**.
4. Otherwise, if you have not yet defined a connection to your repository, you will need to create a new repository location. In this case choose the **Create a new repository location** option and click **Next**. The page like shown on the next figure will be opened. It prompts you for a repository location URL. Enter the URL of the repository you want to connect to and the authentication information. Once you click
   **Next**, the wizard will create the location.

   ![](https://anylogic.help/advanced/teamwork/svn/images/checkout_svn_2a.png)
5. After a repository location is selected, you can now choose a module to check out. On the next page of the wizard, expand the location to see the contents for the given URL.
6. In the **Select the target directory** field, specify the directory where the working copy of the selected project will be checked out:

   ![](https://anylogic.help/advanced/teamwork/svn/images/checkout_2b.png)
7. Click **Finish**. The working copy of the selected folder will be checked out to the target directory you have specified and the **Open** dialog will be opened showing you the contents of this folder. You can open the required model directly from there and it will be opened in AnyLogic workspace. Now you can work with the checked out project following the [recommended SVN work cycle](work-cycle.md) — update latest changes from SVN, edit the project and commit your changes to the repository so that they become available to other developers.
