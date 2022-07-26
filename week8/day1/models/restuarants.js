'use strict';
const {
  Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class Restuarants extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      // define association here
    }
  }
  Restuarants.init({
    name: DataTypes.STRING,
    address: DataTypes.STRING,
    reviewScore: DataTypes.STRING
  }, {
    sequelize,
    modelName: 'Restuarants',
  });
  return Restuarants;
};