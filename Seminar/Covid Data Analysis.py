import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from datetime import datetime as dt


def pie_chart_india():
    date = input("Enter the date for which rate is to be shown in *yyyy-mm-dd* format: ")
    indiarow1 = df[(df.Date == date)]
    print("---REPORT---")
    total_Confirmed = indiarow1['Confirmed'].sum()
    print("Total confirmed are ", total_Confirmed)
    total_Deceased = indiarow1['Deceased'].sum()
    print("Total death are ", total_Deceased)
    total_Recovered = indiarow1['Recovered'].sum()
    print("Total recovery are ", total_Recovered)
    total_active = (total_Confirmed - total_Deceased - total_Recovered)
    print("Total active are ", total_active)
    d_rate = (total_Deceased / total_Confirmed) * 100
    death_rate = round(d_rate, 2)
    print("The death rate is ", death_rate, "%")
    r_rate = (total_Recovered / total_Confirmed) * 100
    recovery_rate = round(r_rate, 2)
    print("The recovery rate is ", recovery_rate, "%")
    a_rate = (total_active / total_Confirmed) * 100
    active_rate = round(a_rate, 2)
    print("The active rate is ", active_rate, "%")
    piechart = [death_rate, recovery_rate, active_rate]
    labels = ['Death rate', 'Recoveryrate', 'Active rate']
    cols = ['red', 'mediumvioletred', 'lightseagreen']
    plt.pie(piechart, labels=labels, colors=cols, shadow=True, startangle=90, explode=(0.1, 0.1, 0.1),
            autopct='%1.1f%%')
    plt.title(f"Pie chart of covid rate for india -{date}")
    plt.show()


def pie_chart_state():
    state1 = input("Enter the name of state ")
    state = state1.capitalize()
    staterow = df[(df.State == state)]
    date = input("Enter the rate for which rate is to be shown *yyyy-mm-dd* ")
    staterow1 = staterow[(staterow.Date == date)]
    print("---REPORT---")
    total_Confirmed = staterow1['Confirmed'].sum()
    print("Total confirmed are ", total_Confirmed)
    total_Deceased = staterow1['Deceased'].sum()
    print("Total death are ", total_Deceased)
    total_Recovered = staterow1['Recovered'].sum()
    print("Total recovery are ", total_Recovered)
    total_active = (total_Confirmed - total_Deceased - total_Recovered)
    print("Total active are ", total_active)
    d_rate = (total_Deceased / total_Confirmed) * 100
    death_rate = round(d_rate, 2)
    print("The death rate is ", death_rate, "%")
    r_rate = (total_Recovered / total_Confirmed) * 100
    recovery_rate = round(r_rate, 2)
    print("The recovery rate is ", recovery_rate, "%")
    a_rate = (total_active / total_Confirmed) * 100
    active_rate = round(a_rate, 2)
    print("The active rate is ", active_rate, "%")
    piechart = [death_rate, recovery_rate, active_rate]
    labels = ['Death rate', 'Recoveryrate', 'Active rate']
    cols = ['red', 'mediumvioletred', 'lightseagreen']
    plt.pie(piechart, labels=labels, colors=cols, shadow=True, startangle=90, explode=(0.1, 0.1, 0.1),
            autopct='%1.1f%%')
    plt.title(f"Pie chart of covid rate for {state} of {date}")
    plt.show()


def pie_chart_district():
    district1 = input("Enter the name of district ")
    district = district1.capitalize()
    districtrow = df[(df.District == district)]
    date = input("Enter the date for which rate is to be shown *yyyy-mm-dd* ")
    districtrow1 = districtrow[(districtrow.Date == date)]
    print("---REPORT---")
    total_Confirmed = districtrow1['Confirmed'].sum()
    print("Total confirmed are ", total_Confirmed)
    total_Deceased = districtrow1['Deceased'].sum()
    print("Total death are ", total_Deceased)
    total_Recovered = districtrow1['Recovered'].sum()
    print("Total recovery are ", total_Recovered)
    total_active = (total_Confirmed - total_Deceased - total_Recovered)
    print("Total active are ", total_active)
    d_rate = (total_Deceased / total_Confirmed) * 100
    death_rate = round(d_rate, 2)
    print("The death rate is ", death_rate, "%")
    r_rate = (total_Recovered / total_Confirmed) * 100
    recovery_rate = round(r_rate, 2)
    print("The recovery rate is ", recovery_rate, "%")
    a_rate = (total_active / total_Confirmed) * 100
    active_rate = round(a_rate, 2)
    print("The active rate is ", active_rate, "%")
    piechart = [death_rate, recovery_rate, active_rate]
    labels = ['Death rate', 'Recoveryrate', 'Active rate']
    cols = ['red', 'mediumvioletred', 'lightseagreen']
    plt.pie(piechart, labels=labels, colors=cols, shadow=True, startangle=90, explode=(0.1, 0.1, 0.1),
            autopct='%1.1f%%')
    plt.title(f"Pie chart of covid rate for {district} of {date}")
    plt.show()


def vaccination_india():
    india_data = df[(df.State == "India")]
    plt.rcParams["figure.figsize"] = (10, 5)
    xdates = [dt.strptime(dstr, '%d/%m/%Y') for dstr in india_data.Updated_On]
    plt.plot(xdates, india_data.First_Dose_Administered, color='green')
    plt.plot(xdates, india_data.Second_Dose_Administered, color='limegreen')
    plt.legend(['First_Dose_Administered', 'fully_vaccinated'])
    plt.xlabel('Date')
    plt.ylabel('Vaccination_status')
    plt.title("Graph of vaccination status for india")
    plt.fill_between(xdates, india_data.First_Dose_Administered, color='lightgreen')
    plt.fill_between(xdates, india_data.Second_Dose_Administered, color='limegreen')
    plt.gca().xaxis.set_major_locator(mdates.DayLocator((1, 15)))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%d/%m/%Y"))
    plt.setp(plt.gca().get_xticklabels(), rotation=60, ha="right")
    plt.tight_layout()
    plt.show()


def vaccination_state():
    state = input("Enter the state name for which want to shoe the vaccination status ")
    state1 = state.capitalize()
    state_data = df[(df.State == state1)]
    plt.rcParams["figure.figsize"] = (10, 5)
    xdates = [dt.strptime(dstr, '%d/%m/%Y') for dstr in state_data.Updated_On]
    plt.plot(xdates, state_data.First_Dose_Administered, color='green')
    plt.plot(xdates, state_data.Second_Dose_Administered, color='limegreen')
    plt.legend(['First_Dose_Administered', 'fully_vaccinated'])
    plt.xlabel('Date')
    plt.ylabel('Vaccination_status')
    plt.title(f"Graph of vaccination status for {state}")
    plt.fill_between(xdates, state_data.First_Dose_Administered, color='lightgreen')
    plt.fill_between(xdates, state_data.Second_Dose_Administered, color='limegreen')
    plt.gca().xaxis.set_major_locator(mdates.DayLocator((1, 15)))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%d/%m/%Y"))
    plt.setp(plt.gca().get_xticklabels(), rotation=60, ha="right")
    plt.tight_layout()
    plt.show()


def coviddata_monthlyavg_state():
    s_name = input("Enter the state for which want to show graph ")
    s_name1 = s_name.capitalize()
    state_data = df[(df.State == s_name1)]
    state_data.set_index('Date', inplace=True)
    state_data.index = pd.to_datetime(state_data.index)
    data = state_data.resample('1M').mean()
    plt.rcParams["figure.figsize"] = (10, 5)
    fig, ax1 = plt.subplots()
    ax1.set_xticks(data.index.values)
    lns1 = ax1.plot(data.index.values, data.Confirmed, color='blue', label='active cases')
    lns2 = ax1.plot(data.index.values, data.Recovered, color='green', label='recovered cases')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Y1 axis confirmed and recovered cases')
    ax1.yaxis.label.set_color("purple")
    ax2 = ax1.twinx()
    lns3 = ax2.plot(data.index.values, data.Deceased, color='red', label='death cases')
    ax2.set_ylabel('Y2 axis death cases')
    ax2.yaxis.label.set_color("red")
    lns = lns1 + lns2 + lns3
    labs = [l.get_label() for l in lns]
    ax1.legend(lns, labs, loc=0)
    plt.title(f"Graph for confirmed recovered and death cases in monthly average for {s_name} ")
    plt.xticks(rotation=60)
    plt.show()


def coviddata_monthlyavg_district():
    d_name = input("Enter the district for which want to show graph ")
    d_name1 = d_name.capitalize()
    district_data = df[(df.District == d_name1)]
    district_data.set_index('Date', inplace=True)
    district_data.index = pd.to_datetime(district_data.index)
    data = district_data.resample('1M').mean()
    plt.rcParams["figure.figsize"] = (10, 5)
    fig, ax1 = plt.subplots()
    ax1.set_xticks(data.index.values)
    lns1 = ax1.plot(data.index.values, data.Confirmed, color='blue', label='active cases')
    lns2 = ax1.plot(data.index.values, data.Recovered, color='green', label='recovered cases')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Y1 axis confirmed and recovered cases for district')
    ax1.yaxis.label.set_color("purple")
    ax2 = ax1.twinx()
    lns3 = ax2.plot(data.index.values, data.Deceased, color='red', label='death cases')
    ax2.set_ylabel('Y2 axis death cases')
    ax2.yaxis.label.set_color("red")
    lns = lns1 + lns2 + lns3
    labs = [l.get_label() for l in lns]
    ax1.legend(lns, labs, loc=0)
    plt.title(f"Graph for confirmed recovered and death cases in monthly average for {d_name}")
    plt.xticks(rotation=60)
    plt.show()


def date_state():
    url = r"https://api.covid19india.org/csv/latest/districts.csv"
    df = pd.read_csv(url)
    state = input("Enter the name of state ")
    state1 = state.capitalize()
    date = input("Enter the date in yyyy-mm-dd format: ")
    new_df = df.loc[(df['State'] == state1) & (df['Date'] == date)]
    new_df.drop(new_df.index[(new_df['District'] == 'Other State')], axis=0, inplace=True)
    barWidth = 0.30
    districts = new_df['District'].squeeze()
    confirmed = new_df['Confirmed'].squeeze()
    recovered = new_df['Recovered'].squeeze()
    fig, ax = plt.subplots()
    x = np.arange(len(districts))
    ax.bar(x, confirmed, barWidth, color="#206a5d", label='Confirmed')
    ax.bar(x + barWidth, recovered, barWidth, color="#81b214", label='Recovered')
    plt.title(f'District wise Confirmed & Recovered cases of {state} as of - {date}')
    ax.set_xlabel('Districts', fontweight='bold')
    ax.set_ylabel('Cases')
    ax.set_xticks(x + barWidth)
    ax.set_xticklabels(districts, rotation='vertical')
    ax.legend()
    plt.show()


def confirmed():
    confirmed_df.plot(kind='line', x='Date_YMD', figsize=(10, 5), grid=True)
    plt.xlabel('Date')
    plt.ylabel('Confirmed cases')
    plt.title('Confirmed cases - INDIA COVID-19')
    plt.show()


def recovered():
    recovered_df.plot(kind='line', x='Date_YMD', figsize=(10, 5), grid=True)
    plt.xlabel('Date')
    plt.ylabel('Discharged cases')
    plt.title('Discharged cases - INDIA COVID-19')
    plt.show()


def death():
    death_df.plot(kind='line', x='Date_YMD', figsize=(10, 5), grid=True)
    plt.xlabel('Date')
    plt.ylabel('Deceased cases')
    plt.title('Deceased cases - INDIA COVID-19')
    plt.show()


print("***WELCOME TO GRAPHICAL DATA OF COVID-19***")
repeat = input("Enter 'yes' to continue visualising, 'no' to exit ")
while repeat != 'no':
    print("_____________MENU_____________")
    print("1:Covid Rate using Pie Chart")
    print("2:Vaccination Status Graph")
    print("3:Graphical representation of Monthly Average Data ")
    print("4:Bar Graph representation")
    print("5:Exit")
    ch = int(input("Enter the choice:  "))
    if (ch == 1):
        repeat1 = input("Enter 'yes' if want to Continue...otherwise enter 'no' ")
        if repeat1 != 'no':
            url = r"https://api.covid19india.org/csv/latest/districts.csv"
            df = pd.read_csv(url)
            print("__________SUBMENU_________")
            print("1:covid rate for india")
            print("2:covid rate for state")
            print("3:covid rate for district")
            ch1 = int(input("enter the choice "))
            if (ch1 == 1):
                pie_chart_india()
                break
            elif (ch1 == 2):
                pie_chart_state()
                break
            elif (ch1 == 3):
                pie_chart_district()
                break;
        else:
            break;
    elif (ch == 2):
        url = r"http://api.covid19india.org/csv/latest/cowin_vaccine_data_statewise.csv"
        df = pd.read_csv(url)
        df.columns = [c.replace(' ', '_') for c in df.columns]
        repeat2 = input("Enter 'yes' if want to Continue...otherwise enter 'no': ")
        if (repeat2 != 'no'):
            print("__________SUBMENU__________")
            print("1:vaccination status for india")
            print("2:vaccination status for state")
            ch2 = int(input("enter the choice "))
            if (ch2 == 1):
                vaccination_india()
            elif (ch2 == 2):
                vaccination_state()
        else:
            break;
    elif (ch == 3):
        repeat3 = input("Enter 'yes' if want to Continue...otherwise enter 'no': ")
        if repeat3 != 'no':
            print("_________SUBMENU__________")
            print("1:For state")
            print("2:For district")
            ch3 = int(input("enter the choice "))
            url = r"https://api.covid19india.org/csv/latest/districts.csv"
            df = pd.read_csv(url)
            if (ch3 == 1):
                coviddata_monthlyavg_state()
            elif (ch3 == 2):
                coviddata_monthlyavg_district()
        else:
            break;
    elif (ch == 4):
        repeat4 = input("Enter 'yes' if want to Continue...otherwise enter 'no': ")
        if repeat4 != 'no':
            print("________SUBMENU________")
            print("1:For state district wise confirmed and recovered as of given date")
            print("2:For india different states confirmed, recovered and death cases ")
            ch4 = int(input("Enter the choice "))
            if (ch4 == 1):
                date_state()
            elif (ch4 == 2):
                url = r'https://api.covid19india.org/csv/latest/state_wise_daily.csv'
                df = pd.read_csv(url)
                new_df = df[['Date_YMD', 'Status', 'MH', 'KL', 'KA', 'TN', 'UP', 'AP', 'DL', 'WB', 'RJ']]
                confirmed_df = new_df[new_df['Status'] == 'Confirmed']
                recovered_df = new_df[new_df['Status'] == 'Recovered']
                death_df = new_df[new_df['Status'] == 'Deceased']
                print("__________SUBMENU__________")
                nch = int(input("Enter choice\n1 for Confirmed\n2 for Recovered\n3 for Deceased\n"))
                if (nch == 1):
                    confirmed()
                elif (nch == 2):
                    recovered()
                elif (nch == 3):
                    death()
        else:
            break;
    elif (ch == 5):
        break;
print("Thankyou!!Take Care!!")
print("*********STAY HOME STAY SAFE*********")






