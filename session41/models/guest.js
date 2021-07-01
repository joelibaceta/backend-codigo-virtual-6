'use strict';
const {
  Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class Guest extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      Guest.belongsTo(models.Booking, {foreignKey: 'BookingId', as: 'booking'});
    }
  };
  Guest.init({
    first_name: DataTypes.STRING,
    last_name: DataTypes.STRING,
    documentType: DataTypes.STRING,
    documentnumber: DataTypes.STRING
  }, {
    sequelize,
    modelName: 'Guest',
  });
  return Guest;
};