from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def date_format_checker():
    if request.method == "POST":
        try:
            day = int(request.form["day"])
            month = int(request.form["month"])
            year = int(request.form["year"])
        except ValueError:
            error_message = "Incorrect input format"
            return render_template("index.html", error_message=error_message)

        if day < 1 or day > 31 or month < 1 or month > 12 or year < 1000 or year > 3000:
            error_message = "Invalid date format. Please enter a valid date."
            return render_template("index.html", error_message=error_message)

        date_string = f"{day:02d}/{month:02d}/{year:04d}"
        try:
            datetime.datetime.strptime(date_string, "%d/%m/%Y")
            success_message = "Date format is valid!"
            return render_template("index.html", success_message=success_message)
        except ValueError:
            error_message = "Invalid date format. Please enter a valid date."
            return render_template("index.html", error_message=error_message)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
