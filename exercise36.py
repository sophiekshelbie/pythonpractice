import bokeh.plotting 
import collections 
import json 

MONTHS = { 
    '1': 'January', 
    '2': 'February', 
    '3': 'March', 
    '4': 'April', 
    '5': 'May', 
    '6': 'June', 
    '7': 'July', 
    '8': 'August', 
    '9': 'September', 
    '10': 'October', 
    '11': 'November', 
    '12': 'December' 
} 

def run(): 
    try: 
        with open('birthdayy.json', 'r') as f: 
            birthdays = json.load(f).values() 
    except: 
        print('The "birthdayy.json" file does not exist') 
        exit() 
        
    months = [] 
    for birthday in birthdays: 
        birthday = birthday.split('/') 
        month = str(int(birthday[1])) 
        months.append(MONTHS[month]) 
        
    months = collections.Counter(months) 
        
    months_name = list(months.keys()) 
    months_quantity = list(months.values()) 
    
    bokeh.plotting.output_file('plot.html') 
    plot = bokeh.plotting.figure(x_range=list(MONTHS.values())) 
    plot.vbar(x=months_name, top=months_quantity, width=0.7) 
    bokeh.plotting.show(plot) 
    
if __name__ == '__main__': 
    run()