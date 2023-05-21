function updateUniqueItems(groceryMap) {
  if (!(groceryMap instanceof Map)) {
    throw new Error('Cannot process');
  }

  const updatedMap = new Map();

  for (const [item, quantity] of groceryMap) {
    if (quantity === 1) {
      updatedMap.set(item, 100);
    } else {
      updatedMap.set(item, quantity);
    }
  }

  return updatedMap;
}

export default updateUniqueItems;
