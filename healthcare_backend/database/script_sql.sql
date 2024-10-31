create database db_healthcare;

CREATE TABLE Patients (
    Patient VARCHAR(50)NOT NULL,
    Labcode VARCHAR(50) NOT NULL,
    Project VARCHAR(255),
    Cohort VARCHAR(255),
    CaseId VARCHAR(255),
    Center VARCHAR(255),
    CenterCode VARCHAR(255),
    TrialCode VARCHAR(255),
    ExternalId VARCHAR(255),
    Specie VARCHAR(255),
    Consent VARCHAR(255),
    Disease VARCHAR(255),
    EvolutiveStage VARCHAR(255),
    DiagnosisState VARCHAR(255),
    DiagnosisDate DATETIME,
    InclusionDate DATETIME,
    PRIMARY KEY (Patient, Labcode)
);