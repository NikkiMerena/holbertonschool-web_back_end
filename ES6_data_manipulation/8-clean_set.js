function cleanSet(set, startString) {
  const cleanedValues = Array.from(set)
    .filter((value) => value.startsWith(startString))
    .map((value) => value.slice(startString.length));

  return cleanedValues.join('-');
}

export default cleanSet;
