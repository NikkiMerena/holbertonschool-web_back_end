function cleanSet(set, startString) {
  const values = Array.from(set).filter((value) => value.startsWith(startString));
  return values.join('-');
}

export default cleanSet;
