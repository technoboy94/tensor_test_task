#!/usr/bin/python1

#queris for creating tables
tables_sql = '''
    CREATE TABLE IF NOT EXISTS Department (
        id INTEGER,
        name VARCHAR,
        parent_dep_id INTEGER, 
        PRIMARY KEY (id),
        FOREIGN KEY (parent_dep_id) REFERENCES Department (id)   
    );
    CREATE TABLE IF NOT EXISTS Employee (
        id INTEGER,
        name VARCHAR,
        dep_id INTEGER, 
        PRIMARY KEY (id),
        FOREIGN KEY (dep_id) REFERENCES Department (id) 
    );
'''

#queries for inserting data
department_sql = "INSERT INTO Department(id, name, parent_dep_id) VALUES "
employee_sql = "INSERT INTO Employee(id, name, dep_id) VALUES "


''' 
    At this query we are getting root parent (office) of Employee with required id by recursion r. 
    Then by another recursion r2 we are getting all the childs (departments) of root (office).
    At the end we are getting names of employee, that have the same dep_id as in the recursive queries.
'''
def get_employee_neighbours(id):
    return '''
    WITH RECURSIVE r2 AS (
        
        WITH RECURSIVE r AS (
            SELECT id, parent_dep_id, name       
            FROM Department 
            WHERE Id IN (SELECT dep_id FROM Employee WHERE id={0})

            UNION ALL

            SELECT T2.id, T2.parent_dep_id, T2.name       
            FROM Department T2
            JOIN r T ON T.parent_dep_id = T2.id
        )
        SELECT id, parent_dep_id, name FROM r
        
        UNION ALL
        
        SELECT T3.id, T3.parent_dep_id, T3.name       
        FROM Department T3
        JOIN r2 T ON T.id = T3.parent_dep_id
    )
    SELECT name FROM employee WHERE dep_id IN (		
        SELECT DISTINCT id FROM r2
        )
        
'''.format(id)