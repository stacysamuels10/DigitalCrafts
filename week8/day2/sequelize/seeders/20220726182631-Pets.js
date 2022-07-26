"use strict";

module.exports = {
  async up(queryInterface, Sequelize) {
    /**
     * Add seed commands here.
     *
     * Example:
     * await queryInterface.bulkInsert('People', [{
     *   name: 'John Doe',
     *   isBetaMember: false
     * }], {});
     */
    await queryInterface.bulkInsert(
      "Pets",
      [
        {
          name: "Samson",
          species: "Cat",
          age: 4,
          weight: "12",
          health: "Excellent",
          unitOfWeight: "lbs",
          owner: "Stacy",
          createdAt: new Date(),
          updatedAt: new Date(),
        },
        {
          name: "Dixie Bell",
          species: "Dog",
          age: 10,
          weight: "50",
          health: "Excellent",
          unitOfWeight: "lbs",
          owner: "Adair",
          createdAt: new Date(),
          updatedAt: new Date(),
        },
        {
          name: "Nora",
          species: "Dog",
          age: 6,
          weight: "60",
          health: "Excellent",
          unitOfWeight: "lbs",
          owner: "Stacy",
          createdAt: new Date(),
          updatedAt: new Date(),
        },
        {
          name: "Benji",
          species: "Bearded Dragon",
          age: 3,
          weight: "2",
          health: "Excellent",
          unitOfWeight: "lbs",
          owner: "Amanda",
          createdAt: new Date(),
          updatedAt: new Date(),
        },
        {
          name: "Stevie",
          species: "Cat",
          age: 1,
          weight: "10",
          health: "Excellent",
          unitOfWeight: "lbs",
          owner: "Andrea",
          createdAt: new Date(),
          updatedAt: new Date(),
        },
      ],
      {}
    );
  },

  async down(queryInterface, Sequelize) {
    /**
     * Add commands to revert seed here.
     *
     * Example:
     * await queryInterface.bulkDelete('People', null, {});
     */
    await queryInterface.bulkDelete("Pets", null, {});
  },
};
