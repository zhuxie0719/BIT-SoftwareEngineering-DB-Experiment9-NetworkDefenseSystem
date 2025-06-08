from flask import Blueprint, render_template
<<<<<<< HEAD
from flask import Flask, render_template, request, jsonify, session
from flask import Flask, render_template, request, jsonify, session
import psycopg2
from datetime import datetime, timedelta
team2_bp = Blueprint('team2', __name__)

DB_CONFIG = {
    'host': '1.92.77.154',
    'port': '26000',
    'dbname': 'network_security_research',
    'user': 'db_admin',
    'password': 'DBAdmin@SuperSecure!2024'
}

def get_db_connection():
    return psycopg2.connect(**DB_CONFIG)
@team2_bp.route('library')
def page3():
    return render_template('team2/library.html')


@team2_bp.route('search_books', methods=['POST'])
def page4():
      # 获取查询参数
        keyword = request.form.get('keyword', '').strip()

        # 构建查询语句
        query = "SELECT * FROM library_schema.book WHERE 1=1"
        params = []

        if keyword:
            query += " AND title LIKE %s OR book_id LIKE %s"
            params.extend([f"%{keyword}%", f"%{keyword}%"])

            # 执行查询
        try:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute(query, params)
            books = cur.fetchall()

            # 将查询结果转换为字典列表
            columns = [desc[0] for desc in cur.description]
            books_list = [dict(zip(columns, row)) for row in books]

            return jsonify(books_list)

        except Exception as e:
            return jsonify({'error': str(e)}), 500

        finally:
            cur.close()
            conn.close()


@team2_bp.route('/borrow_books', methods=['GET'])
def page5():
    # 从session获取用户名
    user_name = session.get('user_name', None)
    if not user_name:
        return jsonify({'error': '用户未登录'}), 401

    try:
        conn = get_db_connection()
        cur = conn.cursor()

        # 查询借阅记录
        query = """
                SELECT book.title, \
                       borrow_record.borrow_date, \
                       borrow_record.due_date,
                       CASE
                           WHEN borrow_record.return_date IS NOT NULL THEN '已归还'
                           WHEN CURRENT_DATE > borrow_record.due_date THEN '逾期'
                           ELSE '借阅中'
                           END AS status
                FROM library_schema.borrow_record
                         JOIN library_schema.book ON borrow_record.book_id = book.book_id
                WHERE borrow_record.user_id = %s
                ORDER BY borrow_record.borrow_date DESC \
                """
        cur.execute(query, (user_name,))
        records = cur.fetchall()

        # 转换为字典列表
        columns = [desc[0] for desc in cur.description]
        records_list = [dict(zip(columns, row)) for row in records]

        # 查询借阅总数
        cur.execute("SELECT COUNT(*) FROM library_schema.borrow_record WHERE user_id = %s", (user_name,))
        total_records = cur.fetchone()[0]

        return jsonify({
            'total': total_records,
            'records': records_list
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cur.close()
        conn.close()

@team2_bp.route('/borrow_books', methods=['POST'])
def page6():
    book_id = request.form.get('book_id')
    # 从session获取用户名
    user_name = session.get('user_name', None)
    if not user_name:
        return jsonify({'success': False, 'message': '用户未登录'}), 401

    try:
        conn = get_db_connection()
        cur = conn.cursor()

        # 检查书籍状态
        cur.execute("SELECT is_borrowed FROM library_schema.book WHERE book_id = %s", (book_id,))
        status = cur.fetchone()[0]

        if status == 'false':
            return jsonify({'success': False, 'message': '书籍当前不可借阅'}), 400

        # 更新书籍状态
        cur.execute("UPDATE book SET is_borrowed = 'true' WHERE book_id = %s", (book_id,))

        # 添加借阅记录
        cur.execute("""
                    INSERT INTO library_schema.borrow_record (book_id, user_id, borrow_date, due_date)
                    VALUES (%s, %s, CURRENT_DATE, CURRENT_DATE + INTERVAL '30 days')
                    """, (book_id, user_name))

        conn.commit()
        return jsonify({'success': True, 'message': '借阅成功'})

    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

    finally:
        cur.close()
        conn.close()

=======

team2_bp = Blueprint('team2', __name__)

@team2_bp.route('/page3')
def page3():
    return render_template('page3.html')

@team2_bp.route('/page4')
def page4():
    return render_template('page4.html')
>>>>>>> 1faf378cef6a63a7d39706f752d46a00da392057
