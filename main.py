from datetime import datetime
from flask import Flask, jsonify, request

app = Flask(__name__)


# Все занятия за весь период
lessons = []


@app.route('/add_lesson', methods=['POST'])
def add_lesson():
    lesson_date = datetime.strptime(request.json['date'], "%d.%m.%Y")
    lesson = {
        'name': request.json['lesson'],
        'date': lesson_date,
        'hours': request.json['hours']
    }
    lessons.append(lesson)
    return '', 200


@app.route('/month_stat/<int:month>', methods=['GET'])
def get_month_statistic(month):
    stat = {}

    for element in lessons:
        if element['date'].month == month:
            l_name = element['name']
            if l_name in stat:
                stat[l_name] = stat.get(l_name) + element['hours']
            else:
                stat[l_name] = element['hours']

    return jsonify({'statistic': stat})


@app.route('/all', methods=['GET'])
def get_all():
    return jsonify({'statistic': lessons})


if __name__ == '__main__':
    app.run(debug=True)
