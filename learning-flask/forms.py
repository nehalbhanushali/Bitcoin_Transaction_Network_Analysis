from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
  first_name = StringField('First name', validators=[DataRequired("Please enter your first name.")])
  last_name = StringField('Last name', validators=[DataRequired("Please enter your last name.")])
  email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email("Please enter your email address.")])
  password = PasswordField('Password', validators=[DataRequired("Please enter a password."), Length(min=6, message="Passwords must be 6 characters or more.")])
  submit = SubmitField('Sign up')

class LoginForm(Form):
  email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email("Please enter your email address.")])
  password = PasswordField('Password', validators=[DataRequired("Please enter a password.")])
  submit = SubmitField("Sign in")

class AddressForm(Form):
  address = StringField('Address', validators=[DataRequired("Please enter an address.")])
  submit = SubmitField("Search")


class ClassifcationForm(Form):
  amount_requested = StringField('Loan Amount', validators=[DataRequired("Please enter your loan amount.")])
  zip_code = StringField('Zip Code', validators=[DataRequired("Please enter a zip code.")])
  employment_length = StringField('Employment Length', validators=[DataRequired("Please enter a employment length")])
  risk_score = StringField('Risk Score', validators=[DataRequired("Please enter a credit score")])
  debt_to_income_ratio = StringField('Debt to Income Ratio', validators=[DataRequired("Please enter a credit score")])
  submit = SubmitField("Check loan eligibilty")


class RegressionForm(Form):
  width = StringField('Width', validators=[DataRequired("Please enter a width")])
  mid = StringField('Width', validators=[DataRequired("Please enter a width")])
  mid30 = StringField('enter Mid Price in last 30 seconds', validators=[DataRequired("Total Payment Inv")])
  imbalance2 = StringField('Imbalance 2 Power of 2', validators=[DataRequired("Please enter a Rovloving Utilization")])
  adj_price2 = StringField('Adjacent Price power of 2', validators=[DataRequired("Please enter a Loan Status")])
  imbalance4 = StringField('imbalance4', validators=[DataRequired("Please enter Fico Range Grade")])
  adj_price4 = StringField('adj_price4', validators=[DataRequired("Please enter a Ttotal Rec PRNCP")])
  imbalance8 = StringField('imbalance8', validators=[DataRequired("Please enter a Revolivng Balance")])
  adj_price8 = StringField('adj_price8', validators=[DataRequired("Please enter a Grade based on Ing last 6 months")])
  t30_count = StringField('t30_count', validators=[DataRequired("Please enter a Acc Open Past 24 months")])
  t30_av = StringField('t30_av', validators=[DataRequired("Installment")])
  agg30 = StringField('agg30', validators=[DataRequired("Last Payment Amount")])
  trend30 = StringField('trend30', validators=[DataRequired("Funder Amount Inv")])
  t60_count = StringField('t60_count', validators=[DataRequired("Total Acc")])
  t60_av = StringField('t60_av', validators=[DataRequired("Credit Age")])
  agg60 = StringField('agg60', validators=[DataRequired("Issue Date")])
  trend60 = StringField('trend60', validators=[DataRequired("Please enter a Annual Inc")])
  t120_count = StringField('t120_count', validators=[DataRequired("Please enter a Mean FICO")])
  t120_av = StringField('t120_av', validators=[DataRequired("Please enter a cluster")])
  agg120 = StringField('agg120')
  trend120 = StringField('trend120', validators=[DataRequired("Issue Date")])
  t180_count = StringField('t180_count', validators=[DataRequired("Please enter a Annual Inc")])
  t180_av = StringField('t180_av', validators=[DataRequired("Please enter a Mean FICO")])
  agg180 = StringField('agg180', validators=[DataRequired("Please enter a cluster")])
  trend180 = StringField('trend180')

  
  submit = SubmitField("Get bitcoin price")



