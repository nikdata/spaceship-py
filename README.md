## Spaceship Titanic

### Data Dictionary

| Variable | Description |
| ------- | ------------ |
| **PassengerId** | A unique Id for each passenger. Each Id takes the form `gggg_pp` where `gggg` indicates a group the passenger is travelling with and `pp` is their number within the group. People in a group are often family members, but not always.|
| **HomePlanet** | The planet the passenger departed from, typically their planet of permanent residence. |
| **CryoSleep** | Indicates whether the passenger elected to be put into suspended animation for the duration of the voyage. Passengers in cryosleep are confined to their cabins.|
| **Cabin** | The cabin number where the passenger is staying. Takes the form deck/num/side, where side can be either P for Port or S for Starboard. |
| **Destination** | The planet the passenger will be debarking to.|
| **Age** | The age of the passenger.|
| **VIP** | Whether the passenger has paid for special VIP service during the voyage.|
| **RoomService**, **FoodCourt**, **ShoppingMall**, **Spa**, **VRDeck** | Amount the passenger has billed at each of the Spaceship Titanic's many luxury amenities.|
| **Name** | The first and last names of the passenger.|
| **Transported** | Whether the passenger was transported to another dimension. This is the target, the column you are trying to predict.|

### Goal

The response variable (or what we need to predict) is the variable `Transported`. This is a binary classification problem (1 meaning true or passenger was transported to another dimension, 0 meaning false or passenger was not transported to another dimension).

### Provided Dataset Files

We are provided with three different files (found in the data folder):

- sample_submission.csv
- train.csv
- test.csv

The `sample_submission.csv` file helps to clarify what information we need to submit to Kaggle for this competition. This file will consist of an ID column and the prediction we made. The `train.csv` file consists of all the raw data that we can use to train our machine learning models. The `test.csv` file consists of all the attributes we can use to make predictions for passengers on whether they will be transported to another dimension or not. The passengers found on `test.csv` are also found on the `sample_submission.csv` file.

### Dataset Preview

Here's a screenshot of the raw data that was provided
