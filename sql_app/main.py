from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/convs/", response_model=schemas.Conv)
def create_conv(conv: schemas.ConvCreate, db: Session = Depends(get_db)):
    db_conv = crud.get_conv_by_sn(db, sn=conv.sn)
    if db_conv:
        raise HTTPException(status_code=400, detail="SN already registered")
    return crud.create_conv(db=db, conv=conv)


@app.get("/convs/", response_model=List[schemas.Conv])
def read_convs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    convs = crud.get_convs(db, skip=skip, limit=limit)
    return convs


@app.get("/convs/{conv_id}", response_model=schemas.Conv)
def read_conv(conv_id: int, db: Session = Depends(get_db)):
    db_conv = crud.get_conv(db, conv_id=conv_id)
    if db_conv is None:
        raise HTTPException(status_code=404, detail="Conv not found")
    return db_conv


@app.post("/convs/{conv_id}/contrs/", response_model=schemas.Contr)
def create_contr_for_conv(conv_id: int, contr: schemas.ContrCreate, db: Session = Depends(get_db)):
    return crud.create_contr(db=db, contr=contr, conv_id=conv_id)


@app.get("/contrs/", response_model=List[schemas.Contr])
def read_contrs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_contrs(db, skip=skip, limit=limit)
    return items