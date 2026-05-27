*来源 (Source): <https://anylogic.help/advanced/teamwork/svn/share.html>*

---

# Import a new project into an SVN repository

**SVN > Share** is the process for importing a project into a SVN repository so that it can be managed by SVN. You share your project when you have already been using SVN and you have an existing working copy in your workspace that you want to connect to SVN.

To share (import) a project into SVN repository

1. Right-click (macOS: Ctrl + click) the model item (the item of the uppermost level) in the **Projects** tree and choose **SVN > ![](https://anylogic.help/advanced/teamwork/svn/images/Import_edit.gif) Share...** from the context menu, or
   Select any element of the model and choose **File > SVN > ![](https://anylogic.help/advanced/teamwork/svn/images/Import_edit.gif) Share...** from the main menu.
2. You will see the **Share Project** wizard. First of all, you should specify the repository location where you want to add your project. On the first page of the **Share Project** wizard you can choose an existing repository location or create a new one.

   AnyLogic supports the svn://... protocol only. Direct repository access via file://... URL is not applicable.
3. If you have not yet defined a connection to your repository, you will need to define the connection to a new repository location in AnyLogic. The wizard’s page will prompt you for a repository location URL. Enter the URL of the repository you want to connect to and the authentication information. Once you click **Next**, the wizard will store the information about this new repository location in AnyLogic IDE.

   ![](https://anylogic.help/advanced/teamwork/svn/images/share_2b.png)
4. If you have already defined the repository location where you want to add your project, choose the **Use existing repository location** option, select the repository URL in the list below and click **Next**.

   ![](https://anylogic.help/advanced/teamwork/svn/images/share_1.png)
5. On the next step you must specify the folder where you want to store the project. The folder name is relative to the URL of the repository location you have specified in the previous step. All intermediate folders must already exist in the repository, but the final folder name must not already exist. You may simply **Use project name as folder name**. Or you can select the **Use specified folder name** and click the **Select...** button to select a path from within the repository. Click **Next** when you are through.

   ![](https://anylogic.help/advanced/teamwork/svn/images/share_2.png)
6. The final page of the wizard is just a final confirmation page. Here you can enter a comment to associate with the commit or choose a previously entered comment from the list. When you ready, click **Finish** to complete the import operation.

   ![](https://anylogic.help/advanced/teamwork/svn/images/share_3.png)
7. If you have not specified your authentication information in the wizard, you will be asked for your username and password required for the connection with the specified SVN repository. Finally your project will be added into SVN repository.
