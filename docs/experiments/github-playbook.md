---
title: GitHub Playbook
---

# GitHub Playbook

This section contains information on how to use GitHub. The information in this
section is based on the experience of the authors of these guidelines. Note that
you don't have to follow these guidelines. You can follow any guidelines you want.
However, we recommend you to follow what is written here.

## Working Individually

When working individually, you are the architect of your project. You can follow
whatever guidelines you want. However, it is a good practice to have the following points in mind:

- **Have a structured repository.** The repository should be structured in a way
  that makes it easy to navigate and understand. For example, you can have a folder for the code, a folder for the data, and a folder for the documentation. For python projects, you can use the [cookiecutter] template.

- **Use linters to have concise code.** Linters are tools that check the code for
  errors and inconsistencies. It is good practice to set up a linter for the chosen programming language. For example, for Python, you can use [pylint].

- **Use a README file.** The README file is a file that contains information about
  the project. It should contain information about the project, how to install
  the project, how to run the project, and how to contribute to the project.
  Basically, the README file should contain all the information that a person
  needs to know to start working on the project.


## Working in a Team

When working in a team, you should follow the following guidelines:

1. **Create a team.** To create a team, go to GitHub Teams and click on the "New
   Team" button. Enter the name of the team and click on the "Create Team"
   button. Next, add the members of the team.

2. **Have a main repository.** The main repository is the repository containing
   all of the code and the documentation of the project. The main repository can
   be either private or public. If the main repository is private, make sure that
   all of the members of the team have access to it. To change that, go to the
   repository "Settings > Collaborators and teams > Manage access > Add people"  and add the members of the team as collaborators.

    !!! warning "Do not commit directly to the main repository"
        The main repository should be used only for storing the code that has
        been reviewed and approved by the team. Therefore, do not commit directly
        to it. Instead, **create a fork**.


3. **Create a fork of the main repository.** Each member of the team should create
    a fork of the main repository. A fork is a copy of the repository on which one
    can work on without worrying they will mess up the whole code base (the main
    repository also serves as a backup). To create a fork, go to the main repository and click on the "Fork" button in the top right corner. This will
    create a copy of the repository in your account.


4. **Work on the code.** To work on the code, follow the steps in [Working on the code].


## Working on the Code

Once you setup your repository, you can start working on the code. Some of the steps (2, 8-10) are specific for working in a team and are labelled as such. To start working on the code, follow the following steps:

1. **Clone the repository.** To clone the repository, run `git clone <repository-url>`.

2. **[team] Create a new remote for the main repository.** To create a new remote, run `git remote add <remote-name> <remote-url>`. The remote name should be descriptive of the remote. For example, if you are working on a project with a team, you can name the remote `team`.

2. **Create a new branch for each feature you are working on.** To create a new  branch, run `git checkout -b <branch-name>`. The branch name should be descriptive of the feature you are working on. For example, if you are
working on a feature that adds a new feature to the code, you can name
the branch `add-new-feature`.

3. **Implement the feature you are working on.** To implement the feature, edit the code.

    !!! tip "Writing documentation"
        It is a good practice to write documentation for the code you are working on. This will help you and the other team members to understand the code. You can write the documentation in the code itself or in a separate file. If you are writing the documentation in a separate file, make sure to add the file to the repository. **While the documentation is not necessary at every step of the development, it is advised to at least periodically add it to the code (after a group of features were completed).**



4. **Add the changes you made to the code.** To add the changes, run `git add    <file-name>`.

5. **Commit the changes you made to the code.** To commit the changes, run `git commit -m "<commit-message>"`. The commit message should be descriptive of
the changes you made to the code.

6. **Push the changes to remote.** Once you are done with the feature, commit the changes and push them to the remote repository. To push the changes, run `git push origin <branch-name>`.

7. **[team] Create a pull request (PR) to merge the changes to the main repository.** To create a pull request, go to the main repository and click on the "New pull request" button. Then, select the branch you want to merge to the main repository. Finally, click on the "Create pull request" button.

8. **[team] Assign reviewers to the PR.** Once the pull request is created, assign it to the team members for review. To assign the pull request, go to the pull request and click on the "Reviewers" button. Then, select the team members you want to assign the pull request to. Finally, click on the "Submit review" button.

    !!! note "Assigning reviewers"
        When working in a team, you should assign the pull request to the team
        member who is responsible for reviewing the code. If you are not sure who
        is responsible for reviewing the code, assign the project leader.

    !!! tip "Checking for documentation"
        When reviewing the code, it is also good to check if the documentation
        is up to date. If the documentation is not up to date, you can ask the
        person who created the pull request to update it.


9. **[team] Merge the PR.** Once the pull request is reviewed, merge it to the main repository. To merge the pull request, go to the pull request and click on the "Merge pull request" button. Then, click on the "Confirm merge" button.

    !!! question "Who should merge the PR?"
        Before starting to work on the code, you should decide who should merge the pull request. There are two options:

        - The project leader merges the pull request.
        - The person who created the pull request merges it.

        This varies from project to project. Therefore, you should decide who should merge the pull request before starting to work on the code. **But
        in both cases, the code has to be reviewed before the merging happens.**


10. **Delete the branch.** To delete the branch, go your remote repository and click on the "Branches" button. Then, select the branch you want to delete and click on the "Delete branch" button. Locally, you can delete the branch by running `git branch -d <branch-name>`.

11. **Pull the changes from the main repository.** To pull the changes, run `git pull <remote-name> master`.

Once you are done with the steps above, you can repeat the process for the next feature.

!!! abstract "Coding workflow"
    The following steps are the steps you should follow when working on the
    code after you setup your repository locally:

    1. create a new branch for each feature you are working on: `git checkout -b <branch-name>`
    2. implement the feature you are working on
    3. add the changes you made to the code: `git add <file-name>`
    4. commit the changes you made to the code: `git commit -m "<commit-message>"`
    5. once you are done with the feature, commit the changes and push them to
        the remote repository: `git push origin <branch-name>`

    Additional steps are required when working in a team:

    1. create a pull request
    2. wait for the pull request to be reviewed and merged
    3. delete the branch you created: `git branch -d <branch-name>`

    Afterwards, you can clean the local repository by pulling the changes from the main repository: `git pull <main-remote-name> main`

    Repeat the process for the next feature.

## Working on the Documentation

The documentation helps the team members to understand the code. Therefore, it is good practice to write the documentation for the code you are working on. The documentation should be clear and concise. It should also be updated periodically. The documentation can be written in the code itself or in a separate file. If you are writing the documentation in a separate file, make sure to add the file to the repository.

From the documentation, the following things should be clear:

- What is the purpose of the code?
- How to start the code (if applicable)?
- What are the features of the code?
- How to use the code?


!!! note "Documentation on a project"
    The way how documentation is provided should be decided within the team. Some teams prefer to write the documentation in the code itself, while others prefer to write it in a separate file. Talk to your team members and decide how you will write the documentation.


<!-- External Links -->
[pylint]: https://www.pylint.org/
[cookiecutter]: https://www.cookiecutter.io/templates


<!-- Internal Links -->
[Working on the code]: #working-on-the-code
