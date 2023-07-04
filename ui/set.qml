import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.LocalStorage 2.0

Item{

    Connections {
        id: dbConnection
        target: SQLite.openDatabaseSync("./Login_setup/login.db", "1.0", "Login Database", 1000000)
        Component.onCompleted: {
            var nameToSearch = username.text// Le nom à rechercher
            var passwdToSearch = password.text
            var query = "SELECT * FROM user WHERE name = ? AND password = ?"
            var result = dbConnection.transaction(function(tx) {
                var rs = tx.executeSql(query, [nameToSearch])
                return rs.rows
            })
            if (result.length > 0) {
                var row = result.item(0)
                console.log("ID:", row.id, "Name:", row.name, "Email:", row.email)
            } else {
                console.log("Aucun utilisateur trouvé avec le nom:", nameToSearch)
            }
        }
    }
}
