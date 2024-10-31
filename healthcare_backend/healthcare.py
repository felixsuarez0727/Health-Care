from fastapi import FastAPI, APIRouter, UploadFile, HTTPException, status, Request, Depends, Query, Header,File, Form 
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from models.ResultResponse import ResultResponse
from models.ErrorMsg import ErrorMsg
from models.Patient import Patient
from database.PatientService import PatientService

from typing import List
from io import BytesIO
from database.MySQLConnection import MySQLConnection


# Dependencia para obtener la conexión a la base de datos
def get_db_connection():
    db_connection = MySQLConnection.get_connection()
    if db_connection.is_connected():
        return db_connection
    else:
        raise Exception("No Database connection.")

app = FastAPI(
    title="Healthcare REST API",
    description="Web platform for Healthcare",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  # Origenes permitidos
    allow_credentials=True,
    allow_methods=["*"],  # Métodos permitidos
    allow_headers=["*"],  # Cabeceras permitidas
)

v1_router = APIRouter()



@v1_router.post("/process-file/", 
    #tags=["v1"],
    description='Endpoint for creating/updating Patient Records',
    responses={
        200: {"model": List[Patient]},
        400: {"model": ErrorMsg}
    })
async def create_item(file: UploadFile = File(...), db_connection = Depends(get_db_connection)):
    # Verificar que el archivo sea un Excel
    if not file.filename.endswith((".xlsx", ".xls")):
        raise HTTPException(status_code=400, detail="File must be an Excel file (.xlsx, .xls)")

    try:
        contents = await file.read()
        bfile = BytesIO(contents)
        
        pt = PatientService(db_connection)
        ma = pt.CreatePatientLogs(bfile)
        return ResultResponse(data=str(ma))   

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {e}")


@v1_router.get("/patient-record/", 
    #tags=["v1"],
    description='List the patient data',
    responses={
        200: {"model": List[Patient]},
        400: {"model": ErrorMsg}
    })
async def record(
    page: int = Query(1, description="Page Number"),
    per_page: int = Query(10, description="Number of records"),
    sort_by: str = Query('InclusionDate', description="Order field"),
    sort_order: str = Query('asc', description="Order secuence"),
    search: str = Query('', description="Search ID"),
    db_connection = Depends(get_db_connection)
): 
    try:       
        da = PatientService(db_connection)
        '''
        page: int = 1,
        per_page: int = 10,
        sort_by: str = 'InclusionDate',
        sort_order: str = 'asc',
        search: str = ''
        '''
        x = da.PatientRecords(page=page, 
                          per_page=per_page, 
                          sort_by=sort_by, 
                          sort_order=sort_order,
                          search=search
                          )
        ##print('X CONTIENE: '+str(x))
        return x
    except Exception as e:
        return 'dice:'+str(e)

app.include_router(v1_router, prefix="/api")
 