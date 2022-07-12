## Display username from user_id in join table
* task_id and user_id lives in the join table.
* if task_id is equal to url param id, then show all user_id's usernames in the page.
* in python manage.py shell
  * from main_app .models import *
    * imports all the models
  * Task.objects.all()
    * in our Task model, grab everything
  * task = Task.objects.get(name='Group Project 1')
    * create variable equal to 1 task
  * task.users.all()
    * grabs all the objects in the users table related to the task_id you selected right before.

## Stopping stopwatch timer adds a new task with timer appended into task
* if an user starts then stops the stopwatch, on stopping the stopwatch it will submit the form.
* on form submission, if name and description fields are empty it will submit with a default value.
* on form submission, the timer on the stopwatch will also be added to the database table.

## An user can add other users to their tasks
* Display all usernames in a dropdown menu on the task details page.
* An user can choose a username from the dropdown then click add.
* The username chosen will get added to the join table containing task_id and user_id.
* It will take the current task_id and add it with the user_id chosen.