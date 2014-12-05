from flask import render_template, flash, redirect,request,session,Flask,json
from sqlalchemy import  or_,and_
from sqlalchemy.sql import select
from app import app,mail
from forms import TempInqForm,TempDtlForm
from flask import jsonify
from models import db,Consultant,Vendor,Employee,Mailist
import json
from flask.ext.mail import Message
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#import flask.ext.restless
import flask.ext.sqlalchemy
from flask.ext import restful
from flask.views import View
from flask.ext import restful
from flask.ext import Resource, Api





# index view function suppressed for brevity
PER_PAGE = 10
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
@app.route('/',methods=["GET","POST"])
@app.route('/inq',methods=["GET","POST"])
def inq():
    form = TempInqForm(request.form,csrf_enabled=False)
    if request.method == 'POST':
        if form.id.data:
            session['id'] = form.id.data
            return redirect('/hrtemps/tempdisp')
        else:
            flash('Please enter a valid name')
    return render_template('temps_inq.html', form=form,contexts='Look Up Consultants')


@app.route('/lookup')
def lookup():
      a = request.args.get('q')
      if (a is not None):
          consultants = (Consultant.query.filter((Consultant.first_name +','+ Consultant.last_name).like ('%'+a+ '%')))
      else:
          consultants = (Consultant.query.filter((Consultant.first_name +','+ Consultant.last_name).like ('%')))    
      #consultants = (or_(Consultant.query.filter((Consultant.first_name +','+ Consultant.last_name).like ('%'+'a'+ '%'))))
      json_results=[]
      #return SWJsonify({'consultants':consultants })
      for temps in consultants:
          json_results.append({'id':str(temps.id),'value':temps.last_name + ',' +temps.first_name})
      return json.dumps(json_results)
 
@app.route('/hrinq')
def hrinq():
      a = request.args.get('q')
      consultants = (Employee.query.distinct(Employee.name.like ('%'+a+ '%')))
      json_results=[]
      for temps in consultants:
          compdata=str(temps.id)
          json_results.append({'id':compdata,'value':temps.name})
      return json.dumps(json_results)
  

@app.route('/tempdisp',methods=["GET","POST"])
def tempdisp():
    if 'id' in session:
        tempid=session.get('id')
        s=Consultant.query.filter(Consultant.id == tempid)
    if request.method == 'POST':
        flash('Here are the temp Details')
        return render_template('tempedit.html')

    return render_template('tempdisp.html', s=s)

@app.route('/mgrlookup')
def lookup_manager():
    a = request.args.get('q')
    if (a is not None):
        consultants = (Employee.query.filter(Employee.name.like ('%'+ a +'%')))
    else:
        consultants = (Employee.query.filter(Employee.name.like ('%')))
    json_results=[]
    for temps in consultants:
        compdata=str(temps.id) + ';' + temps.location  + ';' + temps.legal_entity  + ';' + temps.dept
        json_results.append({'id':compdata,'value':temps.name})
       #json_results.append({'id':temps.id,'value':temps.name})
    return json.dumps(json_results)

@app.route('/gethr')
def gethr():
    a = request.args.get('q')
    if (a is not None):
        consultants = (Employee.query.get(a))
        
    json_results=[]
    #for temps in consultants:
        #compdata=str(temps.id) 
        #json_results.append({'id':compdata,'value':temps.name})
    json_results ={'id':str(consultants.id),'value':consultants.name}
    #json_results = {"id":"2","value":"Sandip"}
    return jsonify(json_results)  
 
@app.route('/tempedit',methods=["GET","POST"])
def tempedit():
    s=Consultant.query.get((request.args['id'],request.args['effdt'],request.args['type']))
    form=TempDtlForm(obj=s,csrf_enabled=False)

     
    if request.method == 'POST' and form.validate():
        if form.act_type.data != 'upd':
            s1=Consultant(id=form.id.data,effdt=form.effdt.data,action_type=form.act_type.data,
                          last_name=form.last_name.data,first_name=form.first_name.data,reason=form.reason.data)
            db.session.add(s1)
        else:
            form.populate_obj(s)
        db.session.commit()
        
        if  (form.mlsnd.data == 1):
            me='hrnotify@polycom.com'
            html = '<strong>This is funny</strong>'  
            msg=MIMEMultipart('alternative')
            msg['To']= 'sandip.sinha@polycom.com'
            msg['Subject'] = 'Test Email'
            smtpserver=smtplib.SMTP('mailrelay.polycom.com',25)
            part1=MIMEText(html,'html')
            msg.attach(part1)
            #smtpserver.login('austin\hrnotify','P0lyc0m1')
            smtpserver.ehlo()
            smtpserver.sendmail(me,msg['To'],msg.as_string()) 
            flash('The Temp Details have been Saved and Mail has been Sent')
        else:
            flash('The Temp Details have been Saved ')
        return redirect('/hrtemps/tempdisp')
       
    return render_template('tempedit.html',form=form)

@app.route('/tempdel',methods=["GET"])
def tempdel():
    s=Consultant.query.get((request.args['id'],request.args['effdt'],request.args['type']))
    db.session.query(Consultant).filter(Consultant.id==request.args['id'],Consultant.effdt==request.args['effdt'],Consultant.action_type==request.args['type']).delete()
     
    db.session.commit()
    flash('The Temp Row has been Deleted')
    return redirect('/hrtemps/tempdisp')
       
@app.route('/finlookup')
def finlookup():
    a = request.args.get('q')
    consultants = (Employee.query.distinct(Employee.finance.like ('%'+ a +'%')))
    json_results=[]
    for temps in consultants:
        json_results.append({'id':temps.finance,'value':temps.finance})
       #json_results.append({'id':temps.id,'value':temps.name})
    return json.dumps(json_results) 

 
@app.route('/gettemp')
def gettemp():
    if request.method == 'GET':
          results = Consultant.query.limit(10).offset(0).all()
      
    
    json_results = []
    for result in results:
      d = {'First_name': result.first_name,
           'Last_name': result.last_name,
           'Type': result.type,
           'Classification': result.classification,
           'Business_title': result.business_title,
           'Location': result.location,
           'Department': result.dept,
           'Business_Email': result.busn_email,
           'Finance': result.finance,
           'Financial_org': result.finance_org,
           'Legal_Entity': result.legal_entity}
    json_results.append(d)

    return jsonify(items=json_results)

todos = {}

class gethrtemp(Resource):
    def get(self, todo_id):
        return {todo_id: 3}

    def put(self, todo_id):
        #todos[todo_id] = request.form['data']
        return {todo_id: 3}

api.add_resource(gethrtemp, '/<string:todo_id>')
      

if __name__ == '__main__':
        app.run()   
