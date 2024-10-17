The following program first reads the json file and saves it as self.data.
The method for creating the customer.json file is created. A for loop is made to run through the self.data searching for the name and phone number of the customer. If the customer is already in the list it is not added again. 
Then we use json.dump to store that information in the customer.json file. 
The method for creating the items.json file is then created. With a nested loop to reach the information inside items. Using the same process we json.dump the items into the created items.json file. The only difference here is that 
we add a count feature. Which adds 1 every time the food item is ran. 

Now for the argparse which is meant to help run the program for the user.

The user will first have to open the command prompt or terminal and move to the directory in which the script and the example_orders.json are saved.
Then you will run the script by providing the json file as an argument. In this case, you would run the following:
**python midterm.py example_orders.json**

This will create the customer.json and items.json files.

You can also ask the terminal for help by typing the following:
**python midterm.py --help**
This will give you a brief explanation of the script and what you need to type in order to run it.
