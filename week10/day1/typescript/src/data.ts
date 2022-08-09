const userIds = [
  {
    id: "b6809de6-1743-11ed-861d-0242ac120002",
  },
  {
    id: "b680a0b6-1743-11ed-861d-0242ac120002",
  },
  {
    id: "b680a1e2-1743-11ed-861d-0242ac120002",
  },
  {
    id: "b680a2fa-1743-11ed-861d-0242ac120002",
  },
  {
    id: "b680a3fe-1743-11ed-861d-0242ac120002",
  },
  {
    id: "b680a7c8-1743-11ed-861d-0242ac120002",
  },
  {
    id: "b680a8ea-1743-11ed-861d-0242ac120002",
  },
  {
    id: "b680aa0c-1743-11ed-861d-0242ac120002",
  },
  {
    id: "b680ab2e-1743-11ed-861d-0242ac120002",
  },
];

const usersToAssign = [
  { name: "user" },
  { name: "user" },
  { name: "user" },
  { name: "user" },
  { name: "user" },
  { name: "user" },
  { name: "user" },
  { name: "user" },
  { name: "user" },
];

type FormattedUser = {
  name: string;
  dept: string;
  id: string;
  createdAt: Date;
  updatedAt: Date;
  userVerification: () => {};
};

// 3 functions
const listOfNames = [
  "sam",
  "john",
  "joe",
  "becky",
  "jane",
  "ashley",
  "ryan",
  "michael",
  "samson",
];

const AssignId = (userIds: [], usersToAssign: []): [] => {
  const assignedIds: [] = [];
  type assignedUser = {
    name: string;
    id: string;
  };
  for (let i = 0; i < userIds.length; i++) {
    let assignedUserLoop: assignedUser = {
      name: usersToAssign[i],
      id: userIds[i],
    };
    assignedIds.push(assignedUserLoop);
  }
  return assignedIds;
};

const AssignNameToUser = (assignedIds: [], listOfNames: string[]) => {
  for (let i = 0; i < assignedIds.length; i++) {
    assignedIds[i];
  }
};

// const AssignId = (userIds: string[], listOfNames: string[]):object[] => {

//     const listOfFormUsers = [];
//   for (let i = 0; i < userIds.length; i++) {
//     let thisUser[i]: FormattedUser = {
//         name: listOfNames[i],
//         dept: "science",
//         id: userIds[i],
//         createdAt: new Date(),
//         updatedAt: new Date(),
//         userVerification: () => {}
//     }
//     listOfFormUsers.push(thisUser[i])
// }
// return listOfFormUsers;
// };

// assign IDs to users
// replace all users with the name "user" to a random name generated
// format the user to send to DB
// userVerifcation func
// I should be able to pass the name of the user and the id, and it should match one of these id's and the name should match one of the names in your list
//const userVerication = (id, name) => {
// check if the name is the name list
// check if the id is in the id list
// if it passes all test, it returns true, else false
