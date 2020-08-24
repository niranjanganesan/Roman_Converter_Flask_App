from flask import Flask, render_template, request
import requests
import roman_convert

application = Flask(__name__)

@application.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        text_input = request.form.get("fname")
        result = roman_convert.fromRoman(text_input)
        output = result[0]
        Blank_Input = result[1]
        Invalid_Input = result[2]
        if Invalid_Input:
            final_result = 'Invalid Roman numeral: ' +"'"+ text_input +"'"+ '. Please enter a valid input'
        elif Blank_Input:
            final_result = 'Input cannot be blank'
        else:
            final_result = 'The Numeric Equivalent is: ' + str(output)
        return render_template("index.html", text_output = final_result)
    if request.method == 'GET':
        return render_template("index.html")

if __name__ == '__main__':
    application.run(host = '0.0.0.0', debug=True, port='80')
