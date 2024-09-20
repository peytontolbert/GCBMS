from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import enum
import datetime

Base = declarative_base()

class UserRole(enum.Enum):
    ADMIN = "Admin"
    DEVELOPER = "Developer"

class User(Base):
    __tablename__ = 'users'
    
    id = Column(String, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    role = Column(Enum(UserRole), default=UserRole.DEVELOPER)
    projects = relationship('Project', back_populates='owner')

class Project(Base):
    __tablename__ = 'projects'
    
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    owner_id = Column(String, ForeignKey('users.id'))
    owner = relationship('User', back_populates='projects')
    vcs_repository = relationship('VCSRepository', uselist=False, back_populates='project')
    executions = relationship('Execution', back_populates='project')

class VCSRepository(Base):
    __tablename__ = 'vcs_repositories'
    
    id = Column(String, primary_key=True)
    project_id = Column(String, ForeignKey('projects.id'))
    repo_url = Column(String, nullable=False)
    branch = Column(String, default='main')
    cloned_at = Column(DateTime, default=datetime.datetime.utcnow)
    project = relationship('Project', back_populates='vcs_repository')

class ExecutionStatus(enum.Enum):
    RUNNING = "Running"
    COMPLETED = "Completed"
    FAILED = "Failed"

class Execution(Base):
    __tablename__ = 'executions'
    
    id = Column(String, primary_key=True)
    project_id = Column(String, ForeignKey('projects.id'))
    status = Column(Enum(ExecutionStatus), default=ExecutionStatus.RUNNING)
    started_at = Column(DateTime, default=datetime.datetime.utcnow)
    ended_at = Column(DateTime)
    project = relationship('Project', back_populates='executions')