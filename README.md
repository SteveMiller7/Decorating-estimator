# ROOM DECORATING COST ESTIMATOR

***

The Room Decorating Cost Estimator is a command_line application that decorators use to establish an estimate to supply customers for painting a room. 

Essential values are entered by the user to establish the end cost.




## How it works
***

The user will enter various values such as customer name, room length, room width, room height, number of doors, windows and radiators to be painted.
It also asks if the the room is a bathroom or a kitchen and makes an allowance for the extra time these rooms take as well as for the more expesnive paint reuqiered. 

Predetermined costs for each item have been worked out per m2, per m or per item and added to a linked google sheet. 
If the user had to increase rates a small update to the google sheet would be done. 
The functions in the application verify the information is correct and present and calculates the costs. 
A total cost is then calculated and all of the relevant information needed for an estimate are then inserted to the linked google estimate sheet. 

## Features
***

### Welcome information

The welcome section has a welcome messsage and gives an instruction to input information when prompted.
It also displays the 'Enter Customer Name' input.

![Welcome information image](https://i.imgur.com/qa5rXWV.png)

The date function automatically displays the current date once the name has been entered.

![Welcome information image](https://i.imgur.com/KnHeITt.png)

The user will now input the information needed to calculate the estimate total from this point.
inputs include:
- Walls length
- Walls width
- Walls height
- Is the room a kitchen or bathroom (these rooms take longer to paint and require a more expensive paint foer the walls)
- A function the calculates the length of skirting boards in the room and displays it.
![Welcome information image](https://i.imgur.com/sAr6vYP.png)
- Number of doors
- Number of windows
- Number of rabiators
![Welcome information image](https://i.imgur.com/YFve33O.png)
