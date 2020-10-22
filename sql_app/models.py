from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from .database import Base

class Conv(Base):
    __tablename__ = "convs"
    id = Column(Integer, primary_key=True, index=True)
    port_type = Column(Integer, nullable=False)
    port_name = Column(String, nullable=False)
    model = Column(Integer, nullable=False)
    sn = Column(Integer, unique=True, index=True, nullable=False)
    last_active_time = Column(DateTime, nullable=True)

    controls = relationship("Contr", back_populates="conv",
                            cascade="all, delete, delete-orphan")
    # maxctrl = Column(Integer, default=0)
    # maxkeys = Column(Integer, default=0)
    # maxdate = Column(String, nullable=True)
    # realctrl = Column(Integer, default=0)
    # factive = Column(Integer, default=0)
    # flags = Column(Integer, default=0)
    # fwver = Column(Integer, default=0)
    # fdelete = Column(Integer, default=0)
    # fmode = Column(Integer, default=0)
    # foverlic = Column(Integer, default=0)
    # fsetlic = Column(Integer, default=0)
    # funbaund = Column(Integer, default=0)
    # fupdclient = Column(Integer, default=0)
    # lic = Column(String, nullable=True)

class Contr(Base):
    __tablename__ = "contrs"
    id = Column(Integer, primary_key=True, index=True)
    sn = Column(Integer, unique=True, index=True, nullable=False)
    model = Column(Integer, default=0)
    address = Column(Integer, default=0)
    fw_version = Column(Integer, default=0)
    ctrl_flags = Column(Integer, default=0)
    bank_size = Column(Integer, default=0)
    pass_point = Column(Integer, default=0)
    conv_id = Column(Integer, ForeignKey("convs.id"))

    conv = relationship("Conv", back_populates="controls")
