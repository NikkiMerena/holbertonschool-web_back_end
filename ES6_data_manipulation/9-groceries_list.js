function groceriesList() {
  const groceryMap = {
    Apples: 10,
    Tomatoes: 10,
    Pasta: 1,
    Rice: 1,
    Banana: 5,
  };
  return groceryMap;
}

// Calling the function & storing the result in a variable
const groceryList = groceriesList();

// Printing the grocery List
console.log(groceriesList);

export default groceriesList;
