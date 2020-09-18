def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    try:
        import csv
        matrix = []
        with open(csv_file_path, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                line = []
                for item in row:
                    if item.isdigit():
                        line.append(int(item))
                    else: 
                        line.append(item)
                matrix.append(line)
        return matrix
    except:
        print("Unable to read csv file")

