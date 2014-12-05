from flask.ext.wtf import Form, TextField, BooleanField,HiddenField,SelectField,DateField,SubmitField,TextAreaField
from flask.ext.wtf import Required,Email,Length
from wtforms.validators import ValidationError
from models import db,Mailist
from wtforms.ext.sqlalchemy.fields import QuerySelectMultipleField



class TempInqForm(Form):
    name = TextField('Enter any part of the First or Last Name', id='name')
    id=HiddenField(id='id')
    submit = SubmitField('Lookup')
    
def validate_empid(form, field):
        if  (form.act_type.data == 'cnv' and not form.emplid.data):
            raise ValidationError('Employee ID must be filled when action is Conversion')

def enabled_categories():
    return Mailist.query.all()
                                    
class TempDtlForm(Form):
    act_type = SelectField(u'Transaction Type:', choices=[('upd', 'Update'), ('hir', 'Hire'), ('xtn', 'Extension'),('cnv', 'Convert'), ('ter', 'Terminate')],validators=[validate_empid])
    effdt=DateField('Effective Date:',id='effdt',validators = [Required()],format='%Y-%m-%d')
    first_name=TextField('First Name:', id='first_name', validators = [Required()])
    last_name=TextField('Last Name:', id='last_name', validators = [Required()])
    type=SelectField(u'Temp Type:', choices=[('C', 'Consultant'), ('F', 'Fixed Term Contractors'), ('T', 'Temporary Contractor'),('W', 'Temporary Worker'), ('O', 'Other')])
    classification=SelectField(u'Classification:', choices=[('Structural', 'Structural'), ('Full term', 'Full term'), ('Project', 'Project'),('Interim', 'Interim'), ('Intermittent', 'Intermittent'), ('Short Term', 'Short Term')])
    reason=SelectField(u'Action Reason:', choices=[('LOA', 'LOA'), ('Add', 'Add'), ('Short', 'Short'),('Seasonal', 'Seasonal'), ('Project', 'Project'), ('Replace', 'Replace'), ('Other', 'Other')])
    busn_email=TextField('Work Email:', id='email',validators =[Length(min=6,message=(u'Little short for an email address?')),Email(message=(u'That\'s not a valid email address.'))])
    req_num=TextField('Requisition Number:', id='reqnum')
    mgr=TextField('Supervisor:', id='mgr', validators = [Required()])
    supervisor=HiddenField('Supervisor ID:', id='supervisor', validators = [Required()])
    it_end_date=DateField('IT End Date:',id='end_dt',validators = [Required()],format='%Y-%m-%d')
    finance=TextField('Finance Division:', id='finance', validators = [Required()])
    finance_org=TextField('Financial Org:', id='finorg', validators = [Required()])
    hr_contact=HiddenField(id='hr_contact')
    hr_name=TextField('HR Contact:', id='hr_name', validators = [Required()])
    business_title= TextField('Business Title:', id='bus_tit')
    legal_entity=TextField('Legal Entity:', id='legal', validators = [Required()])
    dept=TextField('Department:', id='dept', validators = [Required()])
    location=TextField('Location:', id='location', validators = [Required()])
    remote=BooleanField('Remote:', id='remote')
    busn_phone=TextField('Work Phone:', id='bus_phn')
    vendor_id=TextField('Vendor ID:', id='vndrid')
    it_end_date=DateField('IT End Date:',id='it_end_date',validators = [Required()],format='%Y-%m-%d')
    emplid=HiddenField('Employee ID:', id='emplid')
    action_type = HiddenField(id='action_type') 
    id=HiddenField( id='id')
    emplid=TextField('Employee ID:', id='emplid')
    bill_rate=TextField('Bill Rate:', id='brate')
    hourly_rate=TextField('Hourly Rate:', id='hrate')
    comments=TextAreaField('Comments',id='comments')
    mlsnd=BooleanField('Send Mail:', id='mlsnd')
    mailr = QuerySelectMultipleField(query_factory=enabled_categories,get_label='name', allow_blank=False)
    submit = SubmitField('Update')



    

    
     
    
    
    