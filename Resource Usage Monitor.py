import psutil
import mysql.connector
import smtplib
from email.message import EmailMessage

flag={"CPU":0,"Disk":0,"RAM":0}

def check_cpu():
    usage=psutil.cpu_percent(interval=1)
    #compare CPU usage level
    if usage>80:
        flag["CPU"]=1
    return usage
    
def check_disk():
    temp=[]
    for path in psutil.disk_partitions(all=False):
        p=path.mountpoint
        #Disconnected pendrive/external ssd can raise error 
        try:
            stat=psutil.disk_usage(p)
            usage=stat.percent
        except (PermissionError, OSError):
            continue
        temp.append((p,usage))
        #compare disk usage level of particular partition
        if usage>75:
            flag["Disk"]=1
            break
    return temp

def check_memory():
    stat=psutil.virtual_memory()
    usage=stat.percent
    #compare RAM usage level
    if usage>80:
        flag["RAM"]=1
    return usage
    
def get_recipients():
    conn=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='Support_Team')
    if conn.is_connected()== False:
        print("Unable To Connect To Support Team...")
        #returning empty list if failed to fetch detail
        return [],[]
    cur=conn.cursor()
    cur.execute("SELECT * FROM tech_members")
    results = cur.fetchall()
    conn.close()
                #Column 1-> First Name
    Names=[]    #Column 2-> Last Name
    Emails=[]   #Column 3-> Email Address
    for x in results:
        Names.append(x[0]+' '+x[1])
        Emails.append(x[2])
    return Names,Emails

def record_alert(Type,Msg):
    conn=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='Support_Team')
    if conn.is_connected()== False:
        #Raising error for missing record log and return
        print("Alert Cannot Be Recorded To Database...")
        return
    cur=conn.cursor()
    cur.execute("INSERT INTO Alert_Log VALUES (NOW(),%s,%s)",(Type,Msg))
    conn.commit()
    print("Alert Raised")
    print("WARNING: ",Msg)
    conn.close()
    
def alert_email(subject,body,email):
    # Gmail SMTP server details
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    #Email credentials
    sender="xyz@gmail.com"  #Sender's E-Mail
    reciever=email
    password="**************"   #Password (Gmail user enter their App key)
    # Create the email
    msg = EmailMessage()
    msg["From"] =sender
    msg["To"] = reciever
    msg["Subject"] = subject
    msg.set_content(body)
    try:
        # Connect to Gmail SMTP server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Secure the connection
        server.login(sender, password)
        server.send_message(msg)
        server.quit()

        print("To:",reciever,"\t[Email sent successfully!]")

    except Exception as e:
        print("Failed to send email:", e)


def report_generate(cpu,p,disk,ram):
    res=[]
    text1=text2=text3=""
    #check which resource limit exceed
    if flag["CPU"]:
        res.append("CPU")
        text1=f"C.P.U. Usage: {cpu}%.\n"
    if flag["Disk"]:
        res.append("Disk")
        text2=f"Disk Partition {p} Usage: {disk}%.\n"
    if flag["RAM"]:
        res.append("RAM")
        text3=f"R.A.M. Usage: {ram}%.\n"
        
    res=", ".join(res)
    subject="{} Limit Reached.".format(res)
    #Database log update 
    record_alert(res,subject)
    #Fetch support team details
    names,emails=get_recipients()
    #set mail body for individual
    for i in range(len(names)):
        body='''\n______RESOURCE ALERT_______\n\nDear {},
        Following resources usage has reached its limit.
        \t{}\t{}\t{}\nPlease check active processes and available hardware to ensure flawless execution & smooth user experience.'''.format(names[i],text1,text2,text3)
        #calling function to send mail
        alert_email(subject,body,emails[i])

#calling resource monitor functions
cpu=check_cpu()
disks=check_disk()
ram=check_memory()
#check flags to ensure if alert needed
for x in flag.values():
    if x != 0:
        health=1
        break
    else:
        health=0
if health:
    #generate alert for unhealthy state
    print("-SYSTEM IS IN UNHEALTHY STATE-\n")
    p,disk=disks[-1]
    report_generate(cpu,p,disk,ram)
else:
    print("-SYSTEM IS IN HEALTHY STATE-\n")
print("C.P.U. Usage->",cpu)
for p,disk in disks:
    print("Disk Usage","for",p,"->",disk)
print("RAM Usage->",ram)
        
