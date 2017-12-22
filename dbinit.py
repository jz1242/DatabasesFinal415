import os


def main(db):
    data_path = "data/sr28asc/"
    output_path = "db/"
    sql_filename = "USDA_data.sql"
    max_row_num = 1000

    cwd = os.getcwd()
    file_path = os.path.join(cwd, data_path)
    filenames = [
        "FD_GROUP.txt",
        "FOOD_DES.txt",
        "NUTR_DEF.txt",
        "NUT_DATA.txt",
        "WEIGHT.txt"
    ]
    tablenames = [
        "FOOD_GROUP_DESCRIPTION",
        "FOOD_DESCRIPTION",
        "NUTRIENT_DEFINITION",
        "NUTRIENT_DATA",
        "WEIGHTS"
    ]
    filenames = [file_path + f for f in filenames]

    output_dir = os.path.join(cwd, output_path)
    sql_file = open(output_dir + sql_filename, "w+")
    for table, data_file in zip(tablenames, filenames):
        data_rows = parse_usda_file(data_file)[:max_row_num]
        sql_rows = get_insert_sql(table, data_rows)
        for row in sql_rows:
            sql_file.write(row.encode('UTF-8'))
        sql_file.write('\n')


def parse_usda_file(filename):
    datafile = open(filename, "rU")
    rows = []
    for line in datafile:
        datarow = [unicode(data, 'cp1252') for data in line.split('^')]
        rows.append(datarow)

    return rows


def get_insert_sql(table, rowdata):
    # Generate insert sql command for each row
    sqlcmds = []
    for row in rowdata:
        row = parse_row_to_sql(row)
        insert_params = "(" + ",".join(row) + ")"
        sqlcmds.append("insert into " + table + " values " + insert_params + ";\n")

    return sqlcmds


def parse_row_to_sql(row):
    for i in xrange(len(row)):
        data = row[i]
        try:
            float(data)
        except ValueError:
            if data.find('~') == -1:
                row[i] = '0'
            else:
                data = data.strip().strip('~')
                data = data.replace('\'', '\'\'')
                data = data.replace('\"', '\"\"')
                row[i] = '\'' + data + '\''
    return row


if __name__ == "__main__":
    main(None)