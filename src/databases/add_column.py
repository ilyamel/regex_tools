import re

# Add a new column to the last position of table's ddl

create_sql = '''
  CREATE TABLE test
   ( id numeric(38,0),
   data1 varchar(255),
   primary key (id))
   tablespace test_tab_space1
   
     CREATE or replace TABLE test2
   ( id numeric(38,0),
   data1 varchar(255),
   data2 numeric(38, 0),
   constraint "fk_data2" FOREIGN KEY ("data2")
          REFERENCES "schema1"."table1" ("data2_id"))
   tablespace test_tab_space1
   
        CREATE or replace TABLE test2
   ( id numeric(38,0),
   data4 varchar(8000),
   data5 numeric(38, 0),
   is_checked boolean);
   tablespace test_tab_space1
'''

column_name = 'data7'
column_type = 'varchar(14)'

replacement = r'\1\2,\n"{}" {}\5'.format(column_name,
                                         column_type)
print(replacement)

create_sql = re.sub(r'(CREATE TABLE|CREATE OR REPLACE TABLE| CREATE TABLE IF NOT EXIST)(((?!(PRIMARY KEY|CONSTRAINT)).)*)(,\n)?(\s)*(?(5)(?=(CONSTRAINT |PRIMARY KEY))|(?=(\)\n|\);\n)))',
                    replacement,
                    create_sql,
                    flags=re.DOTALL| re.IGNORECASE)

print(create_sql)
