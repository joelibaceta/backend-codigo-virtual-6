'use strict';

module.exports = {
  up: async (queryInterface, Sequelize) => {

    await queryInterface.addColumn(
      'Bookings',
      'deleted',
      {
        type: Sequelize.BOOLEAN,
        allowNull: true
      }
    ) 
    await queryInterface.addColumn(
      'Bookings',
      'deletedAt',
      {
        type: Sequelize.DATE,
        allowNull: true
      }
    ) 
    /**
     * Add altering commands here.
     *
     * Example:
     * await queryInterface.createTable('users', { id: Sequelize.INTEGER });
     */
  },

  down: async (queryInterface, Sequelize) => {
    /**
     * Add reverting commands here.
     *
     * Example:
     * await queryInterface.dropTable('users');
     */
    await queryInterface.removeColumn('Bookings', 'deleted')
    await queryInterface.removeColumn('Bookings', 'deletedAt')
  }
};
