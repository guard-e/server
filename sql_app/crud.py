from sqlalchemy.orm import Session
from . import models, schemas


def get_conv(db: Session, conv_id: int):
    return db.query(models.Conv).filter(models.Conv.id == conv_id).first()


def get_conv_by_sn(db: Session, sn: int):
    return db.query(models.Conv).filter(models.Conv.sn == sn).first()


def get_convs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Conv).offset(skip).limit(limit).all()


def create_conv(db: Session, conv: schemas.ConvCreate):
    # fake_hashed_password = user.password + "notreallyhashed"
    db_conv = models.Conv(**conv.dict())
    #     email=user.email,
    #     hashed_password=fake_hashed_password
    # )
    db.add(db_conv)
    db.commit()
    db.refresh(db_conv)
    return db_conv


def get_contrs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Contr).offset(skip).limit(limit).all()


def create_contr(db: Session, contr: schemas.ContrCreate, conv_id: int):
    db_contr = models.Contr(**contr.dict(), owner_id=conv_id)
    db.add(db_contr)
    db.commit()
    db.refresh(db_contr)
    return db_contr
