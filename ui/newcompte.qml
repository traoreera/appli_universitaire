import QtQuick 2.7
import QtQuick.Controls 2.15
import QtQuick.Controls.Styles 1.4
import QtQuick.Layouts 1.4

Item{
    Column {
        anchors.centerIn: parent
        spacing: 20
        TextField{
            id: nom
            placeholderText: "nom"
            horizontalAlignment: Text.AlignHCenter
            width: 330
            height: 40
            maximumLength: 40
            font.bold: true
            font.pixelSize: 12
            background: Rectangle {
                radius: 20
                color: "white"
                border.color: 'transparent'
            }
        }
        TextField {

            id: prenom
            placeholderText: "Prenom"
            horizontalAlignment: Text.AlignHCenter
            width: 330
            height: 40
            maximumLength: 40
            font.bold: true
            font.pixelSize: 12
            background: Rectangle {
                radius: 20
                color: "white"
                border.color: 'transparent'

            }
        }
        TextField {

            id: codeEtudiant
            placeholderText: "Code Etudiant"
            horizontalAlignment: Text.AlignHCenter
            width: 330
            height: 40
            maximumLength: 40
            font.bold: true
            font.pixelSize: 12
            background: Rectangle {
                radius: 20
                color: "white"
                border.color: 'transparent'

                }
        }
    }
}