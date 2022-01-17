# ROOM DECORATING COST ESTIMATOR

***

The Room Decorating Cost Estimator is a command_line application that decorators use to establish an estimate to supply customers for painting a room. 

Essential values are entered by the user to establish the end cost.




## How it works
***

The user will enter various values such as customer name, room length, room width, room height, number of doors, windows and radiators to be painted.
It also asks if the the room is a bathroom or a kitchen and makes an allowance for the extra time these rooms take as well as for the more expesnive paint reuqiered. 

Predetermined costs for each item have been worked out per m2, per m or per item and added to a linked google sheet. 
If the user has to increase rates a small update to the google sheet cells would need to be done. 
The functions in the application verify the information is correct and present and calculates the costs. 
A total cost is then calculated and all of the relevant information needed for an estimate are then inserted to the linked google estimate sheet. 

Google sheets

Below we see the costs sheet I have created to call the rates from and the estimate sheet which is returned the inoput values for name, length, width, height and total cost.

![Google sheets costs sheet image](https://i.imgur.com/21R4fli.png)

![Google sheets estimate sheet image](https://i.imgur.com/VXvkIlY.png)

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

### Future Features

- Add wallpapering function
- Specify paint finishes
- Add Taping and Filling estimator per m2

## Data Model

***

I used a Hierarchical Data Model to strucutre the app. It requires me to call for information form an external spreadsheet. This information is then used within functions which contain loops, if statments, inputs and methods.
Once all of the calculations have been made and a total estimate cost is returned it is then exported to an external estimate sheet along with other information. 

## Testing

***

I have manually tested the app on:
- Inserted wrong values to all of the inputs in the app to check the return of error massages and ensure it functions correctly.
- Run the code through PEP8online.com to ensure the format is ok. All code was adjusted and retested until passed.
- Tested the Heroku terminal once deployed and tested in the gitpod terminal throughout development. 
- I have manually tested it on iPhone, macbook and iPad.

### Bugs

One bug in particular was my customer name input allowing an empty value to pass. I ended up using a while loop with length function to check that it was higher then 0 so I knew it wasnt empty before continuting to the next function.

There are no remaining bugs

### Validation Testing

PEP8online.com used to check code and make the relevant changes. No errors found on final check. 

## Deployment

The development was deployed using Heroku.

The steps taken to deploy were
 - Create a new app in Heroku
 - Add config vars
 - Add buildpacks for Python and Nodejs
 - Link my Github respitory to Heroku
 - Deploy manually on Heroku

