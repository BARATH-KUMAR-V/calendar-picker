from flask import Flask, request, render_template_string
from datetime import datetime
app = Flask(__name__)

HTML = """
<!DOCTYPE html><html><body style="font-family:Arial;max-width:450px;margin:60px auto">
<h2>Calendar Picker</h2>
<form method="POST">
  <label>Select a Date:</label><br><br>
  <input type="date" name="date" value="{{ today }}" style="padding:8px;font-size:16px" required />
  <br><br>
  <button type="submit" style="padding:10px 20px;font-size:15px;background:#1976d2;color:white;border:none;border-radius:6px;cursor:pointer">Show Date</button>
</form>
{% if selected %}
<div style="background:#e3f2fd;padding:16px;margin-top:20px;border-radius:8px">
  <b>Selected Date:</b> {{ selected }}<br>
  <b>Day:</b> {{ day }}<br>
  <b>Month:</b> {{ month }}<br>
  <b>Year:</b> {{ year }}
</div>
{% endif %}
</body></html>
"""

@app.route("/", methods=["GET","POST"])
def index():
    today = datetime.today().strftime("%Y-%m-%d")
    selected = day = month = year = None
    if request.method == "POST":
        d = datetime.strptime(request.form["date"], "%Y-%m-%d")
        selected = d.strftime("%d %B %Y")
        day = d.strftime("%A")
        month = d.strftime("%B")
        year = d.year
    return render_template_string(HTML, today=today, selected=selected, day=day, month=month, year=year)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
