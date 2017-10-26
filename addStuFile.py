import hashlib
from src.model.db import DB

def main():
    db = DB('src/data/StuInfo.db')
    stufile = open('./studata/2017stu.txt')
    stuinfo = stufile.readlines()
    stufile.close()

    studata = []
    for perStu in stuinfo:
        password = perStu.split('\t')[1].replace('\n', '')
        password = password[len(password)-6:]
        perStuData = {
                'stuid': perStu.split('\t')[0].replace('\n', '').replace(' ', '').replace('\t', ''),
                'pass': hashlib.sha3_512(password.encode()).hexdigest()
            }
        studata.append(perStuData)
        try:
            db.run_sql(
                "INSERT INTO `info` (stuid, pass) VALUES ('%s', '%s')" % (perStuData['stuid'], perStuData['pass']))
        except Exception as e:
            print(perStuData)
            print(e)
            # print(studata)
if __name__ == '__main__':
    main()
