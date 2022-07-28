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
      "Users",
      [
        {
          username: "stacy.samuels10",
          password: "CodingIsGreat5",
          updatedAt: new Date(),
          createdAt: new Date(),
        },
        {
          username: "Joe.F15",
          password: "CodingKing9000",
          updatedAt: new Date(),
          createdAt: new Date(),
        },
        {
          username: "VioletIsAwesome",
          password: "BestTAEver",
          updatedAt: new Date(),
          createdAt: new Date(),
        },
        {
          username: "TexasAggies5",
          password: "GigEm18",
          updatedAt: new Date(),
          createdAt: new Date(),
        },
        {
          username: "LSUTigers10",
          password: "GeauxTigers",
          updatedAt: new Date(),
          createdAt: new Date(),
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
    await queryInterface.bulkDelete("Users", null, {});
  },
};
