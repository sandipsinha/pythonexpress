
from sqlalchemy import Table, Column, Integer, ForeignKey,String,Boolean,Date,Text,Float,Numeric,DateTime
from sqlalchemy.orm import relationship, backref

import flask
from flask import Flask
import json 
 
 
from app import db


DEF_RSN = 'Add'

class Serializer(object):
  __public__ = None
  "Must be implemented by implementors"

  def to_serializable_dict(self):
    dict = {}
    for public_key in self.__public__:
      value = getattr(self, public_key)
      if value:
        dict[public_key] = value
    return dict

class SWEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, Serializer):
      return obj.to_serializable_dict()
    if isinstance(obj, (datetime)):
      return obj.isoformat()
    return json.JSONEncoder.default(self, obj)



class Consultant(db.Model,Serializer):
    __tablename__ = 'consultant'
    id = db.Column(Integer, primary_key = True)
    effdt = db.Column(DateTime, primary_key = True)
    action_type = db.Column(String(3), primary_key = True)
    reason = db.Column(String(20), index=True,default = DEF_RSN)
    last_name =  db.Column(String(50))
    first_name =  db.Column(String(50))
    type = db.Column(String(2))
    classification = db.Column(String(50))
    req_num = db.Column(String(50))
    business_title = db.Column(String(50))
    remote=db.Column(Boolean)
    location=db.Column(String(50))
    dept=db.Column(String(50))
    emplid=db.Column(String(11))
    busn_email=db.Column(String(50))
    busn_phone=db.Column(String(50))
    supervisor=db.Column(String(11))
    it_end_date=db.Column(Date)
    finance=db.Column(String(50))
    finance_org=db.Column(String(50))
    hr_contact=db.Column(String(50))
    legal_entity=db.Column(String(50))
    bill_rate=db.Column(String(30))
    hourly_rate=db.Column(String(30))
    comments=db.Column(Text)
    vendor_id = db.Column(Integer, ForeignKey('vendor.id'))
    
def __init__(self,effdt,action_type,reason,last_name,first_name,vendor_id):
    self.effdt =effdt
    self.action_type = action_type
    self.reason = reason
    self.last_name=last_name
    self.first_name=first_name
    self.vendor_id = vendor_id

    def __repr__(self):
        return (u"<Consultant ('%s','%s')> " % (self.last_name,',',self.first_name)).encode('utf-8')
    
class Vendor(db.Model,Serializer):
    __tablename__ = 'vendor'
    id = db.Column(db.Integer, primary_key = True)
    name =  db.Column(db.String(70))
    consultants = relationship('Consultant', backref='vendor',
                                lazy='dynamic')

    def __repr__(self):
        return '<Vendor %r>' % (self.name )
    
class Employee(db.Model,Serializer):
    __public__ = 'Employee'
    id = db.Column(Integer, primary_key = True)
    effseq = db.Column(Integer)
    effdt = db.Column(Date)
    action = db.Column(String(3))
    reason = db.Column(String(3))
    empl_status= db.Column(String(3))
    name =  db.Column(String(100))
    business_title =  db.Column(String(65))
    busn_email = db.Column(String(65))
    busn_phone = db.Column(String(65))
    dept = db.Column(String(65))
    legal_entity = db.Column(String(65))
    location=db.Column(String(65))
    vp=db.Column(String(11))
    manager=db.Column(String(11))
    pref_name=db.Column(String(100))
    hire_dt=db.Column(Date)
    cmpny_sen_dt=db.Column(Date)
    service_dt=db.Column(Date)
    req_num=db.Column(String(10))
    finance=db.Column(String(30))
    finance_org=db.Column(String(30))
    division=db.Column(String(30))
    currency_cd=db.Column(String(5))
    var_pay_type=db.Column(String(20))
    
    def __repr__(self):
        return (u"<Employee ('%s','%s')> " % (self.pref_name,',',self.name)).encode('utf-8')
    
class Mailist(db.Model,Serializer):
    __public__ = 'Mailist'
    #id = db.Column(db.Integer, primary_key = True)
    emailid = db.Column(String(50),primary_key = True)
    name =  db.Column(db.String(70))
    
    
