import ClassRoom from './0-classroom';

function initializeRooms() {
  const roomSizes = [19, 20, 34];
  const rooms = roomSizes.map((size) => new ClassRoom(size));
  return rooms;
}

// Testing the initializeRooms function
const rooms = initializeRooms();
console.log(rooms);
