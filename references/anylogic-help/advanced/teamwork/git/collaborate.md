*来源 (Source): <https://anylogic.help/advanced/teamwork/git/collaborate.html>*

---

# Collaborating with other developers

* [Retrieving changes from the remote repository](#retrieving-changes-from-the-remote-repository)
* [Pushing changes](#push)

[Branching](branch.md)

When you use Git with others, you work in a distributed environment where each contributor maintains their version of the project. Using Git’s features, people can combine their changes by pulling changes from others, merging or rebasing as needed, and pushing the changes to the remote repository.

If you are working on a model as a team, it’s important to commit changes frequently and keep your local repository in sync with the remote one.

This article covers the basic tasks that are required for proper AnyLogic teamwork using Git.

## Retrieving changes from the remote repository

The common scenario of synchronizing changes with the remote repository involves fetching and pulling.

Fetching ensures that information about the branches and commits present in your repository is updated. You use this command to view the changes that other developers have made to the model from your local copy of the repository, and decide whether or not you want to incorporate them into your work yet.

You pull changes when you are on the same branch with other people and they may have already made some commits with changes that could affect your work. Without pulling, you might miss important updates, and your work might become outdated or incompatible with the rest of the team’s progress.

You can see how many commits you have not pulled by looking at the down arrow next to the repository’s name in the [**Git Repositories** view](repositories.md). Fetch changes regularly.

To fetch the changes from the remote repository

1. Locate your repository in the [**Git Repositories** view](repositories.md).
2. Right-click the name of the repository.
3. Select **Fetch from origin** from the context menu.

To pull the changes from the remote repository

1. Locate your repository in the [**Git Repositories** view](repositories.md).
2. Right-click the name of the repository.
3. Select **Pull** from the context menu. This will automatically download all the commits in your currently checked out branch and apply them to your local copy of the repository.
   The pull may be unsuccessful if there is a conflict between your local copy of the repository and the remote commit. In this case, consider committing your changes to a spun-off branch and then [merge two branches](branch.md#merge).
4. You may also want to perform a non-standard pull. In this case, select the **Pull…** (with ellipsis) option from the context menu.
   This brings up a dialog where you can configure a different repository as the source for the branch, replace the reference, and choose a different [upstream configuration](branch.md#upstream).

   ![AnyLogic: The Pull dialog](https://anylogic.help/advanced/teamwork/git/images/pull-dialog.png)

## Pushing changes

After you have made one or multiple local commits into your branch, it is a good idea to push them to the remote repository so that other developers are aware of the work and changes you have done.

In some cases, you may want to push as soon as you [create a commit](commit.md#create); if there are no conflicts, this can easily be done with the **Commit and Push** button in the **Git Staging** view.

You can see how many local commits you have not yet pushed by looking at the number with the up arrow next to the repository name in the [**Git Repositories** view](repositories.md).

To push changes to the remote repository

1. Locate your repository in the [**Git Repositories** view](repositories.md).
2. Right-click the name of the repository.
3. Select **Push to origin** from the context menu.
   If there are no problems and push is performed to a remote tracking branch, it requires no further parameters and no additional dialog is show.
   The push may fail if there is a conflict between your local copy of the repository and the remote. In this case, consider committing your changes to a spun-off branch and then [merging two branches](branch.md#merge).
