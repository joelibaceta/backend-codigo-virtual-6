-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`usuario` (
  `idusuario` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `dni` DECIMAL NULL,
  `coreo` VARCHAR(100) NULL,
  `nickname` VARCHAR(100) NULL,
  `passwod` VARCHAR(100) NULL,
  PRIMARY KEY (`idusuario`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`carrito`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`carrito` (
  `idcarrito` INT NOT NULL AUTO_INCREMENT,
  `idusuario` INT NOT NULL,
  PRIMARY KEY (`idcarrito`),
  INDEX `fk_carrito_usuario1_idx` (`idusuario` ASC) VISIBLE,
  CONSTRAINT `fk_carrito_usuario1`
    FOREIGN KEY (`idusuario`)
    REFERENCES `mydb`.`usuario` (`idusuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`venta`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`venta` (
  `idventa` INT NOT NULL AUTO_INCREMENT,
  `comprobante` VARCHAR(45) NULL,
  `idcarrito` INT NOT NULL,
  PRIMARY KEY (`idventa`),
  INDEX `fk_venta_carrito1_idx` (`idcarrito` ASC) VISIBLE,
  CONSTRAINT `fk_venta_carrito1`
    FOREIGN KEY (`idcarrito`)
    REFERENCES `mydb`.`carrito` (`idcarrito`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`categoria`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`categoria` (
  `idcategoria` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(200) NULL,
  PRIMARY KEY (`idcategoria`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`producto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`producto` (
  `idproducto` INT NOT NULL AUTO_INCREMENT,
  `sku` VARCHAR(45) NULL,
  `stock` INT(5) NULL,
  `precio` FLOAT NULL,
  `nombre` VARCHAR(45) NULL,
  `descripcion` VARCHAR(255) NULL,
  `idcategoria` INT NOT NULL,
  PRIMARY KEY (`idproducto`),
  INDEX `idcategoria_idx` (`idcategoria` ASC) VISIBLE,
  CONSTRAINT `idcategoria`
    FOREIGN KEY (`idcategoria`)
    REFERENCES `mydb`.`categoria` (`idcategoria`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`detallecarrito`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`detallecarrito` (
  `iddetallecarrito` INT NOT NULL AUTO_INCREMENT,
  `fecha` DATE NULL,
  `cantidad` INT NULL,
  `idproducto` INT NOT NULL,
  `idcarrito` INT NOT NULL,
  PRIMARY KEY (`iddetallecarrito`),
  INDEX `idproducto_idx` (`idproducto` ASC) VISIBLE,
  INDEX `fk_detallecarrito_carrito1_idx` (`idcarrito` ASC) VISIBLE,
  CONSTRAINT `idproducto`
    FOREIGN KEY (`idproducto`)
    REFERENCES `mydb`.`producto` (`idproducto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_detallecarrito_carrito1`
    FOREIGN KEY (`idcarrito`)
    REFERENCES `mydb`.`carrito` (`idcarrito`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
