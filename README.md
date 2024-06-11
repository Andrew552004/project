# Final Project - Trello

This project is the final asignment for the subject of software desing to desmotrate our abilities on backend, in our case the project will be based on trello app (activity manager based on boards) using, _design patterns_, and some _good code practices_ in order to provide a __RESTful API__ with services like login,register, and control of tasks and boards in function of their progress.

## Business Model

![Canvas](https://github.com/Andrew552004/project/assets/149690633/a7efcc5b-e1f3-437b-85a9-7a3f7e517e8d)


#User stories**

• As a user, I want to move tasks between different columns on my dashboard, such as "To Do", "In Progress", and "Completed", so that I can track the progress of my tasks.

• As a user, I want to add comments to tasks, so that I can provide more information or relevant context.

• As a product manager, I want to add new tasks to my board, assign them a description, and set a due date, so that I can manage my tasks effectively.

• As a product manager, I want to assign tasks to other users and receive notifications when they are completed, so that I can collaborate with others and stay updated.

• As a system administrator, I want to manage users, their access permissions, and general system settings, so that I can ensure the smooth operation of the system.

• As a scrum master, I want to create a new board, so that I can organize my different projects or work areas.

• As a scrum master, I want to assign boards to users, so that I can map users into a project, synchronizing the team.

• As a scrum master, I want to cancel activities, so that I can foresee unexpected changes in requirements.

• As a scrum master, I want to initialize sprints once the current one is over, to keep adding value to the project, sticking to the agile framework.


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
5. **If you had insomnia installed you can test our end points**

