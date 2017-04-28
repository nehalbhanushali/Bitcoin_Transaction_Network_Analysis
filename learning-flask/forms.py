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


  avg_block_size = StringField('avg_block_size', validators=[DataRequired("Please enter avg_block_size.")])
  cost_per_transaction = StringField('cost_per_transaction', validators=[DataRequired("Please enter cost_per_transaction.")])
  difficulty = StringField('difficulty', validators=[DataRequired("Please enter difficulty.")])
  estimated_transaction_volume = StringField('estimated_transaction_volume', validators=[DataRequired("Please enter estimated_transaction_volume.")])
  hash_rate = StringField('hash_rate', validators=[DataRequired("Please enter hash_rate.")])
  market_cap = StringField('market_cap', validators=[DataRequired("Please enter market_cap.")])
  median_confirmation_time = StringField('median_confirmation_time', validators=[DataRequired("Please enter median_confirmation_time.")])
  miners_revenue = StringField('miners_revenue', validators=[DataRequired("Please enter miners_revenue.")])
  n_orphaned_blocks = StringField('n_orphaned_blocks', validators=[DataRequired("Please enter n_orphaned_blocks.")])
  n_transactions = StringField('n_transactions', validators=[DataRequired("Please enter n_transactions.")])
  n_transactions_per_block = StringField('n_transactions_per_block', validators=[DataRequired("Please enter n_transactions_per_block.")])
  n_unique_addresses = StringField('n_unique_addresses', validators=[DataRequired("Please enter n_unique_addresses.")])
  total_bitcoins = StringField('total_bitcoins', validators=[DataRequired("Please enter total_bitcoins.")])
  transaction_fees = StringField('transaction_fees', validators=[DataRequired("Please enter transaction_fees.")])
  transaction_to_trade_ratio_D = StringField('transaction_to_trade_ratio_D', validators=[DataRequired("Please enter transaction_to_trade_ratio_D.")])
  up_down_same = StringField('up_down_same', validators=[DataRequired("Please enter up_down_same.")])

  submit = SubmitField("Check sign of price change")


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



