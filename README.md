# Final Project - Trello

This project is the final asignment for the subject of software desing to desmotrate our abilities on backend, in our case the project will be based on trello app (activity manager based on boards) using, _design patterns_, and some _good code practices_ in order to provide a __RESTful API__ with services like login,register, and control of tasks and boards in function of their progress.

## Business Model

![Canvas](https://github.com/Andrew552004/project/assets/149690633/a7efcc5b-e1f3-437b-85a9-7a3f7e517e8d)


#User stories

• As a team leader, I want to create new boards, so that I can organize tasks and projects for my team.
• As a team leader, I want to view details of a specific board, so that I can monitor the tasks and progress associated with that board.
• As a team leader, I want to view a list of all boards, so that I can get an overview of all ongoing projects and their statuses.
• As a team leader, I want to update the details of an existing board, so that I can make adjustments as project requirements change.
• As a team leader, I want to delete boards that are no longer needed, so that I can keep the system organized and free of clutter.
• As a team leader, I want to create new boards, so that I can organize tasks and projects for my team.
• As a team leader, I want to view details of a specific board, so that I can monitor the tasks and progress associated with that board.
• As a team leader, I want to view a list of all boards, so that I can get an overview of all ongoing projects and their statuses.
• As a team leader, I want to update the details of an existing board, so that I can make adjustments as project requirements change.
• As a team leader, I want to delete boards that are no longer needed, so that I can keep the system organized and free of clutter.
• As a team leader, I want to create new cards on boards, so that I can add tasks and manage project activities effectively.
• As a team leader, I want to view details of a specific card, so that I can monitor the progress of tasks associated with that card.
• As a team leader, I want to view a list of cards associated with a board, so that I can get an overview of tasks within a specific project or work area.
• As a team leader, I want to update the details of an existing card, so that I can make adjustments to task descriptions or statuses as needed.
• As a team leader, I want to delete cards that are no longer needed, so that I can keep the board organized and focused on relevant tasks.
• As a team leader, I want to create new tasks and assign them to specific cards, so that I can manage project activities effectively.
• As a team leader, I want to update the details of existing tasks, such as their descriptions or statuses, so that I can track their progress accurately.
• As a team leader, I want to delete tasks that are no longer relevant or necessary, so that I can keep the project board organized and focused.
• As a team leader, I want to move tasks between different cards on the board, so that I can prioritize and allocate resources effectively.
• As a project member, I want to register an account with a unique username and password, so that I can access the project management platform securely.
• As a project member, I want to log in to my account using my username and password, so that I can view and manage project-related information.
• As a team leader, I want to register an account with a unique username and password, so that I can securely access the project management platform and lead my team effectively.
• As a team leader, I want to log in to my account using my username and password, so that I can efficiently view, assign tasks, and oversee the progress of projects within my team.
• As an administrator, I want to register an account with administrative privileges, so that I can securely access and manage system settings, user accounts, and permissions.
• As an administrator, I want to log in to my administrative account using my username and password, so that I can efficiently manage system configurations, user access permissions, and other administrative tasks.

## Technical Definitions

### Tools to Use

In this case, the backend will be build using _python 3.10_, and some related technologies as _Fast API_ to serve functionalities, _PyTest_ to apply some simple unit tests, and _Black_ to auto-format the code and increase code readibility.

## Entities



## How to Use

Follow these steps to set up and use the project:

1. **Make sure you have Docker installed and that you have virtualization on your machine activated and can use local scripts***

2. **Copy this for builds the images defined in the docker-compose.yml.**
   ```bash
   docker compose build
   ```
3. **Copy this for brings up the services, creating and starting the containers.**
   ```bash
   docker-compose up
   ```
4. **Put this for generate the poetry.lock**
   ```bash
   poetry lock
   ```
5. **If you had insomnia installed you can dowload our file for test our end points**

