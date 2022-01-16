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

Welcome information

The welcome section has a welcome messsage and gives an instruction to input information when prompted.
It also displays the 'Enter Customer Name' input.

![Welcome information image](https://i.imgur.com/qa5rXWV.png)

The date function automatically displays the current date once the name has been entered.

![Date function image](https://i.imgur.com/KnHeITt.png)

The user will now input the information needed to calculate the estimate total from this point.
inputs include:
- Walls length
- Walls width
- Walls height
- Is the room a kitchen or bathroom (these rooms take longer to paint and require a more expensive paint foer the walls)
- A function the calculates the length of skirting boards in the room and displays it.

![Inputs image 1](https://i.imgur.com/sAr6vYP.png)

- Number of doors
- Number of windows
- Number of rabiators

![Inputs image 2](https://i.imgur.com/YFve33O.png)

Once all of the information has been entered the total estimate is calculated and returned. 

![Total estimate image](https://i.imgur.com/46NYVDL.png)

### Error Checking 

Errors messages will appear in inputs are not filled correctly.
These messages will appear when:
- The customer name is left blank
- The length, widht and height inputs are not a float
- The kitchen or bathroom question is not "yes" or "no"
- The doors, windows and radiators is not an int

![Errors image 1](https://i.imgur.com/PDUtkdi.png)

![Errors image 2](https://i.imgur.com/5JIiq3F.png)

![Errors image 2](https://i.imgur.com/cGGQqKz.png)

![Errors image 2](https://i.imgur.com/GSIlUzE.png)
