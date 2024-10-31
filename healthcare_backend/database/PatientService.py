import pandas as pd
from models.Patient import Patient


class PatientService:
    def __init__(self, conn):
        self.conn = conn  # Atributo nombre
         
    def CreatePatientLogs(self, file):
        mensaje = ''

        create_list = []
        update_list = []

        # Leer el archivo Excel
        dataframe = pd.read_excel(file, sheet_name="Patients").fillna("")
        print(f"Total de filas en el archivo Excel: {len(dataframe)}")

        mycursor = self.conn.cursor()

        mycursor.execute("SELECT Patient, Labcode FROM patients")
        resultados = mycursor.fetchall()

        mycursor.close()

        existing_patients = {str(res[0]) + str(res[1]) for res in resultados}  # Tuplas de (Patient, Labcode)
        print(f"Pacientes existentes: {len(existing_patients)}")

        # Procesar cada fila del DataFrame
        for index, row in dataframe.iterrows():
            patient = Patient()
            try:
                patient.Patient = row["Patient"]
                patient.Labcode = row["Labcode"]
                patient.Project = row["Project"]
                patient.Cohort = row["Cohort"]
                patient.CaseId = row["CaseId"]
                patient.Center = row["Center"]
                patient.CenterCode = row["CenterCode"]
                patient.TrialCode = row["TrialCode"]
                patient.ExternalId = row["ExternalId"]
                patient.Specie = row["Specie"]
                patient.Consent = row["Consent"]
                patient.Disease = row["Disease"]
                patient.EvolutiveStage = row["EvolutiveStage"]
                patient.DiagnosisState = row["DiagnosisState"]
                patient.DiagnosisDate = row["DiagnosisDate"]
                patient.InclusionDate = row["InclusionDate"]

                # Comprobar si el paciente existe
                if patient.Patient + patient.Labcode in existing_patients:
                    update_list.append(patient) 
                    #print(f"Actualizando paciente: {patient.Patient} - {patient.Labcode}")
                else:
                    create_list.append(patient)
                    #print(f"Inserción de paciente: {patient.Patient} - {patient.Labcode}")
            except Exception as e:
                print(f"Error procesando fila {index}: {e}")
                continue

        # Convertir objetos Patient a tuplas para la operación de inserción masiva
        insert_data = [
            (
                p.Patient, p.Labcode, p.Project, p.Cohort, p.CaseId,
                p.Center, p.CenterCode, p.TrialCode, p.ExternalId, p.Specie,
                p.Consent, p.Disease, p.EvolutiveStage, p.DiagnosisState,
                p.DiagnosisDate, p.InclusionDate
            ) for p in create_list
        ]

        # Eliminar duplicados en insert_data
        unique_keys = set()
        unique_data = []
        for data in insert_data:
            patient_labcode = (data[0], data[1])  # data[0] es Patient y data[1] es Labcode
            if patient_labcode not in unique_keys:
                unique_keys.add(patient_labcode)
                unique_data.append(data)

        insert_data = unique_data
        
        # Convertir objetos Patient a tuplas para la operación de actualización masiva
        update_data = [
            (
                p.Patient, p.Labcode,  # Para SET
                p.Project, p.Cohort, 
                p.CaseId, p.Center, 
                p.CenterCode, p.TrialCode, p.ExternalId, 
                p.Specie, p.Consent, p.Disease, 
                p.EvolutiveStage, p.DiagnosisState, p.DiagnosisDate, 
                p.InclusionDate,
                p.Patient,  # Para WHERE
                p.Labcode   # Para WHERE
            ) for p in update_list
        ]

        print('CREATE LIST: ' + str(len(insert_data)))  
        print('UPDATE LIST: ' + str(len(update_data)))  

        
        sql_insert = """
            INSERT INTO patients (
                Patient, Labcode, Project, Cohort, CaseId, Center, CenterCode, 
                TrialCode, ExternalId, Specie, Consent, Disease, EvolutiveStage, 
                DiagnosisState, DiagnosisDate, InclusionDate
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        if(len(insert_data)>0):
            mycursor=None
            try:
                mycursor =   self.conn.cursor()
                mycursor.executemany(sql_insert, insert_data)

                print(f"{mycursor.rowcount} records inserted.")  
                mensaje += f"{mycursor.rowcount} records inserted."
                
                self.conn.commit()
                mycursor.close()
            except Exception as e:
                mycursor.close()
                mensaje += str(e)
        else:
            mensaje += "There are not elements for inserting."

        sql_update = """
            UPDATE patients
            SET 
                Patient = %s,
                Labcode = %s,
                Project = %s,
                Cohort = %s,
                CaseId = %s,
                Center = %s,
                CenterCode = %s,
                TrialCode = %s,
                ExternalId = %s,
                Specie = %s,
                Consent = %s,
                Disease = %s,
                EvolutiveStage = %s,
                DiagnosisState = %s,
                DiagnosisDate = %s,
                InclusionDate = %s
            WHERE 
                Patient = %s AND 
                Labcode = %s
        """
        if(len(update_data)>0):
            mycursor =None
            try:
                mycursor = self.conn.cursor()
                mycursor.executemany(sql_update, update_data)

                print(f" {mycursor.rowcount} records updated.")  
                mensaje += f" {mycursor.rowcount} records updated."
                
                self.conn.commit()       
                mycursor.close()
            except Exception as e:
                mycursor.close()
                mensaje += str(e)
        else:
            mensaje += " There are not elements for updating."
         
        return mensaje

    def PatientRecords(
        self,
        page: int = 1,
        per_page: int = 10,
        sort_by: str = 'InclusionDate',
        sort_order: str = 'asc',
        search: str = ''
    ):
        mycursor=None
        try:
            pts = []
            # Crear un cursor para ejecutar comandos SQL
            mycursor = self.conn.cursor()

            # Construir la consulta con paginación y ordenamiento
            query = f"""
                SELECT * FROM Patients
                WHERE Patient LIKE %s OR Labcode LIKE %s
                ORDER BY {sort_by} {sort_order}
                LIMIT %s OFFSET %s
            """
            mycursor.execute(query, ('%' + search + '%', '%' + search + '%', per_page, (page - 1) * per_page))

            # Obtener los resultados
            resultados = mycursor.fetchall()

            for res in resultados:
                pt = Patient()
                pt.Patient = res[0]
                pt.Labcode = res[1]
                pt.Project = res[2]
                pt.Cohort = res[3]
                pt.CaseId = res[4]
                pt.Center = res[5]
                pt.CenterCode = res[6]
                pt.TrialCode = res[7]
                pt.ExternalId = res[8]
                pt.Specie = res[9]
                pt.Consent = res[10]
                pt.Disease = res[11]
                pt.EvolutiveStage = res[12]
                pt.DiagnosisState = res[13]
                pt.DiagnosisDate = res[14]
                pt.InclusionDate = res[15]
                pts.append(pt)
            mycursor.close
            return pts
        except Exception as e:
            mycursor.close
            raise e