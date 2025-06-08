from flask import Blueprint, render_template

from .getInformation import getInformation
team1_bp = Blueprint('team1', __name__)

@team1_bp.route('/fullTimeTeacher')
def page1():
    sqlQuery = " SELECT * From shiyan3.teacher t INNER JOIN shiyan3.full_time_teacher f ON t.teacher_id = f.teacher_id;"
    teacherInfo = getInformation(sqlQuery)
    return render_template('team1/full_time_teacher.html', teacherInfo=teacherInfo)

@team1_bp.route('partTimeTeacher')
def page2():
    sqlQuery = """
        SELECT * 
            From shiyan3.teacher t
            INNER JOIN shiyan3.part_time_teacher f
            ON t.teacher_id = f.teacher_id
            ;
    """
    teacherInfo = getInformation(sqlQuery)
    return render_template('team1/part_time_teacher.html', teacherInfo=teacherInfo)

@team1_bp.route('actualStudents')
def page3():
    sqlQuery = "SELECT * From shiyan3.student;"
    studentInfo = getInformation(sqlQuery)
    return render_template('team1/actual_students.html', studentInfo = studentInfo )

@team1_bp.route('student_card/<int:student_id>')
def page4(student_id):
    sqlQuery = "SELECT * FROM shiyan3.student WHERE student_id = %s;"
    student_info= getInformation(student_id, (student_id,))

    return render_template('team1/student_card.html', student_info=student_info[0])

@team1_bp.route('gradStudents')
def page5():
    sqlQuery = "SELECT * From shiyan3.student WHERE category='毕业';"
    studentInfo = getInformation(sqlQuery)
    return render_template('team1/graduated_students.html', studentInfo = studentInfo )

@team1_bp.route('gradStudent_card/<int:student_id>')
def page6(student_id):
    sqlQuery = """
         SELECT * 
        From shiyan3.student s
        INNER JOIN shiyan3.graduated_student g
        ON s.student_id = g.student_id where s.student_id = %s;
    """
    student_info= getInformation(student_id, (student_id,))
    return render_template('team1/grad_student_card.html', student_info=student_info[0])


@team1_bp.route('teacherCourse')
def page7():
    sqlQuery = """
        SELECT c.course_id, c.course_name,c.course_id, c.level,STRING_AGG(t.name, ', ') AS teachers
        FROM shiyan3.course c
        LEFT JOIN shiyan3.teaching_work tw ON c.course_id = tw.course_id
        LEFT JOIN shiyan3.teacher t ON tw.teacher_id = t.teacher_id
        GROUP BY c.course_id, c.course_name,c.course_id, c.level
    """
    courseInfo = getInformation(sqlQuery)

    return render_template('team1/teacher_course.html', courseInfo = courseInfo)

@team1_bp.route('teacherReasearch')
def page8():
    sqlQuery = "SELECT * FROM shiyan3.research_work r INNER JOIN shiyan3.teacher t ON r.teacher_id = t.teacher_id"
    queryInfo = getInformation(sqlQuery)
    return render_template('team1/teacher_research.html', queryInfo = queryInfo )

@team1_bp.route('researchResult')
def page9():
    return render_template('team1/research_result.html')

@team1_bp.route('patentResult')
def page10():
    sqlQuery = "select * from shiyan3.patent"
    queryInfo = getInformation(sqlQuery)
    print(queryInfo[0])
    return render_template('team1/patent_result.html', patentInfo = queryInfo)

@team1_bp.route('textbookResult')
def page11():
    sqlQuery = """
        select t.name, STRING_AGG(tb.name, ',') AS writers 
        FROM shiyan3.textbook t
        JOIN shiyan3.teacher_textbook  tb
        ON tb.textbook_id = t.textbook_id
        GROUP BY t.name; 
        """
    queryInfo = getInformation(sqlQuery)
    return render_template('team1/textbook_result.html', textbookInfo = queryInfo)

@team1_bp.route('reformResult')
def page12():
    return render_template('team1/reformResult.html')


@team1_bp.route('international_information')
def page13():
    return render_template('team1/international_information.html')

