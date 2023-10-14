wrong_inputs="""
<!DOCTYPE html>
<html>
<head>
    <title>Something Went Wrong</title>
</head>
<main>
    <body>
        <h1>Wrong Inputs</h1>
        <p><strong>Something went wrong</strong></p>
    </body>
</main>
<footer></footer>
</html>
"""
student_details="""
<!DOCTYPE html>
<html>
<head>
    <title>Student Details</title>
</head>
<body>
    <h1>Student Details</h1>
    <table border='1'>
        <thead>
            <tr>
                <th>Student ID</th>
                <th>Course ID</th>
                <th>Marks</th>
            </tr>
        </thead>
        <tboady>
            {% for row in D %}
            <tr>
                <td>{{ row[0] }}</td>
                <td>{{ row[1] }}</td>
                <td>{{ row[2] }}</td>
            </tr>
            {% endfor %}
            <tr>
                <td colspan='2' align="center">Total Marks</td>
                <td>{{ sum }}</td>
            </tr>
        </tboady> 
    </table>
</body>
<footer></footer>
</html>
"""
course_details="""
<!DOCTYPE html>
<html>
<head>
    <title>Course Data</title>
</head>
<main>
<body>
    <h1>Course Details</h1>
    <table border='1'>
        <thead>
            <tr>
                <th>Average Marks</th>
                <th>Maximum Marks</th>
            </tr>
        </thead>
        <tboady>
            <tr>
                <td>{{ avg }}</td>
                <td>{{ max }}</td>
            </tr>
        </tboady> 
    </table>
    <img src={{ img }}>
</body>
<footer></footer>
</html>
"""

import sys
from jinja2 import Template as Temp
import matplotlib.pyplot as plt
selec=sys.argv[1]
id=int(sys.argv[2])
data=[]
with open('data.csv','r') as file:
    file.readline()
    if selec=='-s':
        for row in file:
            row=list(map(int,row.strip().split(',')))
            if row[0]==id:
                data.append(row)
    elif selec=='-c':
        for row in file:
            row=list(map(int,row.strip().split(',')))
            if row[1]==id:
                data.append(row)
if len(data)==0:
    with open('output.html','w') as output:
        output.write(wrong_inputs)
elif selec=='-s':
    sum=sum(x[2] for x in data)
    template=Temp(student_details)
    with open('output.html','w') as output:
        output.write(template.render(D=data,id=id,sum=sum))
else:
    marks=[x[2] for x in data if x[1]==id]
    plt.hist(marks)
    plt.xlabel('Marks')
    plt.ylabel('Frequency')
    plt.savefig('plot.png')
    template=Temp(course_details)
    with open('output.html','w') as output:
        output.write(template.render(D=data,id=id,avg=sum(marks)/len(marks),max=max(marks),img='plot.png'))