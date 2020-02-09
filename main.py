# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import string
import sys
import cgi


seller = ['Соль', 'Дрожжи', 'Масло']
price = [15.04, 552.4, 112.3]
quantity = [135, 11, 52]
rate = ['d', 'e', 'm']
rate_name = ['a','b','c']
req=1
description = ['КГ', 'КГ', 'Литр']
winner = ['ООО Солилецкая', 'ООО ЖарСвежар', 'ООО ЖарСвежар']


print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <title>Закупка по потребителю</title>
            <style>
            body {
                background: url(//i.imgur.com/AgyWMpe.jpg);
                background-size: 110%;
               }
            p {
            """
            """
              align="center";
              font-size: 100px;
              margin-top: 140px;
              margin-left: 43%;
              face="Arial";
            }
             """
             """
            .invisibility {
            opacity: 0;
            position: relative;
            }
            .cwdtable tr:nth-child(2n+1) {background: #f3f8f8}
            .cwdtable {font-size:12px;color:#333333;width:90%;border-width: 1px;border-color: #729ea5;border-collapse: collapse;}
            .cwdtable th {font-size:12px;background:#d7ecef;border-width: 1px;padding: 8px;border-style: solid;border-color: #729ea5;}
            .cwdtable tr {background:#ffffff;}
            .cwdtable td {font-size:12px;border-width: 0.5px;padding: 8px;border-style: solid;border-color: #729ea5;}
            .mobileTable {overflow:auto; width:72%; margin-left: 18.7%;  margin-top:232px;}
            .cwdtable th,.cwdtable td{text-align:center}
            .cwdtable tr:hover {background:#f1f4f4;}

            </style>
        </head>
        <body>""")
print("""


<script>
// Set the date we're counting down to
var countDownDate = new Date("Feb 9, 2020 16:58:15").getTime();

// Update the count down every 1 second
var x = setInterval(function() {

  // Get today's date and time
  var now = new Date().getTime();

  // Find the distance between now and the count down date
  var distance = countDownDate - now;

  // Time calculations for days, hours, minutes and seconds
  var days = Math.floor(distance / (1000 * 60 * 60 * 24));
  var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);

  // Output the result in an element with id="demo"
  document.getElementById("demo").innerHTML = days + "d " + hours + "h "
  + minutes + "m " + seconds + "s ";

  // If the count down is over, write some text
  if (distance < 0) {
    clearInterval(x);
    document.getElementById("demo").innerHTML = "Прием ставок окончен";
    document.getElementsByClassName('invisibility')[0].style= "opacity: 1";
    document.getElementsByClassName('invisibility')[1].style= "opacity: 1";
    document.getElementsByClassName('invisibility')[2].style= "opacity: 1";
    document.getElementsByClassName('invisibility')[3].style= "opacity: 1";
  }
}, 1000);
</script>
"""
"""
<p><font id="demo" size="7" color="white" face="Arial"></font></p>
"""
"""


<div class="mobileTable">

<table class="cwdtable" cellspacing="0" cellpadding="1" border="1">
        <tr>
            <td>Наименование</td>
            <td>Ед. измерения</td>
            <td>Начальная цена</td>
            <td>Количество</td>
            <td>Сумма НМЦК</td>
            <td>&nbsp;</td>
            <td>Шаг снижения цены % (от 0.5 до 1)</td>
            <td>Текущая цена</td>
            <td>Текущая сумма</td>
            <td>Снижение цены %</td>
            <td>Подтверждение участия</td>
            <td>Победитель:</td>
        </tr>""")

form = cgi.FieldStorage()
for i in range(len(rate)):
    rate[i] = form.getfirst(rate_name[i], 0.0)


# Работа с файлом
handle = open(r"D:\py+html\cgi-bin\test.txt", "r")
file_rate = handle.read()
handle.close()
inp1 = str(float(rate[0])+float(file_rate[0:3]))
inp2 = str(float(rate[1])+float(file_rate[4:7]))
inp3 = str(float(rate[2])+float(file_rate[8:]))
rate[0] = float(rate[0])+float(file_rate[0:3])
rate[1] = float(rate[1])+float(file_rate[4:7])
rate[2] = float(rate[2])+float(file_rate[8:])
inp = str(inp1+inp2+inp3)

handle = open(r"D:\py+html\cgi-bin\test.txt", "w")
handle.write(inp)
handle.close()

for i in range(len(seller)):
    print("""
            <tr>
                <td><b>"""f"{seller[i]:.{10}s}""""</b></td>
                <td>"""f"{description[i]:.{20}s}""""</td>
                <td>"""f"{price[i]:.{2}f}""""</td>
                <td>"""f"{quantity[i]:.{0}f}""""</td>
                <td>"""f"{quantity[i]*price[i]:.{2}f}""""</td>
                <td>&nbsp;</td>
                <td> <form><input type='text' name=""")
    print(rate_name[i])
    print("""><input type='submit'></form>
                </td>
                <td>"""f"{price[i]/100*(100-float(rate[i])):.{2}f}""""</td>
                <td>"""f"{(price[i]/100*(100-float(rate[i]))*quantity[i]):.{2}f}""""</td>
                <td>"""f"{rate[i]:.{2}f}""""</td>
                <td>Участвую</td>
                <td class="invisibility">"""f"{winner[i]:.{30}s}""""</td>
            </tr>
        """)
print("<div>"""f"{rate:.{2}f}""""</div>""")
print("""</tbody>
        </table>
        </div>
        <div style: height:'200px'>.</div>
        </body>
        </html>""")
