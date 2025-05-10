-- schema.sql

-- Clinicians Table
CREATE TABLE IF NOT EXISTS `Clinicians` (
    `clinician_id` INT AUTO_INCREMENT PRIMARY KEY,
    `full_name` VARCHAR(255) NOT NULL,
    `license_number` VARCHAR(100) UNIQUE, -- Assuming MMC number or similar
    `specialty` VARCHAR(150),
    `email` VARCHAR(255) NOT NULL UNIQUE,
    `password_hash` VARCHAR(255), -- To be populated if login is implemented
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX `idx_clinician_email` (`email`) -- Index for faster email lookups
);
-- Patients Table
CREATE TABLE IF NOT EXISTS `Patients` (
    `patient_id` INT AUTO_INCREMENT PRIMARY KEY,
    `full_name` VARCHAR(255) NOT NULL,
    `date_of_birth` DATE NOT NULL,
    `gender` ENUM('Male', 'Female', 'Other', 'Prefer not to say') NOT NULL, -- Added 'Prefer not to say'
    `nric_passport_number` VARCHAR(255) UNIQUE, -- To store potentially encrypted/hashed value. Needs ADR.
    `contact_number` VARCHAR(50),
    `address` TEXT,
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX `idx_patient_name` (`full_name`),
    INDEX `idx_nric_passport` (`nric_passport_number`) -- Index for faster lookup, even if encrypted
);
-- Encounters Table
CREATE TABLE IF NOT EXISTS `Encounters` (
    `encounter_id` INT AUTO_INCREMENT PRIMARY KEY,
    `patient_id` INT NOT NULL,
    `clinician_id` INT NOT NULL,
    `encounter_date` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, -- Changed to DATETIME for more precision
    `status` ENUM('in-progress', 'completed', 'cancelled') NOT NULL DEFAULT 'in-progress', -- Added 'cancelled' status
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (`patient_id`) REFERENCES `Patients`(`patient_id`) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (`clinician_id`) REFERENCES `Clinicians`(`clinician_id`) ON DELETE RESTRICT ON UPDATE CASCADE,
    INDEX `idx_encounter_patient` (`patient_id`),
    INDEX `idx_encounter_clinician` (`clinician_id`),
    INDEX `idx_encounter_date` (`encounter_date`)
);
-- SubjectiveNotes Table
CREATE TABLE IF NOT EXISTS `SubjectiveNotes` (
    `subjective_note_id` INT AUTO_INCREMENT PRIMARY KEY,
    `encounter_id` INT NOT NULL,
    `raw_audio_path` VARCHAR(512), -- Path to stored audio file
    `raw_text_input` TEXT,
    `transcribed_text` TEXT,
    `ai_draft_text` TEXT,
    `clinician_final_text` TEXT,
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (`encounter_id`) REFERENCES `Encounters`(`encounter_id`) ON DELETE CASCADE ON UPDATE CASCADE, -- Cascade delete as notes are part of an encounter
    INDEX `idx_subjective_encounter` (`encounter_id`)
);
-- ObjectiveNotes Table
CREATE TABLE IF NOT EXISTS `ObjectiveNotes` (
    `objective_note_id` INT AUTO_INCREMENT PRIMARY KEY,
    `encounter_id` INT NOT NULL,
    `raw_text_input` TEXT, -- Objective notes are typically text-only
    `ai_draft_text` TEXT,
    `clinician_final_text` TEXT,
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (`encounter_id`) REFERENCES `Encounters`(`encounter_id`) ON DELETE CASCADE ON UPDATE CASCADE,
    INDEX `idx_objective_encounter` (`encounter_id`)
);
-- AssessmentNotes Table
CREATE TABLE IF NOT EXISTS `AssessmentNotes` (
    `assessment_note_id` INT AUTO_INCREMENT PRIMARY KEY,
    `encounter_id` INT NOT NULL,
    `ai_draft_text` TEXT, -- Assessment is primarily AI-generated based on S+O
    `clinician_final_text` TEXT,
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (`encounter_id`) REFERENCES `Encounters`(`encounter_id`) ON DELETE CASCADE ON UPDATE CASCADE,
    INDEX `idx_assessment_encounter` (`encounter_id`)
);
-- PlanNotes Table
CREATE TABLE IF NOT EXISTS `PlanNotes` (
    `plan_note_id` INT AUTO_INCREMENT PRIMARY KEY,
    `encounter_id` INT NOT NULL,
    `raw_audio_path` VARCHAR(512), -- Path to stored audio file
    `raw_text_input` TEXT,
    `transcribed_text` TEXT,
    `ai_draft_text` TEXT, -- Plan is primarily AI-generated based on S+O+A
    `clinician_final_text` TEXT,
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (`encounter_id`) REFERENCES `Encounters`(`encounter_id`) ON DELETE CASCADE ON UPDATE CASCADE,
    INDEX `idx_plan_encounter` (`encounter_id`)
);