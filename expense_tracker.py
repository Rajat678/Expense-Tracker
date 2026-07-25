import pandas as pd
import matplotlib.pyplot as plt
import os

FILE="myexpenses.csv"

if not os.path.exists(FILE):
    pd.DataFrame(columns=["Date","Category","Description","Amount"]).to_csv(FILE,index=False)

def load():
    return pd.read_csv(FILE)

def save(df):
    df.to_csv(FILE,index=False)

def add():
    d=input("Date(YYYY-MM-DD): ")
    c=input("Category: ")
    desc=input("Description: ")
    amt=float(input("Amount: "))
    df=load()
    df.loc[len(df)] = [d,c,desc,amt]
    save(df)
    print("Expense added")

def view():
    df=load()
    print(df if not df.empty else "No data")

def delete():
    df=load()
    print(df)
    i=int(input("Row index to delete: "))
    df=df.drop(i).reset_index(drop=True)
    save(df)

def total():
    df=load()
    print(f"Total Expense: ₹{df['Amount'].sum():.2f}")

def category_report():
    print(load().groupby("Category")["Amount"].sum())

def monthly_report():
    df=load()
    df["Date"]=pd.to_datetime(df["Date"])
    print(df.groupby(df["Date"].dt.to_period("M"))["Amount"].sum())

def pie_chart():
    df=load()
    rep=df.groupby("Category")["Amount"].sum()
    if rep.empty:
        print("No data"); return
    total_amt=rep.sum()
    fig,ax=plt.subplots(figsize=(8,8))
    wedges,_,_=ax.pie(rep.values,autopct="%1.1f%%",startangle=90)
    labels=[f"{k} - ₹{v:.2f}" for k,v in rep.items()]
    ax.legend(wedges,labels,title="Bills",loc="center left",bbox_to_anchor=(1,0.5))
    ax.text(0,0,f"Total\n₹{total_amt:.2f}",ha="center",va="center",fontweight="bold")
    plt.title("Expense Distribution")
    plt.show()

def bar_chart():
    rep=load().groupby("Category")["Amount"].sum()
    rep.plot(kind="bar")
    plt.ylabel("Amount")
    plt.show()

while True:
    print("""
1.Add
2.View
3.Delete
4.Total
5.Monthly Report
6.Category Report
7.Pie Chart
8.Bar Chart
9.Exit
""")
    ch=input("Choice: ")
    if ch=="1": add()
    elif ch=="2": view()
    elif ch=="3": delete()
    elif ch=="4": total()
    elif ch=="5": monthly_report()
    elif ch=="6": category_report()
    elif ch=="7": pie_chart()
    elif ch=="8": bar_chart()
    elif ch=="9": break
    else: print("Invalid choice")
