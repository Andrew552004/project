# Final Project - Trello

This project is the final asignment for the subject of software desing to desmotrate our abilities on backend, in our case the project will be based on trello app (activity manager based on boards) using, _design patterns_, and some _good code practices_ in order to provide a __RESTful API__ with services like login,register, and control of tasks and boards in function of their progress.

## Poster
<p align="center">
<img src="https://github.com/Andrew552004/project-docker/assets/149690633/c5fe2476-e654-4d42-bb3f-0594a886aa45](https://github.com/Andrew552004/project-docker/blob/main/F54E0cIpSUWjLjjb2KEshA.webp" alt="FastAPI logo" width="600">
</p>

## Business Model
<p align="center">
<img src="https://github.com/Andrew552004/project-docker/assets/149690633/c5fe2476-e654-4d42-bb3f-0594a886aa45" alt="FastAPI logo" width="600">
</p>



## User stories

• As a team leader, I want to create new boards to organize tasks and projects.  
• As a team leader, I want to view details of a specific board to monitor progress.  
• As a team leader, I want to view a list of all boards to get an overview of projects.  
• As a team leader, I want to update the details of an existing board as needed.  
• As a team leader, I want to delete unnecessary boards to maintain organization.  
• As a team leader, I want to create new cards on boards to manage activities.  
• As a team leader, I want to view details of a specific card to monitor task progress.  
• As a team leader, I want to view a list of cards associated with a board for an overview.  
• As a team leader, I want to update the details of an existing card as needed.  
• As a team leader, I want to delete cards that are no longer necessary to keep the board focused.  
• As a team leader, I want to create new tasks and assign them to specific cards to manage activities.  
• As a team leader, I want to update the details of existing tasks to track progress.  
• As a team leader, I want to delete tasks that are no longer relevant to keep the board organized.  
• As a team leader, I want to move tasks between different cards to prioritize resources.  
• As a project member, I want to register an account to access the project management platform.  
• As a project member, I want to log in to my account to view and manage project-related information.  
• As an administrator, I want to register an account with administrative privileges to manage the system.  
• As an administrator, I want to log in to my administrative account to manage system configurations and permissions.  

## Tools used

In this case, the backend will be built using Python 3.10, leveraging Fast API to serve functionalities, PyTest for conducting simple unit tests, and Black for auto-formatting the code to enhance readability. Additionally, we'll employ the following tools:

### Backend:  

1. Python  
2. Fast API  
3. PyTest  
4. Black  
5. Docker  
6. PgAdmin  
7. Insomnia    
8. Poetry
   
### Databases:  

1. PostgreSQL"


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
5. **If you had insomnia installed you can dowload our file(endpoint project) for test our end points**

