import cgi
import sqlite3
import html

form = cgi.FieldStorage()

fullname_input = str(form.getfirst("fullname_input", ""))
phone_input = str(form.getfirst("phone_input", ""))
adres_input = str(form.getfirst("adres_input", ""))


action = form.getfirst("action", "")
save = form.getfirst("save", "")
delete = form.getfirst("delete", "")

conn = sqlite3.connect("C:/Users/HP 15-bc401ur/Desktop/3python/database.db" )
curr = conn.cursor()


def getAll():
    if action == "add": 
        tup = (fullname_input, phone_input, adres_input)
        curr.execute("INSERT INTO responsible_person(fullname, phone, adres) VALUES (?, ?, ?)", tup)
        conn.commit()
    if not delete == "":
        curr.execute("DELETE FROM responsible_person WHERE person_id="+delete)
        conn.commit()
    if not save == "":
        t = (fullname_input, phone_input, adres_input, save)
        curr.execute("""Update responsible_person set fullname = ?, phone = ?, adres = ? where person_id = ?""", t)
        conn.commit()

    curr.execute("SELECT * FROM responsible_person ")
    rows = curr.fetchall()
    for row in rows:
        print("""
                                    <tr>
                                        <th scope="row">""" + str(row[0]) + """</th>
                                        <td>""" + str(row[1]) + """</td>
                                        <td>""" + str(row[2])+ """</td>
                                        <td>""" + str(row[3]) + """</td>
                                        <td>
                                            <div class="col">
                                                <form action="/cgi-bin/responsible_person.py">
                                                <button type="submit" class="btn btn-light" data-bs-toggle="modal"
                                                data-bs-target="#editModal">Изменить</button>
                                                <input type="hidden" name="action" value="""+str(row[0])+""">
                                                </form>
                                            </div>
                                        </td>
                                    </tr>
        """)

def editRow():
    if action == "edit":
        pass
    if action != "add" and action != "":
        curr.execute("SELECT * FROM responsible_person WHERE person_id="+action)
        rows = curr.fetchall()
        for row in rows:
            print("""
                          <div class="modal fade" id="editModal" tabindex="-1" aria-labelledby="editModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-lg">
            <div class="modal-content">
                
               <form class="container-fluid" action="/cgi-bin/responsible_person.py">
               <div class="modal-header">
                    <h5 class="modal-title" id="editModalLabel">Изменение строки</h5>
                    
                    <button type="submit" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                         <div class="input-group mb-3">
                            <span class="input-group-text" id="basic-addon1">FullName</span>
                            <input type="text" name="fullname_input" class="form-control" placeholder="Name" aria-label="Name" aria-describedby="basic-addon1">
                        </div>
                        <div class="input-group mb-3">
                            <span class="input-group-text" id="basic-addon1">Phone</span>
                            <input type="text" name="phone_input" class="form-control" placeholder="Phone" aria-label="Phone" aria-describedby="basic-addon1">
                        </div>
                        <div class="input-group mb-3">
                            <span class="input-group-text" id="basic-addon1">Address</span>
                            <input type="text" name="adres_input" class="form-control" placeholder="Address" aria-label="Address" aria-describedby="basic-addon1">
                        </div>
                </div>
                <div class="modal-footer">
                    <button type="submit" name="delete" value="""+action+""" class="btn-sm btn-danger" data-bs-dismiss="modal">Удалить</button>
                    <button type="submit" name="save" value="""+action+""" class="btn btn-dark">Сохранить</button>
                </div>
                <script type="text/javascript">
    window.onload = function () {
        OpenBootstrapPopup();
    };
    function OpenBootstrapPopup() {
        $("#editModal").modal("show");
    }
</script>
                </form>
            </div>
        </div>
    </div>
        """)

print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM"
        crossorigin="anonymous"></script>
         <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <title>Agaka</title>
</head>

<body class="container-fluid p-0 w-100">
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark sticky-top">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">Вычислительная техника</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false"
                aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle active" href="#" id="navbarDropdownMenuLink" role="button"
                            data-bs-toggle="dropdown" aria-expanded="false">
                            Таблицы
                        </a>
                        <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                           <li><a class="dropdown-item " type="submit" href="/cgi-bin/responsible_person.py">Ответственные</a></li>
                            <li><a class="dropdown-item" href="/cgi-bin/auditorium.py">Аудитории</a></li>
                            <li><a class="dropdown-item" href="/cgi-bin/central_processor.py">Процессоры</a></li>
                            <li><a class="dropdown-item" href="/cgi-bin/computer.py">Компьютеры</a></li>
                        </ul>
                    </li>
                    <li class="nav-item">
                        <div class="col">
                            <form action="/cgi-bin/responsible_person.py">
                                <button type="submit"  class="btn btn-light" >Обновить</button>
                                <button type="button" class="btn btn-light" data-bs-toggle="modal"
                            data-bs-target="#addModal" data-bs-whatever="@mdo">Добавить</button>
                            </form>
                        </div>

                    </li>

                </ul>
            </div>
        </div>
    </nav>
    <div class="d-flex justify-content-center mt-1">
        <table class="table table-dark table-hover mb-0">
            <thead>
                <tr>
                    <th scope="col">PersonId</th>
                    <th scope="col">Name</th>
                    <th scope="col">Phone</th>
                    <th scope="col">Address</th>
                </tr>
            </thead>
            <tbody>
""")
getAll()
print("""
            </tbody>
        </table>
    </div>

    <div class="modal fade" id="addModal" tabindex="-1" aria-labelledby="addModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-lg">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="addModalLabel">Добавление строки</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                 <form class="container-fluid" action="/cgi-bin/responsible_person.py" accept-charset="utf-8">
                <div class="modal-body">
                    <div class="input-group mb-3">
                        <input type="text" name="fullname_input" class="form-control" placeholder="Name" aria-label="Name" aria-describedby="basic-addon1" required>
                        <input type="text" name="phone_input" class="form-control" placeholder="Phone" aria-label="Phone" aria-describedby="basic-addon1" required>
                        <input type="text" name="adres_input" class="form-control" placeholder="Address" aria-label="Address" aria-describedby="basic-addon1" required>
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn-sm btn-danger" data-bs-dismiss="modal">Отмена</button>
                    <input type="hidden" name="action" value="add">
                    <button type="submit" class="btn btn-dark">Добавить</button>
                </div>
                </form>
            </div>
        </div>
    </div>

""")
editRow()
print("""
</body>

</html>
""")