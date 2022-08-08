// objects
// const user = { name: "joe"}
// let user: {
//   name: string;
// } = {
//   name: "joe",
// };

//type alias

// let amanda: User = {
//   name: "Amanda",
//   username: "lizardgurl152xd",
//   age: 20,
//   emailAddress: "lizardsrox@yahoo.com",
// };

// let west: User = {
//   name: "West",
//   username: "westdaddy",
//   emailAddress: "bestcoastwestcoast@gmail.com",
// };

// if you don't know what keys will be called
// you can use this in your object
// const obj = {[key: string]: any;}

// type alias Carpenter
type Carpenter = {
  companyName: string;
  readonly id: number;
};

let carlos: Carpenter = {
  companyName: "ABC Company",
  id: 1001,
};

// declare an array variable called list of carpenters that only receives the type of carpenters

const listOfCarpenters: Carpenter[] = [];
listOfCarpenters.push(carlos);

type Password = {
  password: string | number;
  securityClearance: "Basic" | "Top Secret";
};

type SoftwareEngineer = {
  readonly id: number;
  password: Password;
};

const blk: SoftwareEngineer = {
  id: 12202,
  password: {
    password: 7777,
    securityClearance: "Basic",
  },
};
//listOfUsers to combine users or masterUsers
//maserUser id, password, email, createdAt, updatedAt, clearanceLevel: "top secret" | "Basic"
// create a user type id, password, email, createdAt, updatedAt

type User = {
  id: number;
  password: string;
  email: string;
  createdAt: Date;
  updatedAt: Date;
};

type MasterUser = User & {
  clearanceLevel: "top secret" | "basic";
};

let listOfUsers: MasterUser[] | User[] = [];

let Stacy: MasterUser = {
  id: 1,
  password: "password",
  email: "leavemealone@gmail.com",
  createdAt: new Date(),
  updatedAt: new Date(),
  clearanceLevel: "top secret",
};
