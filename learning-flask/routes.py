from flask import Flask, render_template, request, session, redirect, url_for

from models import db, User, Place, Classifcation
from forms import SignupForm, LoginForm, AddressForm,ClassifcationForm,RegressionForm

import urllib2
import json
from data_parser import BTCNetwork
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, jsonify


from models import db, User, Place
from forms import SignupForm, LoginForm, AddressForm



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/learningflask'

app.config.from_object(__name__)
db.init_app(app)
app.secret_key = "development-key"





@app.route("/regression", methods=["GET", "POST"])
def regression():
  
  return render_template("regression.html")

@app.route("/success", methods=["GET", "POST"])
def success():

  form=RegressionForm()
  actual_rate_interest='0'
  if request.method == "POST":
    if form.validate() == False:
      print('failed')
      return render_template('success.html', form=form)
    else:
      width = form.width.data 
      mid = form.mid.data
      mid30 = form.mid30.data
      imbalance2 = form.imbalance2.data
      adj_price2 = form.adj_price2.data
      imbalance4 = form.imbalance4.data 
      adj_price4 = form.adj_price4.data
      imbalance8 = form.imbalance8.data
      adj_price8 = form.adj_price8.data

      t30_count = form.t30_count.data
      t30_av = form.t30_av.data 
      agg30 = form.agg30.data
      trend30 = form.trend30.data

      t60_count = form.t60_count.data
      t60_av = form.t60_av.data 
      agg60 = form.agg60.data
      trend60 = form.trend60.data


      t120_count = form.t120_count.data
      t120_av = form.t120_av.data 
      agg120 = form.agg120.data
      trend120 = form.trend120.data

      t180_count = form.t180_count.data
      t180_av = form.t180_av.data 
      agg180 = form.agg180.data
      trend180= form.trend180.data



      data = {
              "Inputs": {
                      "input1":
                      [
                          {
                                  'Column 0': "0",   
                                  '_id': "1493266294.35",   
                                  'width': width,   
                                  'mid': mid,   
                                  'mid30': mid30,   
                                  'imbalance2': imbalance2,   
                                  'adj_price2': adj_price2,   
                                  'imbalance4': imbalance4,   
                                  'adj_price4': adj_price4,   
                                  'imbalance8': imbalance8,   
                                  'adj_price8': adj_price8,   
                                  't30_count': t30_count,   
                                  't30_av': t30_av,   
                                  'agg30': agg30,   
                                  'trend30': trend30,   
                                  't60_count': t60_count,   
                                  't60_av': t60_av,   
                                  'agg60': agg60,   
                                  'trend60': trend60,   
                                  't120_count': t120_count,   
                                  't120_av': t120_av,   
                                  'agg120': agg120,   
                                  'trend120': trend120,   
                                  't180_count': t180_count,   
                                  't180_av': t180_av,   
                                  'agg180': agg180,   
                                  'trend180': trend180,   
                          }
                      ],
              },
          "GlobalParameters":  {
          }
      }



      body = str.encode(json.dumps(data))
      #first service
      url = 'https://ussouthcentral.services.azureml.net/workspaces/f28500a2409240e0912181212c9e7c5e/services/4d873d1de32f4a57b0550f8c1b14b511/execute?api-version=2.0&format=swagger'
      api_key = 'swpXT4QjxL2tNeP2mqWyCwiw+/4FQgarE++f0aanDQ15FUrY6KSk6OH0YQSXtAia6PeG6FErmqo/Oo0kfL67eA=='
      headers= {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

      req = urllib2.Request(url, body, headers)


      

        


      try:
          response = urllib2.urlopen(req)

          result = response.read()
          resp_dict = json.loads(result)
          print(result)
          bitcoinPrice=resp_dict['Results']['output1'][0]['Scored Label Mean']
          
          print("Bit coin price",bitcoinPrice)



          
      except urllib2.HTTPError, error:
          print("The request failed with status code: " + str(error.code))

          # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
          print(error.info())
          print(json.loads(error.read())) 



    return render_template('regression.html',bitcoinPrice=bitcoinPrice,mid=mid)

  elif request.method == 'GET':
    return render_template('success.html',form=form)



@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/fetch")
def fetch():
  return render_template("fetch.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
  if 'email' in session:
    return redirect(url_for('home'))

  form = SignupForm()

  if request.method == "POST":
    if form.validate() == False:
      return render_template('signup.html', form=form)
    else:
      newuser = User(form.first_name.data, form.last_name.data, form.email.data, form.password.data)
      db.session.add(newuser)
      db.session.commit()

      session['email'] = newuser.email
      return redirect(url_for('home'))

  elif request.method == "GET":
    return render_template('signup.html', form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
  if 'email' in session:
    return redirect(url_for('home'))

  form = LoginForm()

  if request.method == "POST":
    if form.validate() == False:
      return render_template("login.html", form=form)
    else:
      email = form.email.data 
      password = form.password.data 

      user = User.query.filter_by(email=email).first()
      if user is not None and user.check_password(password):
        session['email'] = form.email.data 
        return redirect(url_for('home'))
      else:
        return redirect(url_for('login'))

  elif request.method == 'GET':
    return render_template('login.html', form=form)

@app.route("/logout")
def logout():
  session.pop('email', None)
  return redirect(url_for('index'))


@app.route("/classification",methods=["GET", "POST"])
def classification():


  form = ClassifcationForm()

  if request.method == "POST":
    if form.validate() == False:
      return render_template("classification.html", form=form)
    else:

      avg_block_size = form.avg_block_size.data
      cost_per_transaction = form.cost_per_transaction.data
      difficulty = form.difficulty.data
      estimated_transaction_volume = form.estimated_transaction_volume.data
      hash_rate = form.hash_rate.data
      market_cap = form.market_cap.data
      median_confirmation_time = form.median_confirmation_time.data
      miners_revenue = form.miners_revenue.data
      n_orphaned_blocks = form.n_orphaned_blocks.data
      n_transactions = form.n_transactions.data
      n_transactions_per_block = form.n_transactions_per_block.data
      n_unique_addresses = form.n_unique_addresses.data
      total_bitcoins = form.total_bitcoins.data
      transaction_fees = form.transaction_fees.data
      transaction_to_trade_ratio_D = form.transaction_to_trade_ratio_D.data
      up_down_same = form.up_down_same.data


      data = {
          "Inputs": {
                  "input1":
                  [
                      {
                              'Column 0': "1",   
                              'avg-block-size': avg_block_size,
                              'cost-per-transaction': cost_per_transaction,
                              'difficulty': difficulty,
                              'estimated-transaction-volume': estimated_transaction_volume,
                              'hash-rate': hash_rate,
                              'market-cap': market_cap,
                              'median-confirmation-time': median_confirmation_time,
                              'miners-revenue': miners_revenue,
                              'n-orphaned-blocks': n_orphaned_blocks,
                              'n-transactions': n_transactions,
                              'n-transactions-per-block': n_transactions_per_block,
                              'n-unique-addresses': n_unique_addresses,
                              'total-bitcoins': total_bitcoins,
                              'transaction-fees': transaction_fees,
                              'transaction_to_trade_ratio_D': transaction_to_trade_ratio_D,
                              'up_down_same': "0", 
                      }
                  ],
          },
      "GlobalParameters":  {
      }
      }

      body = str.encode(json.dumps(data))

      url = 'https://ussouthcentral.services.azureml.net/workspaces/f28500a2409240e0912181212c9e7c5e/services/debd1df031cf45c5aeee3d36941e28a1/execute?api-version=2.0&format=swagger'
      api_key = '647UvHl1rMv71rlUWmXD/XmmSQmCmy2v0Mg7lI7dNNMKZkwGyp79SNAN7cP3/vvqhUMo3a6Tc9e3uWYFnD06OA=='
      headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

      req = urllib2.Request(url, body, headers)

      try:
        response = urllib2.urlopen(req)

        result = response.read()
        resp_dict = json.loads(result)
        print(result)
        loaneligibilty=resp_dict['Results']['output1'][0]['Scored Labels']
        
        print(loaneligibilty)
        c= Classifcation()
        print(c)
        status=c.get_status(loaneligibilty)
      except urllib2.HTTPError, error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(json.loads(error.read()))
      #return  redirect(url_for('success'))
      if(status=='Accepted'):
        return redirect(url_for('success'))
      else:
        return redirect(url_for('fetch'))


  elif request.method == 'GET':
    return render_template('classification.html', form=form)


@app.route("/")
def home():
    return render_template('index.html', context={})

@app.route("/get_btn", methods=['POST'])
def get_btn():
    btn_address = request.form['btn_address']

    if not btn_address:
        flash('Please enter a valid bitcoin address')
        return redirect(url_for('home'))

    btc = BTCNetwork()
    data = btc.data_parse(origin=btn_address)

    return jsonify(nodes=data[0], links=data[1])

@app.route("/get_cluster", methods=['POST'])
def get_cluster():
    origin = request.form['origin_addr']

    if not origin:
        flash('Please enter a valid bitcoin address')
        return redirect(url_for('home'))

    btc = BTCNetwork()
    nodes, links = btc.data_parse(origin=origin)

    clustered_nodes, clustered_links, number_of_clusters = btc.data_clust(origin, nodes, links)
    return jsonify(nodes=clustered_nodes, links=clustered_links, number_of_clusters=number_of_clusters)



  

if __name__ == "__main__":
  app.run(debug=True)