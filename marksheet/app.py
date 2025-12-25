from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    step = 1
    student = ""
    count = 0
    subjects = []
    totals = []
    obtained = []
    total_marks = 0
    obtained_marks = 0
    percentage = 0
    result = ""

    if request.method == "POST":
        step = int(request.form["step"])

        # Step 1: Student name
        if step == 1:
            student = request.form["student"]
            step = 2

        # Step 2: Number of subjects
        elif step == 2:
            student = request.form["student"]
            count = int(request.form["count"])
            step = 3

        # Step 3: Subject names
        elif step == 3:
            student = request.form["student"]
            count = int(request.form["count"])
            for i in range(count):
                subjects.append(request.form[f"subject{i}"])
            step = 4

        # Step 4: Marks
        elif step == 4:
            student = request.form["student"]
            count = int(request.form["count"])

            for i in range(count):
                subjects.append(request.form[f"subject{i}"])
                t = int(request.form[f"total{i}"])
                o = int(request.form[f"obtained{i}"])
                totals.append(t)
                obtained.append(o)
                total_marks += t
                obtained_marks += o

            percentage = (obtained_marks / total_marks) * 100
            result = "PASS" if percentage >= 35 else "FAIL"
            step = 5

    return render_template(
        "index.html",
        step=step,
        student=student,
        count=count,
        subjects=subjects,
        totals=totals,
        obtained=obtained,
        total_marks=total_marks,
        obtained_marks=obtained_marks,
        percentage=percentage,
        result=result
    )

if __name__ == "__main__":
    app.run(debug=True)
