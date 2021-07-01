'use strict';
const {
  Model
} = require('sequelize');

module.exports = (sequelize, DataTypes) => {
  class Booking extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      Booking.hasMany(models.Guest,  {as: 'guests'});
    }
  };

  Booking.init({
    roomType: DataTypes.STRING,
    beginDate: DataTypes.DATE,
    endDate: DataTypes.DATE,
    email: DataTypes.STRING,
    phone: DataTypes.STRING,
    documentType: DataTypes.STRING,
    documentNumber: DataTypes.STRING,
    deleted: DataTypes.BOOLEAN,
    deletedAt: DataTypes.DATE
  }, {
    sequelize,
    modelName: 'Booking',
  });
  return Booking;
};