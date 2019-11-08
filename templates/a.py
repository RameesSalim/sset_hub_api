
@app.route('/')
def index():
    if session.get('username'):
        # return render_template('index.html')
        return redirect(url_for('attendance'))
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username']  and request.form['password']:
            url = "https://sset.ecoleaide.com"
            username = request.form['username']
            password = request.form['password']
            # session['username'] = username
            new_url = requests.get(url)
            print(new_url.url)
            #Filtering Session ID from the base URL
            session_filter = str(new_url.url)
            session_obj = session_filter.split(';')
            session_obj = ";" + session_obj[1]
            print(session_obj)
            # session['sess'] = session
            #Inputs to submit form
            username = "SSET_" + username 
            # Ecoliade Login Action 
            br = mechanize.Browser()
            br.set_handle_robots(False)
            br.addheaders = [("User-agent","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13")]
            sign_in = br.open(new_url.url)  #the login url
            br.select_form(nr = 0) 
            br.set_all_readonly(False)
            br["username"] =username 
            br["password"] =password  
            logged_in = br.submit()  
            logincheck = logged_in.read()  
            # word = "Change Password"
            if b'Change Password' in logincheck:
                session['username'] = username
                session['value'] = session_obj
                # session['password'] = password
                return redirect(url_for('index'))
        
            # print(logincheck)
            # return redirect(url_for('home'))
        else:
            session['username'] = False
            error = "Invalid Credentials"

    return render_template('login.html', error=error)


@app.route('/attendance', methods=['GET', 'POST'])
def attendance():
    if not session.get('username'):
        # return render_template('index.html')
        return redirect(url_for('login'))
    error = None
    if request.method == 'POST':
        if request.form['date']:
            date = request.form['date']
            print(date)
            new_date = datetime.datetime.strptime(date,"%Y-%m-%d").strftime("%d/%m/%Y")
            print(new_date)
            br = mechanize.Browser()
            br.set_handle_robots(False)
            br.addheaders = [("User-agent","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13")]
            opening_url = "https://sset.ecoleaide.com/search/subjAttendReport.htm" + session['value']
            print(opening_url)
            new_url = br.open(opening_url)
            print(new_url)
            br.select_form(nr = 0) 
            br.set_all_readonly(False)
            # br["fromDate"] =new_date
            # br.form.find_control(id="fromDate")=new_date 
            password_field = br.form.find_control(id="form1_fromDate")
            password_field.value = new_date
            read = br.submit()  
            details = read.read()
            soup = BeautifulSoup(details, 'html5lib') 
            # print(soup.prettify()) 
            #Getting Attributes
            data=[]
            table = soup.find('table', attrs = {'class':'subj-attendance-table'})
            table_body = table.find('tbody')

            rows = table_body.find_all('tr')
            datas = np.array([], dtype=float, ndmin=2)
            i = 0
            for row in rows:
                cols = row.find_all('td')
                cols = [ele.text.strip() for ele in cols]
                data.append([ele for ele in cols if ele])
                data[i] = cols
                i= i+1
            error = data
    return render_template('date.html', error=error)
