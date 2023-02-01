-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema example3
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `example3` ;

-- -----------------------------------------------------
-- Schema example3
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `example3` DEFAULT CHARACTER SET utf8 ;
USE `example3` ;

-- -----------------------------------------------------
-- Table `example3`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `example3`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `example3`.`camiones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `example3`.`camiones` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `patente` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_camiones_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_camiones_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `example3`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
